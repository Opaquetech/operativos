# Actividad 15 — Monitoreo de Procesos Activos del Sistema

## Portada

**Proyecto:** Monitoreo en Tiempo Real de Procesos y Conexiones de Red  
**Asignatura:** Sistemas Operativos  
**Fecha:** 20 de mayo de 2026  
**Estudiante:** [Tu nombre]  
**Objetivo:** Crear una herramienta gráfica para supervisar procesos, puertos y conexiones activas en el sistema

---

## 1. Introducción

Los sistemas operativos modernos ejecutan múltiples procesos simultáneamente. Cada proceso consume recursos (CPU, memoria, puertos de red) y establece conexiones para comunicarse. Un administrador de sistemas o desarrollador necesita:

- **Identificar qué procesos corren** en tiempo real
- **Detectar conexiones activas** (qué proceso usa qué puerto)
- **Monitorear actividad de red** para diagnósticos de rendimiento
- **Generar reportes** para auditoría

**Psutil** es una librería Python multiplataforma que expone la API del sistema operativo para acceder a:
- Información de procesos (PID, nombre, usuario, estado)
- Conexiones de red (IPv4, puertos locales/remotos, estado)
- Uso de recursos (CPU, memoria, disco)

**Tkinter** proporciona un GUI nativo para visualizar estos datos en tiempo real.

---

## 2. Conceptos Fundamentales

### 2.1 Procesos y PIDs

Un **proceso** es una instancia en ejecución de un programa. Cada proceso tiene:
- **PID (Process ID):** identificador único
- **PPID:** PID del proceso padre
- **Nombre:** ejecutable asociado
- **Usuario:** propietario del proceso
- **Estado:** running, sleeping, zombie, etc.

### 2.2 Conexiones de Red

Una **conexión de red** es un túnel de comunicación entre dos puntos:
- **Dirección local:** IP:puerto en nuestra máquina
- **Dirección remota:** IP:puerto del otro lado
- **Protocolo:** TCP, UDP
- **Estado:** LISTEN, ESTABLISHED, TIME_WAIT, CLOSE_WAIT, etc.

### 2.3 Psutil: Lectura de Datos del Sistema

```python
import psutil

# Obtener todos los procesos
for proc in psutil.process_iter(['pid', 'name', 'username']):
    print(proc.info)

# Obtener conexiones de red
for conn in psutil.net_connections():
    print(f"PID: {conn.pid}, Local: {conn.laddr}, Remoto: {conn.raddr}, Estado: {conn.status}")
```

### 2.4 Actualización en Tiempo Real sin Bloqueos

En **Tkinter**, el evento loop se bloquea si realizamos operaciones largas. La solución:
- Usar `root.after(ms, función)` para actualizar periódicamente
- O usar threading para recolectar datos en segundo plano

---

## 3. Arquitectura del Programa

```
┌─────────────────────────────────────────────┐
│         ProcessMonitorApp (tkinter GUI)     │
├─────────────────────────────────────────────┤
│  - Ventana principal (root)                 │
│  - Treeview: tabla de procesos/conexiones   │
│  - Botones: Filtrar, Ordenar, Exportar      │
│  - Frame de estado: log en tiempo real      │
├─────────────────────────────────────────────┤
│ Funciones de Recolección:                   │
│  - get_processes()   → lista de procesos    │
│  - get_connections() → conexiones activas   │
│  - format_duration() → tiempo legible        │
│  - safe_process_info() → info del proceso   │
└─────────────────────────────────────────────┘
```

---

## 4. Características Implementadas

### 4.1 Monitoreo en Tiempo Real
- Actualización cada 2 segundos (configurable)
- Tabla con columnas: PID, Nombre, Dirección Local, Puerto Local, Dirección Remota, Puerto Remoto, Estado

### 4.2 Ordenamiento Dinámico
- Click en encabezado de columna para ordenar
- Soporta: PID, nombre, puerto, tiempo

### 4.3 Generación de Reportes
- Exportar snapshot a CSV con timestamp
- Guardar en archivo `reporte_conexiones_<YYYYMMDD_HHMMSS>.csv`
- Incluye metadatos: fecha, hostname, usuario, total de conexiones

### 4.4 Filtrado
- Texto de búsqueda para filtrar por nombre o PID
- Campo de entrada interactivo

### 4.5 Logging
- Archivo `monitor_log.txt` con eventos del programa
- Rotación automática si alcanza cierto tamaño

---

## 5. Flujo de Ejecución

1. **Inicio:** Lee procesos y conexiones del sistema
2. **GUI:** Muestra tabla en Tkinter
3. **Loop:** Cada 2 segundos, actualiza datos
4. **Usuario:**
   - Puede clickear columnas para ordenar
   - Buscar procesos por nombre/PID
   - Exportar reporte a CSV
5. **Log:** Registra acciones en `monitor_log.txt`

---

## 6. Código Fuente Comentado

Ver archivo: `actividades/15-monitor-processes.py`

### Pseudocódigo Principal

```python
class ProcessMonitorApp:
    def __init__(self, root):
        # Inicializar GUI
        # Crear tabla (Treeview)
        # Crear botones
        
    def refresh_data(self):
        # Obtener procesos y conexiones
        # Actualizar tabla
        # Programar siguiente refresh
        
    def export_report(self):
        # Crear CSV con snapshot actual
        # Guardar en disco
        
    def search_filter(self, text):
        # Filtrar tabla por texto
        
    def on_column_click(self, col):
        # Ordenar por columna
```

---

## 7. Resultados de Ejecución

### 7.1 Captura 1: Inicio del programa
```
PID      Nombre          Dirección Local    Puerto Local    Dirección Remota       Puerto Remoto    Estado
1        systemd         127.0.0.1          -               -                      -               -
452      sshd            0.0.0.0            22              -                      -               LISTEN
1234     firefox         127.0.0.1          54321           142.250.80.46          443            ESTABLISHED
1567     python3         0.0.0.0            5000            -                      -               LISTEN
```

### 7.2 Captura 2: Después de búsqueda "python"
```
PID      Nombre          Dirección Local    Puerto Local    Dirección Remota       Puerto Remoto    Estado
1567     python3         0.0.0.0            5000            -                      -               LISTEN
1890     python3         127.0.0.1          54322           93.184.216.34          80              TIME_WAIT
```

### 7.3 Captura 3: Exportación a CSV
```
Archivo: reporte_conexiones_20260520_143022.csv

Timestamp,Hostname,Usuario,PID,Nombre,Dir_Local,Puerto_Local,Dir_Remota,Puerto_Remota,Estado
2026-05-20 14:30:22,mi-pc,user,1,systemd,127.0.0.1,-,-,-,-
2026-05-20 14:30:22,mi-pc,user,452,sshd,0.0.0.0,22,-,-,LISTEN
...
```

---

## 8. Consideraciones Técnicas

### 8.1 Permisos
- En Linux, `psutil.net_connections()` requiere `sudo` para conexiones de otros usuarios
- Ejecutar sin elevación de privilegios muestra solo conexiones del usuario actual

### 8.2 Rendimiento
- Leer 10,000+ conexiones cada 2 segundos puede ser lento
- Solución: filtrar por estado (ej: solo ESTABLISHED)

### 8.3 Multiplataforma
- `psutil` funciona en Windows, macOS, Linux
- Diferentes APIs internas, misma interfaz Python

---

## 9. Mejoras Futuras

1. **Gráficos de CPU/Memoria:** matplotlib en tiempo real
2. **Alertas:** notificación si PID específico consume >90% CPU
3. **Historial:** guardar métricas en BD SQLite
4. **Control remoto:** API REST para monitoreo desde otra máquina
5. **Integración con Prometheus:** exportar métricas para monitoreo empresarial

---

## 10. Conclusiones

Esta herramienta permite **visibilidad completa del sistema** sin línea de comandos. Es útil para:
- Diagnóstico de problemas de rendimiento
- Detección de conexiones sospechosas (seguridad)
- Aprendizaje de administración de sistemas
- Auditoría de aplicaciones

El uso de **psutil + tkinter** demuestra cómo integrar datos del SO con interfaces amigables en Python.

---

## Bibliografía

1. psutil documentation: https://psutil.readthedocs.io/
2. Tkinter official docs: https://docs.python.org/3/library/tkinter.html
3. Linux networking: man pages (netstat, ss, procfs)
4. Windows Process model: MSDN documentation

---

**Anexo: Archivo de Programa**

El código ejecutable se encuentra en: `actividades/15-monitor-processes.py`
