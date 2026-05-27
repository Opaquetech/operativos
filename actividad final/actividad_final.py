#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Actividad Final: Gestor de Servicios con GUI (Debian/Ubuntu)
Archivo: actividad_final.py
Autor: [Tu nombre]
Fecha: 27 de mayo de 2026

Descripción:
    Interfaz gráfica para gestionar servicios systemd en Debian/Ubuntu.
    Similar a systemctl: listar, iniciar, detener, reiniciar, recargar,
    habilitar, deshabilitar y editar archivos de unidad (.service) con
    manejo seguro de particiones montadas en solo-lectura.

Requisitos:
    - Python 3.6+
    - Debian/Ubuntu (systemd)
    - tkinter
    - sudo (para operaciones privilegiadas)

Uso:
    python3 "actividad final/actividad_final.py"

"""

import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import threading
import logging
from datetime import datetime

# Configurar logging
logging.basicConfig(
    filename='services_manager.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class ServicesManagerApp:
    """Gestor de servicios con interfaz Tkinter."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Actividad Final - Gestor de Servicios Systemd")
        self.root.geometry("1000x700")
        
        self.services = []
        self.current_service = None
        
        self.create_widgets()
        self.load_services()
        
        logging.info("Aplicación iniciada")
    
    def create_widgets(self):
        """Crear componentes de la interfaz."""
        top_frame = ttk.Frame(self.root)
        top_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
        
        ttk.Label(top_frame, text="Actividad Final: Gestor de Servicios", font=("Arial", 14, "bold")).pack(anchor=tk.W)
        
        button_frame = ttk.Frame(top_frame)
        button_frame.pack(side=tk.TOP, fill=tk.X, pady=10)
        
        ttk.Button(button_frame, text="Iniciar", command=self.start_service).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Detener", command=self.stop_service).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Reiniciar", command=self.restart_service).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Recargar", command=self.reload_service).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Habilitar", command=self.enable_service).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Deshabilitar", command=self.disable_service).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Editar", command=self.edit_service).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Actualizar", command=self.reload_services).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Exportar CSV", command=self.export_csv).pack(side=tk.LEFT, padx=5)
        
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        left_frame = ttk.Frame(main_frame)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        ttk.Label(left_frame, text="Servicios:", font=("Arial", 10, "bold")).pack(anchor=tk.W)
        
        scrollbar = ttk.Scrollbar(left_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.tree = ttk.Treeview(
            left_frame,
            columns=('Servicio', 'Estado', 'Habilitado'),
            show='headings',
            yscrollcommand=scrollbar.set,
            height=25
        )
        scrollbar.config(command=self.tree.yview)
        
        self.tree.column('Servicio', width=300, anchor=tk.W)
        self.tree.column('Estado', width=150, anchor=tk.CENTER)
        self.tree.column('Habilitado', width=120, anchor=tk.CENTER)
        
        self.tree.heading('Servicio', text='Servicio')
        self.tree.heading('Estado', text='Estado')
        self.tree.heading('Habilitado', text='Habilitado')
        
        self.tree.bind('<<TreeviewSelect>>', self.on_service_select)
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        right_frame = ttk.LabelFrame(main_frame, text="Detalles del Servicio", padding=10)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, padx=(10, 0), expand=True)
        
        self.detail_text = tk.Text(right_frame, wrap=tk.WORD, height=30, width=40, state=tk.DISABLED)
        self.detail_text.pack(fill=tk.BOTH, expand=True)
        
        bottom_frame = ttk.LabelFrame(self.root, text="Log de Operaciones", padding=10)
        bottom_frame.pack(fill=tk.X, padx=10, pady=10)
        
        self.log_text = tk.Text(bottom_frame, wrap=tk.WORD, height=6, state=tk.DISABLED)
        self.log_text.pack(fill=tk.BOTH, expand=True)
    
    def run_command(self, cmd, use_sudo=False, timeout=15):
        """Ejecutar comando en bash."""
        try:
            if use_sudo:
                cmd = ['sudo'] + cmd
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
            return result.returncode, result.stdout, result.stderr
        except subprocess.TimeoutExpired:
            return 1, "", "Comando expirado (timeout)"
        except Exception as e:
            return 1, "", str(e)
    
    def load_services(self):
        """Cargar lista de servicios desde systemctl."""
        def load_thread():
            try:
                code, out, err = self.run_command(['systemctl', 'list-units', '--type', 'service', '--all', '--plain', '--no-pager'])
                if code != 0:
                    self.append_log(f"Error al obtener servicios: {err}")
                    return
                services = []
                for line in out.strip().split('\n')[1:]:
                    if not line.strip():
                        continue
                    parts = line.split()
                    if len(parts) >= 3:
                        name = parts[0]
                        state = parts[2] if len(parts) > 2 else "unknown"
                        services.append({
                            'name': name,
                            'state': state,
                            'enabled': None
                        })
                for service in services:
                    code, out, err = self.run_command(['systemctl', 'is-enabled', service['name']])
                    service['enabled'] = 'yes' if code == 0 else 'no'
                self.services = services
                self.display_services()
                self.append_log(f"✓ Cargados {len(services)} servicios")
            except Exception as e:
                self.append_log(f"Error: {e}")
                logging.error(f"Error loading services: {e}")
        threading.Thread(target=load_thread, daemon=True).start()
    
    def display_services(self):
        """Mostrar servicios en tabla."""
        for item in self.tree.get_children():
            self.tree.delete(item)
        for service in self.services:
            self.tree.insert('', tk.END, values=(
                service['name'],
                service['state'],
                service['enabled']
            ))
    
    def on_service_select(self, event):
        selection = self.tree.selection()
        if not selection:
            return
        item = selection[0]
        values = self.tree.item(item, 'values')
        service_name = values[0]
        for service in self.services:
            if service['name'] == service_name:
                self.current_service = service
                self.show_service_details(service)
                break
    
    def show_service_details(self, service):
        self.detail_text.config(state=tk.NORMAL)
        self.detail_text.delete('1.0', tk.END)
        details = f"Servicio: {service['name']}\n"
        details += f"Estado: {service['state']}\n"
        details += f"Habilitado: {service['enabled']}\n"
        details += "─" * 40 + "\n"
        code, out, err = self.run_command(['systemctl', 'show', service['name'], '-p', 'Description', '--value'])
        if code == 0:
            details += f"Descripción: {out.strip()}\n"
        code, out, err = self.run_command(['systemctl', 'status', service['name']])
        if code == 0:
            details += "\nEstado Detallado:\n" + out[:500] + "\n..."
        self.detail_text.insert('1.0', details)
        self.detail_text.config(state=tk.DISABLED)
    
    def get_service_name(self):
        if self.current_service:
            return self.current_service['name']
        messagebox.showwarning("Advertencia", "Selecciona un servicio primero")
        return None
    
    def start_service(self):
        name = self.get_service_name()
        if not name:
            return
        self.append_log(f"Iniciando {name}...")
        code, out, err = self.run_command(['systemctl', 'start', name], use_sudo=True)
        if code == 0:
            self.append_log(f"✓ {name} iniciado")
            logging.info(f"Servicio {name} iniciado")
        else:
            self.append_log(f"✗ Error al iniciar {name}: {err}")
            logging.error(f"Error starting {name}: {err}")
        self.reload_services()
    
    def stop_service(self):
        name = self.get_service_name()
        if not name:
            return
        if not messagebox.askyesno("Confirmar", f"¿Detener {name}?"):
            return
        self.append_log(f"Deteniendo {name}...")
        code, out, err = self.run_command(['systemctl', 'stop', name], use_sudo=True)
        if code == 0:
            self.append_log(f"✓ {name} detenido")
            logging.info(f"Servicio {name} detenido")
        else:
            self.append_log(f"✗ Error al detener {name}: {err}")
            logging.error(f"Error stopping {name}: {err}")
        self.reload_services()
    
    def restart_service(self):
        name = self.get_service_name()
        if not name:
            return
        if not messagebox.askyesno("Confirmar", f"¿Reiniciar {name}?"):
            return
        self.append_log(f"Reiniciando {name}...")
        code, out, err = self.run_command(['systemctl', 'restart', name], use_sudo=True)
        if code == 0:
            self.append_log(f"✓ {name} reiniciado")
            logging.info(f"Servicio {name} reiniciado")
        else:
            self.append_log(f"✗ Error al reiniciar {name}: {err}")
            logging.error(f"Error restarting {name}: {err}")
        self.reload_services()
    
    def reload_service(self):
        name = self.get_service_name()
        if not name:
            return
        self.append_log(f"Recargando {name}...")
        code, out, err = self.run_command(['systemctl', 'reload', name], use_sudo=True)
        if code == 0:
            self.append_log(f"✓ {name} recargado")
            logging.info(f"Servicio {name} recargado")
        else:
            self.append_log(f"✗ Error al recargar {name}: {err}")
            logging.error(f"Error reloading {name}: {err}")
    
    def enable_service(self):
        name = self.get_service_name()
        if not name:
            return
        self.append_log(f"Habilitando {name} en boot...")
        code, out, err = self.run_command(['systemctl', 'enable', name], use_sudo=True)
        if code == 0:
            self.append_log(f"✓ {name} habilitado")
            logging.info(f"Servicio {name} habilitado")
        else:
            self.append_log(f"✗ Error al habilitar {name}: {err}")
            logging.error(f"Error enabling {name}: {err}")
        self.reload_services()
    
    def disable_service(self):
        name = self.get_service_name()
        if not name:
            return
        if not messagebox.askyesno("Confirmar", f"¿Deshabilitar {name} en boot?"):
            return
        self.append_log(f"Deshabilitando {name}...")
        code, out, err = self.run_command(['systemctl', 'disable', name], use_sudo=True)
        if code == 0:
            self.append_log(f"✓ {name} deshabilitado")
            logging.info(f"Servicio {name} deshabilitado")
        else:
            self.append_log(f"✗ Error al deshabilitar {name}: {err}")
            logging.error(f"Error disabling {name}: {err}")
        self.reload_services()

    def get_fragment_path(self, service_name):
        code, out, err = self.run_command(['systemctl', 'show', service_name, '-p', 'FragmentPath', '--value'])
        if code == 0:
            path = out.strip()
            return path if path else None
        return None

    def remount_if_needed(self, path, make_rw=True):
        try:
            code, mp_out, mp_err = self.run_command(['findmnt', '-n', '-o', 'TARGET,OPTIONS', '--target', path])
            if code != 0 or not mp_out.strip():
                return False
            parts = mp_out.strip().split()
            mountpoint = parts[0]
            options = parts[1] if len(parts) > 1 else ''
            if make_rw:
                if 'ro' in options.split(','):
                    code, out, err = self.run_command(['mount', '-o', 'remount,rw', mountpoint], use_sudo=True)
                    return code == 0
                return False
            else:
                code, out, err = self.run_command(['mount', '-o', 'remount,ro', mountpoint], use_sudo=True)
                return code == 0
        except Exception:
            return False

    def edit_service(self):
        name = self.get_service_name()
        if not name:
            return
        frag = self.get_fragment_path(name)
        if not frag:
            messagebox.showinfo("Info", "No se encontró archivo de unidad para este servicio")
            return
        code, out, err = self.run_command(['cat', frag], use_sudo=True)
        content = out if code == 0 else ''
        edit_win = tk.Toplevel(self.root)
        edit_win.title(f"Editar: {frag}")
        edit_win.geometry("800x600")
        txt = tk.Text(edit_win, wrap=tk.NONE)
        txt.insert('1.0', content)
        txt.pack(fill=tk.BOTH, expand=True)
        btn_frame = ttk.Frame(edit_win)
        btn_frame.pack(fill=tk.X)
        def save_and_close():
            new_content = txt.get('1.0', tk.END)
            import tempfile, os
            fd, tmp_path = tempfile.mkstemp(prefix='svc_edit_', text=True)
            os.close(fd)
            with open(tmp_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            remounted = False
            try:
                remounted = self.remount_if_needed(frag, make_rw=True)
                code, out, err = self.run_command(['cp', tmp_path, frag], use_sudo=True)
                if code == 0:
                    self.append_log(f"✓ Archivo {frag} guardado")
                    logging.info(f"Archivo {frag} modificado por GUI")
                    messagebox.showinfo("Guardado", "Archivo guardado correctamente")
                else:
                    self.append_log(f"✗ Error guardando {frag}: {err}")
                    logging.error(f"Error guardando {frag}: {err}")
                    messagebox.showerror("Error", f"No se pudo guardar: {err}")
            finally:
                try:
                    os.remove(tmp_path)
                except Exception:
                    pass
                if remounted:
                    self.remount_if_needed(frag, make_rw=False)
            edit_win.destroy()
        ttk.Button(btn_frame, text="Guardar", command=save_and_close).pack(side=tk.RIGHT, padx=5, pady=5)
        ttk.Button(btn_frame, text="Cancelar", command=edit_win.destroy).pack(side=tk.RIGHT, padx=5, pady=5)

    def reload_services(self):
        self.load_services()

    def append_log(self, message):
        self.log_text.config(state=tk.NORMAL)
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.log_text.insert(tk.END, f"[{timestamp}] {message}\n")
        self.log_text.see(tk.END)
        lines = self.log_text.get('1.0', tk.END).split('\n')
        if len(lines) > 100:
            self.log_text.delete('1.0', '100.0')
        self.log_text.config(state=tk.DISABLED)

    def export_csv(self):
        try:
            import csv
            fname = 'services_report.csv'
            with open(fname, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['timestamp', 'service', 'state', 'enabled'])
                ts = datetime.now().isoformat()
                for s in self.services:
                    writer.writerow([ts, s.get('name'), s.get('state'), s.get('enabled')])
            self.append_log(f"✓ Exportado CSV: {fname}")
            messagebox.showinfo("Exportado", f"CSV guardado: {fname}")
        except Exception as e:
            self.append_log(f"✗ Error exportando CSV: {e}")
            logging.error(f"Error exportando CSV: {e}")

def main():
    root = tk.Tk()
    app = ServicesManagerApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
