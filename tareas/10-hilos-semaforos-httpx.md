# Tarea 10: Hilos con Semáforos (httpx)

**Fechas:** 22 de abril de 2026 - 24 de abril de 2026

---

## Descripción

Programa en Python que lee una lista de URLs desde un archivo, las explora de forma concurrente usando httpx, y controla la concurrencia mediante semáforos de asyncio.

---

## Requisitos del Programa

### Funcionalidades:
1. **Lectura de URLs:**
   - Obtener lista de URLs desde archivo (URLs.txt)
   - Una URL por línea
   - Validación de URLs

2. **Exploración Concurrente:**
   - Usar librería `httpx` para peticiones HTTP
   - Múltiples peticiones simultáneas
   - Control de concurrencia con semáforos

3. **Control de Concurrencia:**
   - Limitar número simultáneo de conexiones
   - Semáforos de asyncio
   - Evitar sobrecargar el servidor

4. **Reporte de Resultados:**
   - Estado HTTP de cada URL
   - Tiempo de respuesta
   - Errores detectados
   - Resumen final

---

## Especificaciones Técnicas

**Librerías Requeridas:**
- `httpx`: Cliente HTTP asincrónico
- `asyncio`: Programación asincrónica
- `time`: Medición de tiempos

### Instalación:
```bash
pip install httpx
```

---

## Estructura del Archivo de URLs

**URLs.txt:**
```
https://www.google.com
https://github.com
https://www.python.org
https://stackoverflow.com
https://docs.python.org
https://httpx.readthedocs.io
...
```

---

## Implementación de Semáforos

```python
import asyncio
import httpx

# Crear semáforo para limitar conexiones simultáneas
semaphore = asyncio.Semaphore(5)  # Máximo 5 conexiones simultáneas

async def fetch_url(client, url):
    async with semaphore:  # Adquirir semáforo
        try:
            response = await client.get(url, timeout=10.0)
            return url, response.status_code
        except Exception as e:
            return url, f"Error: {str(e)}"
```

---

## Flujo del Programa

```
┌──────────────────┐
│ Leer URLs.txt    │
└────────┬─────────┘
         ↓
┌──────────────────────────────┐
│ Crear lista de URLs válidas  │
└────────┬─────────────────────┘
         ↓
┌──────────────────────────────┐
│ Crear semáforo (5 conexiones)│
└────────┬─────────────────────┘
         ↓
┌──────────────────────────────┐
│ Ejecutar peticiones (async)  │
│ - Respetar semáforo          │
│ - Obtener status code        │
│ - Medir tiempo               │
└────────┬─────────────────────┘
         ↓
┌──────────────────────────────┐
│ Mostrar resultados           │
│ - Status de cada URL         │
│ - Tiempos de respuesta       │
│ - Errores detectados         │
└──────────────────────────────┘
```

---

## Salida Esperada

```
=== Exploración de URLs ===
Archivo: URLs.txt
Semáforo: 5 conexiones máximas
Iniciando...

[1/20] https://google.com         → 200 OK (0.52s)
[2/20] https://github.com         → 200 OK (0.38s)
[3/20] https://python.org         → 301 REDIRECT (0.45s)
[4/20] https://invalid.xyz        → Error: Connection refused

=== Resumen ===
Total URLs: 20
Exitosas: 18
Errores: 2
Tiempo total: 2.45 segundos
```

---

## Evaluación

- [ ] Lectura correcta de archivo URLs.txt
- [ ] Validación de URLs
- [ ] Implementación de semáforos
- [ ] Peticiones asincrónicas funcionando
- [ ] Control de concurrencia correcto
- [ ] Status codes capturados
- [ ] Tiempos medidos correctamente
- [ ] Reporte completo

