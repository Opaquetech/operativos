# Actividad 04 — Visualización de IPv4 en Tiempo Real (netstat)

**Fechas:** 4-15 marzo 2026

## Descripción
Leer en tiempo real las direcciones IPv4 enlazadas a la máquina usando `netstat` y mostrar una interfaz con `tkinter` resaltando IPs inválidas o sospechosas.

## Requisitos
- Capturar salida de `netstat` periódicamente.
- Parsear las direcciones IPv4 locales y remotas.
- Validar formato de IP con `ipaddress`.
- Interfaz gráfica con actualización dinámica.

## Ejemplo de enfoque
1. Usar `subprocess.check_output(['netstat', '-nt'])` para capturar conexiones TCP.
2. Parsear líneas y extraer `local_address` y `remote_address`.
3. Validar IP con `ipaddress.ip_address()` y marcar en rojo si inválida.

## Código de ejemplo (resumen, al final si aplica):

```python
# netstat_ipv4_monitor.py (resumen)
import subprocess
import ipaddress

out = subprocess.check_output(['netstat','-nt']).decode()
for line in out.splitlines()[2:]:
    parts = line.split()
    local = parts[3]
    remote = parts[4]
    # parsear IP:puerto y validar
```

## Entregables
- `netstat_ipv4_monitor.py` (opcional)
- Informe con capturas y explicación

---
*Fin actividad 04.*
