# Tarea 15: Monitoreo de Procesos Activos del Sistema

**Fechas:** 20 de mayo de 2026 - 27 de mayo de 2026

---

## Descripcion

Realizar un programa en Python que permita monitorear en tiempo real los procesos activos del sistema y sus conexiones de red, mostrando informacion clave de cada proceso.

---

## Requisitos del Programa

El sistema debe indicar, como minimo:

1. `PID`
2. `Nombre de la tarea/proceso`
3. `Direccion de enlace establecida` (si existe)
4. `Puerto de enlace local`

Adicionalmente, el sistema debe incluir:

1. **Monitoreo en tiempo real**
   - Actualizacion periodica automatica de los datos.
   - Visualizacion continua de procesos y conexiones activas.

2. **Herramientas de ordenamiento**
   - Ordenar por nombre de proceso.
   - Ordenar por PID.
   - Ordenar por tiempo de enlace/conexion.

3. **Generacion de reportes (logs)**
   - Registrar eventos del monitoreo en archivos de log.
   - Guardar evidencia de ejecucion y cambios observados.

---

## Tecnologias Obligatorias

- `psutil`
- `tkinter`

### Instalacion sugerida

```bash
pip install psutil
```

> Nota: `tkinter` suele venir incluido con Python en la mayoria de distribuciones.

---

## Especificaciones Tecnicas Minimas

- Interfaz grafica desarrollada con `tkinter`.
- Lectura de procesos y conexiones con `psutil`.
- Tabla o lista visual con columnas para PID, nombre, direccion y puerto.
- Botones o controles para ordenar por los criterios solicitados.
- Actualizacion automatica sin bloquear la interfaz.
- Registro de logs en archivo (por ejemplo: `monitor_log.txt`).

---

## Entregables

1. Codigo fuente del programa en Python.
2. Evidencia de funcionamiento (capturas o salida de logs).
3. **Reporte de la actividad** en formato Markdown o PDF.

---

## Estructura Sugerida del Reporte

1. Portada
   - Titulo de la actividad
   - Nombre del estudiante
   - Asignatura
   - Fecha

2. Introduccion
   - Objetivo del monitoreo de procesos
   - Importancia del seguimiento en tiempo real

3. Herramientas utilizadas
   - `psutil`
   - `tkinter`

4. Desarrollo
   - Diseno de la solucion
   - Explicacion del codigo principal
   - Implementacion del monitoreo en tiempo real
   - Implementacion del ordenamiento
   - Implementacion de logs

5. Resultados
   - Capturas de pantalla del programa
   - Ejemplo de registros generados en logs

6. Conclusiones
   - Aprendizajes obtenidos
   - Problemas encontrados y soluciones

7. Bibliografia
   - Documentacion oficial de `psutil` y `tkinter`

---

## Criterios de Evaluacion

- [ ] Muestra PID, nombre, direccion de enlace y puerto local.
- [ ] Monitoreo en tiempo real funcionando correctamente.
- [ ] Ordenamiento por nombre, PID y tiempo de enlace implementado.
- [ ] Generacion de logs/reportes funcionando.
- [ ] Uso correcto de `psutil` y `tkinter`.
- [ ] Reporte tecnico completo y claro.
