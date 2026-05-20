# Reporte Técnico: Monitor de Procesos y Conexiones de Red

**Fecha de elaboración:** 20 de mayo de 2026  
**Asignatura:** Sistemas Operativos  
**Problema:** 2

---

## 1. Introducción

El presente reporte documenta la implementación de una aplicación de monitoreo de procesos y conexiones de red desarrollada en Python. La herramienta permite el seguimiento en tiempo real de los procedimientos ejecutándose en el sistema operativo, visualizando información detallada sobre sus conexiones de red establecidas. Este tipo de aplicaciones resulta fundamental en la administración de sistemas, auditoría de seguridad y análisis de rendimiento.

---

## 2. Objetivos

### 2.1 Objetivo General
Desarrollar una aplicación que realice el seguimiento en tiempo real de procesos y sus conexiones de red, permitiendo visualización, ordenamiento y generación de reportes.

### 2.2 Objetivos Específicos
- Capturar información de procesos activos mediante la interfaz de sistema operativo.
- Extraer datos de conexiones de red asociadas a cada proceso (puertos, direcciones locales y remotas).
- Implementar una interfaz gráfica interactiva con capacidades de filtrado y ordenamiento.
- Generar registros (logs) de actividad y reportes exportables en formato texto.

---

## 3. Marco Teórico

### 3.1 Conceptos Fundamentales

**Proceso (Process):** Instancia en ejecución de un programa, identificado por un número único denominado PID (Process Identifier). Cada proceso posee su propia tabla de descriptores de archivo, espacios de memoria y contexto de ejecución.

**Conexión de Red:** Comunicación establecida entre dos puntos finales (endpoints) a través de protocolos de transporte como TCP o UDP. Cada conexión se caracteriza por direcciones IP, puertos, y estado de la conexión.

**NTP vs Monitoreo Local:** Mientras que investigaciones anteriores abordaron el puerto UDP 123 (NTP), este problema se enfoca en el monitoreo local de toda la actividad de red del sistema.

### 3.2 Herramientas Utilizadas

**psutil:** Librería de Python que proporciona interfaz multiplataforma para recuperar información sobre procesos y utilización del sistema.

**tkinter:** Toolkit estándar de Python para construcción de interfaces gráficas (GUI) con componentes nativos del sistema operativo.

---

## 4. Diseño e Implementación

### 4.1 Arquitectura General

La aplicación está estructurada en torno a una clase principal `ProcessMonitorApp` que gestiona:
- Captura de datos de conexiones de red
- Actualización automática cada 3 segundos
- Presentación en componente Treeview (tabla jerárquica)
- Ordenamiento dinámico por múltiples criterios
- Persistencia de eventos en archivo de log

### 4.2 Código Fuente Completo

```python
import psutil
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import datetime
from pathlib import Path

LOG_PATH = Path("monitor_log.txt")


def format_duration(seconds):
    """
    Convierte segundos a formato HH:MM:SS para mejor legibilidad.
    
    Args:
        seconds: Número de segundos (puede ser None)
    
    Returns:
        String en formato HH:MM:SS o cadena vacía si seconds es None
    """
    if seconds is None:
        return ""
    seconds = int(seconds)
    hours, remainder = divmod(seconds, 3600)
    minutes, secs = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"


def safe_process_info(pid):
    """
    Obtiene información segura de un proceso sin generar excepciones.
    
    Args:
        pid: Process ID
    
    Returns:
        Tupla (nombre_proceso, tiempo_creacion, objeto_proceso)
    """
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
    """
    Aplicación principal de monitoreo de procesos y conexiones de red.
    
    Atributos:
        root: Ventana principal de tkinter
        sort_column: Columna actual de ordenamiento
        sort_reverse: Booleano para ordenamiento inverso
        current_rows: Lista de filas actualmente mostradas
    """
    
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
        """Construye todos los componentes de la interfaz gráfica."""
        frame = ttk.Frame(self.root, padding=12)
        frame.pack(fill=tk.BOTH, expand=True)

        # Marco de control con selector de ordenamiento
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

        # Tabla (Treeview) para mostrar conexiones
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
        """Crea archivo de log si no existe."""
        if not LOG_PATH.exists():
            LOG_PATH.write_text("Monitor de procesos iniciado\n", encoding="utf-8")

    def log_event(self, message):
        """
        Registra un evento con timestamp en el archivo de log.
        
        Args:
            message: Mensaje a registrar
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with LOG_PATH.open("a", encoding="utf-8") as log_file:
            log_file.write(f"[{timestamp}] {message}\n")

    def change_sort(self, value):
        """
        Cambia el criterio de ordenamiento.
        
        Args:
            value: Nuevos criterio de ordenamiento (pid, name, connection_time)
        """
        if self.sort_column == value:
            self.sort_reverse = not self.sort_reverse
        else:
            self.sort_column = value
            self.sort_reverse = False
        self.sort_var.set(value)
        self.log_event(f"Cambio de orden: {value} (reverse={self.sort_reverse})")
        self.populate_tree(self.current_rows)

    def get_connection_data(self):
        """
        Obtiene datos actuales de conexiones de red del sistema.
        
        Returns:
            Lista de diccionarios con información de conexiones
        """
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
        """
        Actualiza la tabla con los datos proporcionados, aplicando ordenamiento.
        
        Args:
            rows: Lista de diccionarios con datos de conexiones
        """
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
        """
        Actualiza datos automáticamente cada 3 segundos utilizando el scheduler de tkinter.
        """
        rows = self.get_connection_data()
        self.populate_tree(rows)
        self.root.after(3000, self.refresh_data)

    def save_report(self):
        """
        Exporta el reporte actual a un archivo de texto con timestamp.
        """
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
```

---

## 5. Funcionalidades Implementadas

| Funcionalidad | Descripción |
|---|---|
| **Monitoreo en tiempo real** | Actualización automática de conexiones cada 3 segundos |
| **Captura de PID** | Identificador único del proceso (Process ID) |
| **Nombre del proceso** | Nombre ejecutable del programa |
| **Dirección local** | Interfaz de red local (IP) |
| **Puerto local** | Puerto de escucha/origen del proceso |
| **Dirección remota** | Endpoint remoto conectado (IP:Puerto) |
| **Estado de conexión** | Estado de la conexión (ESTABLISHED, LISTEN, etc.) |
| **Ordenamiento dinámico** | Posibilidad de ordenar por PID, nombre o tiempo de enlace |
| **Sistema de logs** | Registro persistente de eventos en `monitor_log.txt` |
| **Exportación de reportes** | Generación de reportes timestamped en formato texto |

---

## 6. Dependencias y Requisitos

- **Python 3.7 o superior**
- **psutil**: Librería de interfaz a procesos del SO
- **tkinter**: Incluida por defecto en Python

### 6.1 Instalación de dependencias

```bash
pip install psutil
```

---

## 7. Instrucciones de Uso

1. **Instalación:**
   ```bash
   pip install psutil
   ```

2. **Ejecución:**
   ```bash
   python3 main.py
   ```

3. **Operación:**
   - Visualizar lista de conexiones activas en tiempo real
   - Seleccionar criterio de ordenamiento: PID, nombre o tiempo de enlace
   - Hacer clic en encabezados de columna para invertir orden ascendente/descendente
   - Pulsar "Guardar reporte" para exportar vista actual

---

## 8. Consideraciones Técnicas

### 8.1 Permisos
En sistemas Unix/Linux, se recomienda ejecutar con permisos elevados para visualizar todas las conexiones:
```bash
sudo python3 main.py
```

### 8.2 Rendimiento
- Refrescamiento cada 3 segundos proporciona equilibrio entre precisión y consumo de recursos
- Interfaz responsiva incluso con centenares de conexiones activas

### 8.3 Manejo de Excepciones
El código implementa control robusto de excepciones para procesos que:
- Ya no existen (NoSuchProcess)
- Requieren permisos elevados (AccessDenied)
- Son zombies (ZombieProcess)

---

## 9. Resultados y Observaciones

Se ha desarrollado exitosamente una aplicación de monitoreo que cumple con todos los requisitos especificados:

✓ Seguimiento de procesos y conexiones de red  
✓ Visualización de PID, nombre, direcciones y puertos  
✓ Ordenamiento múltiple (PID, nombre, tiempo de enlace)  
✓ Sistema de logging persistente  
✓ Generación de reportes exportables  
✓ Interfaz gráfica funcional y responsiva  

---

## 10. Conclusiones

La herramienta desarrollada proporciona una solución práctica y escalable para el monitoreo de procesos y actividad de red en sistemas operativos modernos. La arquitectura modular permite futuras extensiones como filtrado avanzado, alertas automáticas o integración con sistemas de análisis.

El uso de bibliotecas estándar (psutil, tkinter) garantiza portabilidad multiplataforma manteniendo compatibilidad con diferentes distribuciones de Linux, macOS y Windows.

---

