# Actividad 16 — Interfaz Gráfica para Gestión de Servicios (Debian/Ubuntu)

## Portada

**Proyecto:** Gestor Visual de Servicios del Sistema  
**Plataforma:** Debian/Ubuntu Linux  
**Asignatura:** Sistemas Operativos  
**Fecha:** 20 de mayo de 2026  
**Objetivo:** Crear un GUI tipo `systemctl` para controlar servicios sin línea de comandos

---

## 1. Introducción

En sistemas Linux (Debian/Ubuntu), los **servicios** (también llamados *daemons*) son programas que corren en segundo plano. Ejemplos:
- `apache2`: servidor web
- `mysql`: base de datos
- `ssh`: acceso remoto
- `nginx`: proxy/balanceador de carga

Históricamente se usaba `service` o `init.d`, ahora se usa **systemd** con el comando `systemctl`.

### 1.1 ¿Por qué un GUI?

- Administradores de sistemas pueden no estar familiarizados con CLI
- Reduce errores de tipeo
- Proporciona confirmaciones visuales
- Registra acciones para auditoría

### 1.2 Servicios en Debian/Ubuntu

Un servicio se define en un archivo `.service` en `/etc/systemd/system/` o `/lib/systemd/system/`. Ejemplo:

```ini
[Unit]
Description=Apache Web Server
After=network.target

[Service]
Type=forking
ExecStart=/usr/sbin/apachectl start
ExecReload=/usr/sbin/apachectl graceful
ExecStop=/usr/sbin/apachectl stop

[Install]
WantedBy=multi-user.target
```

---

## 2. Conceptos de Systemctl

### 2.1 Estados de un Servicio

- **active (running):** el servicio está en ejecución
- **active (exited):** ejecutó pero terminó normalmente
- **inactive:** no está corriendo
- **failed:** intentó iniciarse pero falló
- **disabled:** no se inicia al boot

### 2.2 Comandos Principales

```bash
systemctl start <service>      # Iniciar
systemctl stop <service>       # Detener
systemctl restart <service>    # Reiniciar
systemctl reload <service>     # Recargar (sin parar)
systemctl enable <service>     # Activar en boot
systemctl disable <service>    # Desactivar en boot
systemctl status <service>     # Ver estado
systemctl list-units --type service  # Listar todos
```

### 2.3 Permisos

- Operaciones normales requieren `sudo` (excepto ver status)
- En GUI, ejecutaremos con `subprocess` y capturaremos salida

---

## 3. Arquitectura del Programa

```
┌────────────────────────────────────────────────┐
│         ServicesManagerApp (tkinter GUI)       │
├────────────────────────────────────────────────┤
│  - Ventana principal                           │
│  - Treeview: lista de servicios con estado     │
│  - Botones: Start, Stop, Restart, Enable...    │
│  - Panel de detalles: información del servicio │
├────────────────────────────────────────────────┤
│ Funciones Backend:                             │
│  - get_all_services() → lista systemctl        │
│  - execute_command() → corre sudo systemctl    │
│  - parse_status() → extrae estado de salida    │
│  - mount_remount() → manejo de particiones     │
└────────────────────────────────────────────────┘
```

---

## 4. Características Implementadas

### 4.1 Listado de Servicios
- Obtiene todos los servicios con `systemctl list-units --type service`
- Muestra: nombre, estado (active/inactive), descripción

### 4.2 Control de Servicios
- **Botones:** Start, Stop, Restart, Reload
- Confirma antes de ejecutar acciones destructivas
- Usa `subprocess` con `sudo`

### 4.3 Habilitación en Boot
- **Enable:** servicio inicia automáticamente al arranque
- **Disable:** no inicia automáticamente

### 4.4 Panel de Detalles
- Mostrar información completa del servicio
- Ver últimas líneas del log (journal)

### 4.5 Manejo de Particiones (Opcional Avanzado)
- Para servicios en particiones read-only, ofrecer:
  - Remontar partición en read-write
  - Editar/actualizar servicio
  - Remontar en read-only

---

## 5. Procedimiento Técnico: Remontar Partición

En algunos casos, archivos de servicio están en particiones montadas en read-only:

```bash
# 1. Identificar qué partición contiene el archivo
mount | grep /etc/systemd

# 2. Remontar en read-write
sudo mount -o remount,rw /

# 3. Realizar cambios (editar archivo)

# 4. Remontar en read-only
sudo mount -o remount,ro /
```

**Advertencia:** esto es operación avanzada; errores pueden dañar el sistema.

---

## 6. Flujo de Uso

1. **Inicio:** Carga lista de servicios con estado actual
2. **Usuario selecciona servicio:** Se muestra detalles en panel derecho
3. **Usuario clickea botón:** (ej "Start")
4. **Programa:**
   - Pide confirmación (si es destructivo)
   - Ejecuta `sudo systemctl start <service>`
   - Captura salida/errores
   - Actualiza UI con nuevo estado
5. **Log:** Registra todas las acciones en `services_manager.log`

---

## 7. Código Comentado

Ver archivo: `actividades/16-services-gui.py`

### Pseudocódigo Principal

```python
class ServicesManagerApp:
    def __init__(self, root):
        self.root = root
        self.services = []
        self.create_widgets()
        self.load_services()
    
    def load_services(self):
        # Ejecutar: systemctl list-units --type service
        # Parsear salida
        # Mostrar en tabla
    
    def on_service_selected(self, service):
        # Mostrar detalles en panel derecho
        # Mostrar estado actual
    
    def start_service(self, service):
        # Confirmar
        # Ejecutar: sudo systemctl start <service>
        # Actualizar UI
    
    def reload_services(self):
        # Limpiar tabla
        # Recargar desde systemctl
```

---

## 8. Ejemplo de Ejecución

### Pantalla Inicial
```
Servicios Activos:
┌────────────────────────────────────────────────────────────┐
│ Nombre           │ Estado        │ Descripción              │
├────────────────────────────────────────────────────────────┤
│ apache2          │ active        │ Apache Web Server        │
│ ssh              │ active        │ OpenBSD Secure Shell    │
│ mysql            │ inactive      │ MySQL Database          │
│ nginx            │ failed        │ NGINX HTTP Server       │
└────────────────────────────────────────────────────────────┘

[Botones: Start | Stop | Restart | Reload | Enable | Disable | Actualizar]
```

### Después de Seleccionar `apache2` e Iniciar
```
Detalles:
Nombre: apache2
Estado: active (running)
Descripción: Apache HTTP Server
Habilitado en boot: yes

Últimas líneas del log:
2026-05-20 14:35:22 apache2[5421]: [mpm_prefork:notice] AH00163: Apache/2.4.41 started
2026-05-20 14:35:22 systemd[1]: Started Apache Web Server.

[Log de operaciones]
14:35:10 - Iniciando apache2...
14:35:12 - apache2 iniciado exitosamente ✓
```

---

## 9. Consideraciones de Seguridad

### 9.1 Permisos
- Usar `sudo` para cambios de estado
- Pedir contraseña (se cachea en sudoers)
- Validar entrada (no inyección de comandos)

### 9.2 Validación
- Verificar que el nombre del servicio es válido
- No permitir caracteres especiales
- Confirmar comandos destructivos (stop, restart)

### 9.3 Auditoría
- Registrar todas las acciones en log
- Incluir timestamp y usuario
- Guardar salida/error de cada comando

---

## 10. Mejoras Futuras

1. **Búsqueda y filtrado** de servicios
2. **Edición de archivos .service** en GUI
3. **Gráfico de uso de recursos** por servicio
4. **Alertas** si un servicio falla
5. **Control remoto** (SSH a otro servidor)

---

## 11. Conclusiones

El gestor visual de servicios simplifica administración del sistema. Beneficios:

- **Facilidad de uso:** usuarios no necesitan terminal
- **Seguridad:** confirmaciones previenen errores críticos
- **Auditoría:** registro completo de cambios
- **Mantenibilidad:** fácil para nuevos administradores

La integración de `systemctl` con `tkinter` demuestra cómo automatizar tareas administrativas en Python.

---

## Bibliografía

1. Systemd official documentation: https://systemd.io/
2. Debian Administrator's Handbook: Chapter 9 (Services)
3. Ubuntu man pages: `man systemctl`, `man systemd.service`
4. Red Hat System Administrator's Guide: Managing Services

---

**Anexo: Archivo de Programa**

El código ejecutable se encuentra en: `actividades/16-services-gui.py`
