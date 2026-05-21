#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Actividad 15: Monitor de Procesos y Conexiones en Tiempo Real
Autor: [Tu nombre]
Fecha: 20 de mayo de 2026

Descripción:
    Herramienta gráfica que monitorea procesos del sistema y sus conexiones de red
    en tiempo real. Permite filtrar, ordenar y exportar reportes en CSV.

Requisitos:
    - Python 3.6+
    - psutil
    - tkinter (incluido en Python)

Uso:
    python3 15-monitor-processes.py
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import psutil
import csv
from datetime import datetime
import os
import threading
import logging

# Configurar logging
logging.basicConfig(
    filename='monitor_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def format_size(bytes_value):
    """Convertir bytes a formato legible."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes_value < 1024:
            return f"{bytes_value:.1f} {unit}"
        bytes_value /= 1024
    return f"{bytes_value:.1f} TB"

def safe_process_info(pid):
    """Obtener información segura de un proceso."""
    try:
        proc = psutil.Process(pid)
        return {
            'pid': pid,
            'name': proc.name(),
            'status': proc.status(),
            'memory': proc.memory_info().rss
        }
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        return None

class ProcessMonitorApp:
    """Aplicación de monitoreo de procesos en Tkinter."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Monitor de Procesos y Conexiones")
        self.root.geometry("1200x600")
        
        self.data = []
        self.current_sort_col = None
        self.reverse_sort = False
        
        # Crear GUI
        self.create_widgets()
        
        # Iniciar refresco de datos
        logging.info("Iniciando aplicación de monitoreo")
        self.refresh_data()
    
    def create_widgets(self):
        """Crear componentes de la interfaz."""
        
        # Frame superior: controles
        top_frame = ttk.Frame(self.root)
        top_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        
        # Búsqueda
        ttk.Label(top_frame, text="Filtrar por nombre/PID:").pack(side=tk.LEFT, padx=5)
        self.search_var = tk.StringVar()
        self.search_entry = ttk.Entry(top_frame, textvariable=self.search_var, width=30)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        self.search_entry.bind('<KeyRelease>', lambda e: self.apply_filter())
        
        # Botones
        ttk.Button(top_frame, text="Exportar CSV", command=self.export_csv).pack(side=tk.LEFT, padx=5)
        ttk.Button(top_frame, text="Actualizar", command=self.manual_refresh).pack(side=tk.LEFT, padx=5)
        ttk.Button(top_frame, text="Limpiar Log", command=self.clear_log).pack(side=tk.LEFT, padx=5)
        
        # Frame medio: tabla
        table_frame = ttk.Frame(self.root)
        table_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Crear Treeview con scrollbars
        scrollbar_y = ttk.Scrollbar(table_frame)
        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        
        scrollbar_x = ttk.Scrollbar(table_frame, orient=tk.HORIZONTAL)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.tree = ttk.Treeview(
            table_frame,
            columns=('PID', 'Nombre', 'Dir_Local', 'Pto_Local', 'Dir_Remota', 'Pto_Remota', 'Estado', 'Mem'),
            show='headings',
            yscrollcommand=scrollbar_y.set,
            xscrollcommand=scrollbar_x.set,
            height=20
        )
        
        scrollbar_y.config(command=self.tree.yview)
        scrollbar_x.config(command=self.tree.xview)
        
        # Definir columnas
        columns = {
            'PID': 60,
            'Nombre': 120,
            'Dir_Local': 120,
            'Pto_Local': 80,
            'Dir_Remota': 120,
            'Pto_Remota': 80,
            'Estado': 100,
            'Mem': 80
        }
        
        for col, width in columns.items():
            self.tree.column(col, width=width, anchor=tk.CENTER)
            self.tree.heading(col, text=col, command=lambda c=col: self.sort_by_column(c))
        
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        # Frame inferior: estado
        bottom_frame = ttk.Frame(self.root)
        bottom_frame.pack(fill=tk.X, padx=5, pady=5)
        
        self.status_label = ttk.Label(bottom_frame, text="Inicializando...", relief=tk.SUNKEN)
        self.status_label.pack(fill=tk.X)
    
    def get_connections_data(self):
        """Obtener datos de conexiones de red."""
        data = []
        try:
            for conn in psutil.net_connections(kind='inet'):
                if conn.pid is None:
                    continue
                
                proc_info = safe_process_info(conn.pid)
                if not proc_info:
                    continue
                
                local_ip = conn.laddr.ip if conn.laddr else ""
                local_port = conn.laddr.port if conn.laddr else "-"
                remote_ip = conn.raddr.ip if conn.raddr else "-"
                remote_port = conn.raddr.port if conn.raddr else "-"
                
                data.append({
                    'pid': proc_info['pid'],
                    'name': proc_info['name'],
                    'local_ip': local_ip,
                    'local_port': str(local_port),
                    'remote_ip': remote_ip,
                    'remote_port': str(remote_port),
                    'status': conn.status,
                    'memory': proc_info['memory']
                })
        except (psutil.AccessDenied, psutil.Error) as e:
            logging.warning(f"Error al obtener conexiones: {e}")
        
        return data
    
    def refresh_data(self):
        """Actualizar datos en tiempo real."""
        self.data = self.get_connections_data()
        self.display_data(self.data)
        
        # Actualizar estado
        count = len(self.data)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.status_label.config(text=f"Conexiones: {count} | Última actualización: {timestamp}")
        
        # Programar siguiente actualización (2 segundos)
        self.root.after(2000, self.refresh_data)
    
    def manual_refresh(self):
        """Actualizar manualmente."""
        self.refresh_data()
        messagebox.showinfo("Actualización", "Datos actualizados manualmente")
    
    def display_data(self, data):
        """Mostrar datos en la tabla."""
        # Limpiar tabla
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Insertar datos
        for row in data:
            values = (
                row['pid'],
                row['name'],
                row['local_ip'],
                row['local_port'],
                row['remote_ip'],
                row['remote_port'],
                row['status'],
                format_size(row['memory'])
            )
            self.tree.insert('', tk.END, values=values)
    
    def apply_filter(self):
        """Filtrar tabla por búsqueda."""
        search_text = self.search_var.get().lower()
        
        if not search_text:
            self.display_data(self.data)
            return
        
        filtered = [row for row in self.data if search_text in str(row['pid']).lower() or search_text in row['name'].lower()]
        self.display_data(filtered)
    
    def sort_by_column(self, col):
        """Ordenar tabla por columna."""
        if self.current_sort_col == col:
            self.reverse_sort = not self.reverse_sort
        else:
            self.current_sort_col = col
            self.reverse_sort = False
        
        # Mapa de columnas a claves de datos
        column_map = {
            'PID': 'pid',
            'Nombre': 'name',
            'Dir_Local': 'local_ip',
            'Pto_Local': 'local_port',
            'Dir_Remota': 'remote_ip',
            'Pto_Remota': 'remote_port',
            'Estado': 'status',
            'Mem': 'memory'
        }
        
        key = column_map.get(col, 'pid')
        
        # Ordenar (convertir a número si es posible)
        def sort_key(x):
            val = x.get(key, '')
            if isinstance(val, int):
                return val
            try:
                return int(val)
            except:
                return str(val).lower()
        
        sorted_data = sorted(self.data, key=sort_key, reverse=self.reverse_sort)
        self.display_data(sorted_data)
    
    def export_csv(self):
        """Exportar datos a CSV."""
        if not self.data:
            messagebox.showwarning("Advertencia", "No hay datos para exportar")
            return
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"reporte_conexiones_{timestamp}.csv"
        
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(
                    f,
                    fieldnames=['Timestamp', 'PID', 'Nombre', 'Dir_Local', 'Pto_Local', 'Dir_Remota', 'Pto_Remota', 'Estado', 'Memoria']
                )
                writer.writeheader()
                
                for row in self.data:
                    writer.writerow({
                        'Timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        'PID': row['pid'],
                        'Nombre': row['name'],
                        'Dir_Local': row['local_ip'],
                        'Pto_Local': row['local_port'],
                        'Dir_Remota': row['remote_ip'],
                        'Pto_Remota': row['remote_port'],
                        'Estado': row['status'],
                        'Memoria': format_size(row['memory'])
                    })
            
            logging.info(f"Reporte exportado a {filename}")
            messagebox.showinfo("Éxito", f"Reporte exportado a:\n{filename}")
        
        except Exception as e:
            logging.error(f"Error al exportar CSV: {e}")
            messagebox.showerror("Error", f"No se pudo exportar:\n{e}")
    
    def clear_log(self):
        """Limpiar archivo de log."""
        try:
            open('monitor_log.txt', 'w').close()
            messagebox.showinfo("Log", "Archivo de log limpiado")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo limpiar el log:\n{e}")

def main():
    root = tk.Tk()
    app = ProcessMonitorApp(root)
    logging.info("Aplicación iniciada correctamente")
    root.mainloop()

if __name__ == '__main__':
    main()
