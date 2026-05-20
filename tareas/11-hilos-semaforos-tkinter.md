# Tarea 11: Hilos con Semáforos y Tkinter

**Fechas:** 22 de abril de 2026 - 28 de abril de 2026

---

## Descripción

Evolución del proyecto anterior (Tarea 10) integrando una interfaz gráfica con tkinter para visualizar en tiempo real el proceso de exploración de URLs.

---

## Requisitos del Programa

### Funcionalidades:
1. **Todas las de la Tarea 10 más:**
   - Interfaz gráfica con tkinter
   - Visualización en tiempo real
   - Barra de progreso
   - Estado de cada URL
   - Control de ejecución

### Componentes de la GUI:
1. **Área de entrada:**
   - Selector de archivo URLs.txt
   - Configuración de semáforo (número de conexiones)
   - Botones de inicio/pausa/cancelar

2. **Área de progreso:**
   - Barra de progreso global
   - URLs procesadas / Total
   - Velocidad de procesamiento

3. **Lista de URLs:**
   - Mostrar cada URL procesada
   - Status code o error
   - Tiempo de respuesta
   - Color según resultado (verde=OK, rojo=error)

4. **Estadísticas:**
   - Total de URLs
   - Exitosas/Errores
   - Tiempo transcurrido
   - Tiempo estimado restante

---

## Especificaciones Técnicas

**Librerías Requeridas:**
- `tkinter`: Interfaz gráfica
- `httpx`: Cliente HTTP asincrónico
- `asyncio`: Programación asincrónica
- `threading`: Hilos para no bloquear GUI

### Instalación:
```bash
pip install httpx
```

---

## Diseño de Interfaz

```
╔═══════════════════════════════════════════════════╗
║     Explorador de URLs - Interfaz Gráfica        ║
╠═══════════════════════════════════════════════════╣
║ Archivo: [URLs.txt] [Examinar...]                ║
║ Semáforo: [5 conexiones] ↕                       ║
║                                                   ║
║ [Inicio] [Pausa] [Cancelar] [Limpiar]            ║
║                                                   ║
║ Progreso: [████████░░░░░░░░░░░░░░] 35% (7/20)   ║
║                                                   ║
║ Resultados:                                       ║
║ ┌────────────────────────────────────────────┐  ║
║ │ ✓ google.com         200 OK      0.52s    │  ║
║ │ ✓ github.com         200 OK      0.38s    │  ║
║ │ → python.org         301 REDIR   0.45s    │  ║
║ │ ✗ invalid.xyz        ERROR      timeout  │  ║
║ │ ✓ stackoverflow.com   200 OK      0.61s    │  ║
║ └────────────────────────────────────────────┘  ║
║                                                   ║
║ Estadísticas:                                    ║
║ Procesadas: 7/20 | Exitosas: 6 | Errores: 1    ║
║ Tiempo: 0:02:35 | Estimado: 0:04:30             ║
╚═══════════════════════════════════════════════════╝
```

---

## Estructura del Código

### Componentes principales:
1. **Clase GUI (tkinter):**
   - Construir interfaz
   - Manejar eventos de botones
   - Actualizar displays

2. **Clase Worker (asyncio):**
   - Ejecutar exploración de URLs
   - Controlar semáforos
   - Reportar progreso

3. **Thread Manager:**
   - Ejecutar worker en hilo separado
   - No bloquear interfaz principal

---

## Características Avanzadas

### Colores por Estado:
- ✓ Verde: Status 2xx (OK)
- → Amarillo: Status 3xx (Redirección)
- ⚠ Naranja: Status 4xx (Cliente error)
- ✗ Rojo: Status 5xx o conexión rechazada

### Funcionalidades Adicionales:
- [ ] Pausar/Reanudar exploración
- [ ] Cancelar en cualquier momento
- [ ] Exportar resultados a CSV
- [ ] Guardar/Cargar configuración
- [ ] Historial de exploraciones

---

## Evaluación

- [ ] Interfaz gráfica funcional
- [ ] Carga de archivo URLs.txt
- [ ] Configuración de semáforo
- [ ] Barra de progreso actualizada
- [ ] Lista de resultados en tiempo real
- [ ] Estadísticas correctas
- [ ] Colores según status
- [ ] Sin bloqueo de interfaz
- [ ] Botones de control funcionan
- [ ] Código documentado

