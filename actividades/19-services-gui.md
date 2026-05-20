# Interfaz Grafica para Manejo de Servicios en Linux

**Fechas:** 20 de mayo de 2026 - 27 de mayo de 2026

---

## Descripcion

Desarrollar en Python una interfaz grafica para administrar servicios en Linux (Debian/Ubuntu), con funcionalidades similares a `systemctl`, utilizando `tkinter`.

La aplicacion debe permitir visualizar servicios, ejecutar acciones administrativas y registrar evidencia de cada operacion.

---

## Objetivo General

Construir una herramienta GUI para la administracion de servicios del sistema en Debian/Ubuntu, integrando buenas practicas de seguridad, validacion y trazabilidad.

---

## Objetivos Especificos

1. Mostrar todos los servicios activos del sistema.
2. Permitir detener servicios seleccionados.
3. Permitir cargar/iniciar servicios.
4. Permitir deshabilitar servicios.
5. Implementar flujo de montaje seguro cuando se requieran cambios sobre archivos de servicios en particiones montadas en solo lectura.
6. Generar reportes y logs de las operaciones ejecutadas.

---

## Tecnologias Obligatorias

- Python 3
- tkinter
- subprocess
- logging

Opcional recomendado:

- threading (para no bloquear la GUI)
- queue (comunicacion segura entre hilos)

---

## Requisitos Funcionales

### 1. Visualizacion de servicios

- Mostrar una tabla/lista con al menos:
  - Nombre del servicio
  - Estado (active, inactive, failed, etc.)
  - Si esta habilitado (enabled/disabled)
  - Descripcion
- Boton de refresco para actualizar la lista.

### 2. Acciones sobre servicios

La GUI debe permitir ejecutar sobre el servicio seleccionado:

- Iniciar (`start`)
- Detener (`stop`)
- Reiniciar (`restart`) (recomendado)
- Recargar (`reload`) (opcional)
- Habilitar (`enable`) (recomendado)
- Deshabilitar (`disable`)

### 3. Confirmaciones de seguridad

- Solicitar confirmacion antes de detener o deshabilitar servicios.
- Advertir si el servicio pertenece a componentes criticos del sistema.

### 4. Logs y reportes

- Registrar en archivo de log:
  - Fecha y hora
  - Usuario que ejecuta
  - Servicio afectado
  - Comando ejecutado
  - Resultado (exito/error)
- Permitir exportar reporte de operaciones en `.txt` o `.csv`.

---

## Requisito Especial: Montaje y Restauracion de Particiones

Algunos cambios sobre archivos de unidad (`.service`) pueden requerir escritura en una particion montada en solo lectura.

El programa debe contemplar este flujo:

1. Detectar el punto de montaje donde se realizara la modificacion.
2. Verificar modo de montaje actual (ro/rw).
3. Si esta en `ro`, remontar temporalmente en `rw`.
4. Ejecutar cambios requeridos.
5. Verificar integridad/configuracion (`systemctl daemon-reload`, validaciones).
6. Restaurar el modo original de montaje (si era `ro`, volver a `ro`).
7. Registrar todas las acciones en log.

### Reglas de seguridad obligatorias

- Nunca dejar la particion en `rw` si originalmente estaba en `ro`.
- Si ocurre error en cualquier paso, ejecutar rutina de rollback para restaurar estado inicial.
- Mostrar en GUI el estado final del montaje y resultado de la operacion.

---

## Requisitos Tecnicos Minimos del Programa

- Interfaz desarrollada con `tkinter`.
- Ejecucion de comandos via `subprocess`.
- Manejo de errores robusto (timeouts, permisos, servicios inexistentes, comandos fallidos).
- No bloquear la GUI durante operaciones largas.
- Comentarios tecnicos claros en funciones clave.
- Codigo modular (funciones o clases separadas para GUI, comandos y logs).

---

## Entregables

1. Codigo fuente Python del programa.
2. Archivo(s) de log generados durante pruebas.
3. Capturas de pantalla de varias corridas (diferentes casos de uso).
4. Reporte amplio en Markdown o PDF.

---

## Estructura Obligatoria del Reporte Amplio

### 1. Portada

- Titulo de la actividad
- Nombre del alumno
- Asignatura
- Fecha

### 2. Introduccion

- Que son los servicios en Linux
- Importancia de `systemctl` y systemd

### 3. Marco teorico

- Conceptos: servicio, daemon, unidad systemd
- Estados de servicio
- Habilitado vs activo
- Riesgos operativos al administrar servicios

### 4. Diseno de la solucion

- Arquitectura del programa
- Descripcion de la interfaz
- Flujo de comandos ejecutados

### 5. Implementacion

- Explicacion del codigo por modulos
- Manejo de permisos y errores
- Manejo de remontaje `ro` -> `rw` -> estado original
- Generacion de logs/reportes

### 6. Pruebas y corridas

- Varias corridas mostrando:
  - Listado de servicios
  - Detencion de servicio
  - Carga/inicio de servicio
  - Deshabilitacion de servicio
  - Caso con remontaje y restauracion
- Evidencia con capturas y resultado de logs

### 7. Analisis de resultados

- Problemas encontrados
- Lecciones aprendidas
- Buenas practicas observadas

### 8. Conclusiones

- Aportes de la practica
- Limites de la herramienta
- Posibles mejoras

### 9. Bibliografia

- Documentacion oficial de systemd/systemctl
- Documentacion de Python (tkinter, subprocess, logging)

---

## Criterios de Evaluacion

- [ ] La GUI muestra servicios activos correctamente.
- [ ] Permite detener servicios seleccionados.
- [ ] Permite cargar/iniciar servicios.
- [ ] Permite deshabilitar servicios.
- [ ] Implementa flujo seguro de remontaje y restauracion de particion.
- [ ] Genera logs completos de operaciones.
- [ ] Presenta varias corridas con evidencia.
- [ ] Reporte amplio completo y bien estructurado.

---

## Nota de Seguridad

No se deben detener ni deshabilitar servicios criticos en entornos de produccion.
Realizar pruebas en entorno controlado (maquina virtual o laboratorio).
