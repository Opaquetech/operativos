# Actividad 13 — Primitivas de Sincronización de Procesos

**Fechas:** 29 abril - 4 mayo 2026

## Descripción
Implementar ejemplos demostrativos de primitivas de sincronización: Mutex, Semáforo, Condition, Barrera, Reader-Writer (sin BoundedSemaphore).

## Requisitos
- Ejemplos con `threading` y prints que indiquen entrada/critica/salida
- Diagramas Mermaid explicativos
- Archivo `controlZC.py` con demostraciones

## Ejemplo (parcial):

```python
import threading
import time

counter = 0
lock = threading.Lock()

def demo_mutex():
    def worker():
        global counter
        print('Entrando...')
        with lock:
            print('Seccion critica')
            tmp = counter
            time.sleep(0.1)
            tmp += 1
            counter = tmp
            print('Saliendo')
    threads = [threading.Thread(target=worker) for _ in range(4)]
    for t in threads: t.start()
    for t in threads: t.join()

if __name__ == '__main__':
    demo_mutex()
```

## Entregables
- `controlZC.py` con demos
- `primitivas.md` documentación

---
*Fin actividad 13.*
