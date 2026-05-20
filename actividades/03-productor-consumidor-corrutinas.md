# Actividad 03 — Productor y Consumidor con Corrutinas

**Fechas:** 4-11 marzo 2026

## Descripción
Simulación del patrón productor-consumidor usando `asyncio`, con cola compartida y mecanismos de sincronización.

## Requisitos
- Usar `asyncio` y `asyncio.Queue`.
- Implementar productores y consumidores asíncronos.
- Usar locks para proteger secciones críticas si aplica.
- Mostrar salida con colores para distinguir actores.

## Código de ejemplo (al final del documento):

```python
# productor_consumidor_async.py
import asyncio
import random
from colorama import Fore, Style

async def productor(q, id):
    for i in range(10):
        item = f"item-{id}-{i}"
        await q.put(item)
        print(Fore.GREEN + f"[P{id}] producido: {item}" + Style.RESET_ALL)
        await asyncio.sleep(random.random())

async def consumidor(q, id):
    while True:
        item = await q.get()
        print(Fore.BLUE + f"[C{id}] consumido: {item}" + Style.RESET_ALL)
        q.task_done()
        await asyncio.sleep(random.random())

async def main():
    q = asyncio.Queue()
    producers = [asyncio.create_task(productor(q, i)) for i in range(2)]
    consumers = [asyncio.create_task(consumidor(q, i)) for i in range(2)]

    await asyncio.gather(*producers)
    await q.join()
    for c in consumers:
        c.cancel()

if __name__ == '__main__':
    asyncio.run(main())
```

## Entregables
- `productor_consumidor_async.py`
- Documentación breve sobre el uso de locks y comportamiento observado.

---
*Fin actividad 03.*
