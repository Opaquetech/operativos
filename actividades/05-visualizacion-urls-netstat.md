# Actividad 05 — Visualización de URLs en Tiempo Real (netstat)

**Fechas:** 4-23 marzo 2026

## Descripción
Extraer y visualizar URLs/dominios conectados desde la máquina en tiempo real usando `netstat`, resolviendo IPs a nombres cuando sea posible y validando frente a blacklists.

## Requisitos
- Capturar conexiones en tiempo real con `netstat`.
- Extraer endpoints remotos y resolver a dominios con `socket.gethostbyaddr` cuando sea posible.
- Validar URLs/dominios contra listas negras (p. ej. URLhaus, PhishTank).
- Interfaz gráfica con `tkinter` y resaltado.

## Notas técnicas
- Resolución inversa puede ser lenta; hacer en un hilo o task separado.
- Mantener caché de resoluciones para rendimiento.

## Entregables
- `netstat_urls_monitor.py` (opcional)
- Reporte con ejemplos y capturas

---
*Fin actividad 05.*
