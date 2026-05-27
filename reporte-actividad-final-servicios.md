# Informe: Gestor de Servicios (Interfaz gráfica, Debian/Ubuntu)

**Autor:** [Tu nombre]

**Actividad:** Interfaz gráfica para gestión de servicios systemd (Actividad final)

---

## Resumen

Se desarrolló una aplicación en Python con `tkinter` que permite gestionar servicios `systemd` en sistemas Debian/Ubuntu. El programa lista los servicios, muestra detalles, permite iniciar, detener, reiniciar, recargar, habilitar, deshabilitar y editar el archivo de unidad del servicio de forma segura (remontando la partición si es necesario). Se genera un log de operaciones.

## Archivos relevantes

- Código fuente: [actividades/16-services-gui.py](actividades/16-services-gui.py#L1-L400)
- Registro de operaciones: `services_manager.log` (en el directorio donde se ejecuta el script)

## Objetivos

- Mostrar servicios systemd activos y disponibles.
- Permitir operaciones comunes: start, stop, restart, reload, enable, disable.
- Proveer una herramienta para editar el archivo `.service` asociado, manejando particiones montadas en solo-lectura mediante un remount temporal.
- Generar logs de las operaciones realizadas.

## Requisitos

- Debian/Ubuntu (systemd)
- Python 3.6+
- tkinter (normalmente incluido)
- Permisos para ejecutar comandos `systemctl` y operaciones de escritura (uso de `sudo`).

Nota: Para evitar pedir contraseña múltiples veces, se puede configurar sudoers para permitir `systemctl` y `mount` sin contraseña para usuarios de confianza, con `visudo`.

## Instalación y ejecución

1. Abrir terminal en la carpeta del proyecto.
2. Ejecutar:

```bash
python3 actividades/16-services-gui.py
```

Si algunas operaciones requieren `sudo`, el script las invocará y el sistema puede pedir la contraseña.

## Uso (interfaz)

- Seleccionar un servicio en la lista para ver detalles.
- Botones disponibles:
  - **Iniciar**: inicia el servicio (`systemctl start`).
  - **Detener**: detiene el servicio (`systemctl stop`).
  - **Reiniciar**: reinicia el servicio (`systemctl restart`).
  - **Recargar**: recarga la configuración (`systemctl reload`).
  - **Habilitar**: habilita el servicio al arranque (`systemctl enable`).
  - **Deshabilitar**: deshabilita el servicio al arranque (`systemctl disable`).
  - **Editar**: abre un editor simple para modificar el archivo `.service` asociado; realiza un remount temporal a `rw` si la partición está en `ro`, copia los cambios con privilegios y restaura el estado original.
  - **Actualizar**: recarga la lista de servicios.

## Explicación técnica del código

El script principal es [actividades/16-services-gui.py](actividades/16-services-gui.py#L1-L400).

- `ServicesManagerApp`: clase principal que crea la interfaz con `tkinter`, gestiona la tabla de servicios y el panel de detalles.
- `run_command(cmd, use_sudo=False)`: ejecuta comandos subshell con `subprocess.run`. Si `use_sudo=True` antepone `sudo` al comando.
- `load_services()`: lee la salida de `systemctl list-units --type service --all` y complementa con `systemctl is-enabled` para saber si están habilitados.
- Operaciones start/stop/restart/reload/enable/disable: ejecutan `systemctl` con `use_sudo=True` y actualizan la lista.
- `get_fragment_path(service_name)`: obtiene la ruta del archivo de unidad consultando `systemctl show -p FragmentPath`.
- `edit_service()`: muestra una ventana modal con el contenido del archivo `.service` usando `cat` con `sudo`, permite editar y guardar. Para guardar escribe en un fichero temporal y luego copia el temp al destino con `cp` usando `sudo`.
- `remount_if_needed(path, make_rw=True)`: utiliza `findmnt` para determinar el punto de montaje y las opciones; si la partición está montada `ro` y se solicita `make_rw=True`, ejecuta `mount -o remount,rw <mountpoint>` con `sudo`. Si se remonta, devuelve True para que luego sea restaurada a `ro`.

## Manejo seguro de edición y remount

Al editar un archivo de unidad, puede ocurrir que el archivo resida en una partición montada como solo-lectura (por ejemplo, una partición root montada desde un live-ISO o un sistema con restricciones). El flujo implementado es:

1. Determinar la ruta del archivo con `systemctl show -p FragmentPath`.
2. Consultar `findmnt` para obtener punto de montaje y opciones.
3. Si la partición tiene `ro` en sus opciones y el usuario guarda cambios, ejecutar `mount -o remount,rw <mountpoint>` con `sudo`.
4. Copiar el archivo temporal al destino con `sudo cp tmpfile fragment`.
5. Si se realizó un remount, restaurar con `mount -o remount,ro <mountpoint>`.

Advertencia: Remontar particiones del sistema puede ser riesgoso. Asegúrate de comprender el entorno y tener backups antes de modificar archivos críticos.

## Ejemplos de ejecución y salida

- Iniciar la aplicación y detener el servicio `apache2` desde la GUI.
- Editar `/lib/systemd/system/ejemplo.service` y guardar los cambios; verificar en el log:

```
2026-05-27 14:00:00,000 - INFO - Aplicación iniciada
2026-05-27 14:02:12,345 - INFO - Servicio apache2 detenido
2026-05-27 14:05:00,123 - INFO - Archivo /lib/systemd/system/ejemplo.service modificado por GUI
```

## Logs y reportes

- El script escribe eventos y errores en `services_manager.log`.
- Para generar un reporte adicional (por ejemplo CSV) se puede añadir una función que exporte la lista `self.services` a `CSV` junto con marcas de tiempo.

## Limitaciones y seguridad

- Algunas operaciones requieren privilegios elevados (`sudo`). Si el usuario no tiene permisos, el script mostrará errores.
- El remount y edición de servicios puede comprometer la estabilidad si se hacen cambios incorrectos en unidades críticas.
- El script no valida semánticamente el contenido del `.service` antes de sobrescribir.

## Posibles mejoras

- Añadir confirmación con contraseña integrada y cache seguro del sudo.
- Validar la sintaxis del archivo `.service` antes de sobrescribir (por ejemplo, `systemd-analyze verify`).
- Añadir exportación de reportes (CSV/JSON) y programar auditorías periódicas.
- Mejorar la detección de cambios concurrentes y hacer copias de seguridad automáticas antes de sobrescribir.

## Conclusión

Se entregó una interfaz funcional que cumple los requisitos de la actividad final: listar servicios, gestionar su estado, habilitar/deshabilitar y editar archivos de unidad con manejo de particiones solo-lectura. El enfoque prioriza seguridad (remount controlado) y trazabilidad (logs).

---

¿Quieres que añada una función para exportar la lista de servicios a CSV y anexarla al reporte automáticamente?