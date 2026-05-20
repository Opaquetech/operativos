import psutil
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import datetime
from pathlib import Path

LOG_PATH = Path("monitor_log.txt")


def format_duration(seconds):
    if seconds is None:
        return ""
    seconds = int(seconds)
    hours, remainder = divmod(seconds, 3600)
    minutes, secs = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"


def safe_process_info(pid):
    if pid is None or pid == 0:
        return "<sin PID>", None, None
    try:
        proc = psutil.Process(pid)
        name = proc.name()
        create_time = proc.create_time()
        return name, create_time, proc
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        return "<desconocido>", None, None


class ProcessMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Monitor de procesos y conexiones")
        self.sort_column = "pid"
        self.sort_reverse = False
        self.current_rows = []

        self.create_widgets()
        self.ensure_log_file()
        self.log_event("Inicio del monitor de procesos")
        self.refresh_data()

    def create_widgets(self):
        frame = ttk.Frame(self.root, padding=12)
        frame.pack(fill=tk.BOTH, expand=True)

        control_frame = ttk.Frame(frame)
        control_frame.pack(fill=tk.X, pady=(0, 8))

        ttk.Label(control_frame, text="Ordenar por:").pack(side=tk.LEFT)
        self.sort_var = tk.StringVar(value="pid")
        choices = ["pid", "name", "connection_time"]
        self.sort_menu = ttk.OptionMenu(
            control_frame,
            self.sort_var,
            self.sort_var.get(),
            *choices,
            command=self.change_sort
        )
        self.sort_menu.pack(side=tk.LEFT, padx=(8, 16))

        self.log_button = ttk.Button(control_frame, text="Guardar reporte", command=self.save_report)
        self.log_button.pack(side=tk.RIGHT)

        self.tree = ttk.Treeview(
            frame,
            columns=("pid", "name", "local_address", "local_port", "remote_address", "status", "connection_time"),
            show="headings",
            selectmode="browse"
        )

        headings = {
            "pid": "PID",
            "name": "Nombre del proceso",
            "local_address": "Dirección local",
            "local_port": "Puerto local",
            "remote_address": "Dirección remota",
            "status": "Estado",
            "connection_time": "Tiempo de enlace"
        }

        for col, title in headings.items():
            self.tree.heading(col, text=title, command=lambda c=col: self.change_sort(c))
            self.tree.column(col, anchor=tk.W, width=130)

        self.tree.column("name", width=180)
        self.tree.column("local_address", width=150)
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.status_label = ttk.Label(frame, text="Cargando datos...")
        self.status_label.pack(fill=tk.X, pady=(8, 0))

    def ensure_log_file(self):
        if not LOG_PATH.exists():
            LOG_PATH.write_text("Monitor de procesos iniciado\n", encoding="utf-8")

    def log_event(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with LOG_PATH.open("a", encoding="utf-8") as log_file:
            log_file.write(f"[{timestamp}] {message}\n")

    def change_sort(self, value):
        if self.sort_column == value:
            self.sort_reverse = not self.sort_reverse
        else:
            self.sort_column = value
            self.sort_reverse = False
        self.sort_var.set(value)
        self.log_event(f"Cambio de orden: {value} (reverse={self.sort_reverse})")
        self.populate_tree(self.current_rows)

    def get_connection_data(self):
        result = []
        now = datetime.now().timestamp()

        try:
            connections = psutil.net_connections(kind="inet")
        except (psutil.AccessDenied, psutil.NoSuchProcess) as exc:
            messagebox.showwarning(
                "Acceso denegado",
                "No se pudieron obtener todas las conexiones. Ejecuta como administrador/root para ver más detalles."
            )
            connections = []

        for conn in connections:
            if not conn.laddr:
                continue

            pid = conn.pid or 0
            name, create_time, _ = safe_process_info(pid)
            local_address = conn.laddr.ip
            local_port = conn.laddr.port
            remote_address = "" if not conn.raddr else f"{conn.raddr.ip}:{conn.raddr.port}"
            status = conn.status
            connection_time = ""
            if create_time is not None:
                connection_age = now - create_time
                connection_time = format_duration(connection_age)

            result.append({
                "pid": pid,
                "name": name,
                "local_address": local_address,
                "local_port": local_port,
                "remote_address": remote_address,
                "status": status,
                "connection_time": connection_time,
                "sort_pid": pid,
                "sort_name": name.lower(),
                "sort_connection_time": float(connection_time.replace(':', '')) if connection_time else 0,
            })

        return result

    def populate_tree(self, rows):
        self.tree.delete(*self.tree.get_children())

        if self.sort_column in {"pid", "name", "connection_time"}:
            rows.sort(
                key=lambda item: item[f"sort_{self.sort_column}"],
                reverse=self.sort_reverse
            )

        for row in rows:
            self.tree.insert(
                "",
                tk.END,
                values=(
                    row["pid"],
                    row["name"],
                    row["local_address"],
                    row["local_port"],
                    row["remote_address"],
                    row["status"],
                    row["connection_time"],
                )
            )

        self.current_rows = rows
        self.status_label.config(text=f"Conexiones mostradas: {len(rows)} | Ordenado por: {self.sort_column}")
        self.log_event(f"Actualización de datos: {len(rows)} entradas mostradas")

    def refresh_data(self):
        rows = self.get_connection_data()
        self.populate_tree(rows)
        self.root.after(3000, self.refresh_data)

    def save_report(self):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"reporte_conexiones_{timestamp}.txt"
        path = Path(filename)

        with path.open("w", encoding="utf-8") as file:
            file.write("Reporte de conexiones de red\n")
            file.write(f"Fecha y hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write(f"Ordenado por: {self.sort_column}\n")
            file.write("\n")
            file.write("PID\tNombre\tDireccion local\tPuerto local\tDireccion remota\tEstado\tTiempo de enlace\n")
            for row in self.current_rows:
                file.write(
                    f"{row['pid']}\t{row['name']}\t{row['local_address']}\t{row['local_port']}\t{row['remote_address']}\t{row['status']}\t{row['connection_time']}\n"
                )

        self.log_event(f"Reporte guardado: {filename}")
        messagebox.showinfo("Reporte guardado", f"Reporte exportado a {filename}")


if __name__ == "__main__":
    root = tk.Tk()
    app = ProcessMonitorApp(root)
    root.geometry("1100x580")
    root.mainloop()
