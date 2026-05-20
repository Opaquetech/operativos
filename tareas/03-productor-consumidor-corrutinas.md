# Tarea 3: Productor y Consumidor con Corrutinas

**Fechas:** 4 de marzo de 2026 - 11 de marzo de 2026

---

## Descripción

Implementar una simulación del modelo clásico productor-consumidor utilizando corrutinas asincrónicas en Python.

---

## Requisitos del Programa

### Modelo:
- Implementar patrón productor-consumidor
- Utilizar corrutinas (async/await)
- Un o más productores generan datos
- Uno o más consumidores procesan datos
- Cola compartida entre productores y consumidores

### Características:
- Bloqueo de zona crítica mediante candados (locks)
- Salida visual con colores diferentes para cada trabajador
- Sincronización entre productores y consumidores

---

## Especificaciones Técnicas

**Librerías Requeridas:**
- `queue` (Queue o asyncio.Queue)
- `asyncio` (corrutinas)
- `threading` o locks de asyncio para sincronización

### Instalación:
```bash
# Estas librerías vienen con Python, pero se puede usar:
pip install colorama  # Para colores en terminal (opcional)
```

---

## Estructura Esperada

```
┌─────────────┐
│  Productor  │ ──┐
└─────────────┘   │
                  ├──→ [Cola Compartida] ──→ Consumidor 1
┌─────────────┐   │                           Consumidor 2
│  Productor  │ ──┘
└─────────────┘
```

---

## Características de Salida

### Ejemplo de Salida Visual:
```
[PRODUCTOR_1] Produciendo... dato_123
[CONSUMIDOR_1] Consumiendo... dato_123
[PRODUCTOR_2] Produciendo... dato_124
[CONSUMIDOR_2] Consumiendo... dato_124
```

Usar colores:
- Verde para productores
- Azul para consumidores
- Rojo para errores

---

## Evaluación

- [ ] Corrutinas implementadas correctamente
- [ ] Cola funcional y compartida
- [ ] Locks/candados en zona crítica
- [ ] Sincronización sin deadlocks
- [ ] Salida con colores diferenciados
- [ ] Código bien documentado

