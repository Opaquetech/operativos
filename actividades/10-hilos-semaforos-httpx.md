# Actividad 10 — Hilos con Semáforos (httpx)

**Fechas:** 22-24 abril 2026

## Descripción
Explorar URLs concurrentemente usando `httpx` y controlar concurrencia con semáforos de `asyncio`.

## Requisitos
- Leer `URLs.txt`
- Usar `httpx` asincrónico
- Controlar concurrencia con `asyncio.Semaphore`
- Generar resumen con status y tiempos

## Código de ejemplo (al final de este documento):

```python
import asyncio
import httpx

async def fetch(url, sem):
    async with sem:
        async with httpx.AsyncClient() as client:
            r = await client.get(url, timeout=10.0)
            return url, r.status_code, r.elapsed.total_seconds()

async def main():
    sem = asyncio.Semaphore(5)
    urls = open('URLs.txt').read().splitlines()
    tasks = [fetch(u, sem) for u in urls]
    results = await asyncio.gather(*tasks)
    for r in results:
        print(r)

if __name__ == '__main__':
    asyncio.run(main())
```

## Entregables
- `explorar_urls_httpx.py`
- Reporte de resultados

---
*Fin actividad 10.*
