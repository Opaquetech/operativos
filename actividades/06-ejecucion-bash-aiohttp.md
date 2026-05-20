# Actividad 06 — Ejecución de Comandos Bash vía aiohttp

**Fechas:** 4-30 marzo 2026

## Descripción
Desarrollar un servicio web con `aiohttp` que reciba solicitudes para ejecutar comandos bash y devuelva la salida.

## Requisitos y consideraciones de seguridad
- Usar `aiohttp` para endpoints HTTP asincrónicos.
- No ejecutar comandos sin validar (usar whitelist o sanitización).
- Registrar cada comando ejecutado en logs.
- Opcional: añadir autenticación básica.

## Ejemplo de servidor (esqueleto, colocar como código al final si se requiere):

```python
# aio_execute.py (resumen)
from aiohttp import web
import asyncio, subprocess

async def execute(request):
    cmd = request.query.get('cmd')
    # validar cmd
    proc = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    out, err = await proc.communicate()
    return web.Response(text=out.decode() + err.decode())

app = web.Application()
app.router.add_get('/execute', execute)
web.run_app(app, port=8080)
```

## Entregables
- `aio_execute.py` con validación y logging
- Documentación de medidas de seguridad

---
*Fin actividad 06.*
