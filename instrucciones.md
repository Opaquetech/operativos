# Instrucciones

Este archivo está destinado a contener las instrucciones de los problemas o tareas que quieras que resuelva.

## Cómo usarlo

1. Describe el problema o la tarea claramente.
2. Añade cualquier dato relevante:
   - Archivos afectados
   - Comportamiento esperado
   - Comportamiento actual
   - Errores o mensajes concretos
3. Si quieres, incluye ejemplos de entrada y salida o pasos para reproducir el problema.

## Ejemplo de formato

### Problema 1
- Descripción: Investigación técnica del puerto UDP 123 y mecanismos de protección en distintos dispositivos.
- Archivos involucrados: N/A
- Comportamiento esperado: Obtener una guía clara de uso y protección del puerto UDP 123.
- Comportamiento actual: Investigación pendiente.
- Pasos para reproducir: N/A

### Problema 2
- Descripción:
- Archivos involucrados:
- Comportamiento esperado:
- Comportamiento actual:
- Pasos para reproducir:

---

Puedes agregar aquí nuevos problemas cuando quieras y con gusto los resolveré uno por uno.

**Actividades añadidas**

- Actividad 15: Monitoreo de procesos activos → actividades/15-monitor-processes.md
- Actividad 16: Interfaz de servicios (Debian/Ubuntu) → actividades/16-services-gui.md
- Actividad 17: Resumen diagrama procesos Windows 11 → actividades/17-windows-processes-diagram.md

> La investigación completa del puerto UDP 123 se movió al archivo `investigacion-puerto-udp-123.md`.


Probelama 2.


Realizar un programa en python que realice un seguimiento de los procedimientos que se estan ejecutando en la computadora, indicando:

pid

nombre de la tarea

dirección de enlace establecida (si hay)

el puerto de enlace local

el sistema debe tener el manejo de monitoreo en tiempo real, brindar herramientas para ordenar por nombre de proceso o por pid o tiempo de enlace.

el sistema debe tener la generación de reportes (logs)

utilizar: psutil, tkinter

realizar un reporte de esta actividad  




Tareas a elaborar 


Guía de Problemas y Tareas de Programación
Este documento contiene la recopilación de instrucciones para diversos problemas técnicos, abarcando desde comandos de sistema hasta comunicación entre procesos y sockets.

1. Comandos Básicos del MS-DOS
Fechas: 13 de enero de 2026 - 14 de enero de 2026 Instrucciones: Estudiar los siguientes comandos y sus posibles variantes:

Red: ipconfig, netstat, ping, routert
Sistema de archivos: dir, mkdir, cd, rmdir, del, type
Utilidades: notepad, date, find, findstr
Tuberías: |, >, <
Entregable: Realizar una libreta (.ipynb) en VS Code instalando el complemento Jupyter.

2. MPI Suma (Mecanismos de Comunicación entre Procesos)
Fechas: 4 de marzo de 2026 - 11 de marzo de 2026 Instrucciones: Realizar un programa donde:

El proceso 0 genera 10,000 números.
Los reparte equitativamente entre cuatro procesos.
Cada proceso realiza la suma de su parte.
El proceso 0 recibe los resultados y muestra la suma total.
Tecnología: MPI y mpi4py.

3. Productor y Consumidor con Corrutinas
Fechas: 4 de marzo de 2026 - 11 de marzo de 2026 Instrucciones: Simulación del modelo productor-consumidor.

Utilizar corrutinas (async).
Librerías: queue, asyncio.
Implementar bloqueo de zona crítica mediante candados (locks).
Salida visual: Imprimir con colores diferentes para cada trabajador.
4. Visualización de IPv4 en Tiempo Real (netstat)
Fechas: 4 de marzo de 2026 - 15 de marzo de 2026 Instrucciones: Programa que lea en tiempo real las direcciones IPv4 enlazadas a la computadora usando netstat.

Utilizar tuberías del sistema y os.system.
Interfaz gráfica con tkinter.
Validación: Mostrar en color rojo aquellas IPs que no sean válidas (referencia: ipblocklist).
Reporte: Incluir portada, documentación, código comentado, capturas de corridas y conclusión.
5. Visualización de URLs en Tiempo Real (netstat)
Fechas: 4 de marzo de 2026 - 23 de marzo de 2026 Instrucciones: Similar al proyecto de IPs, pero enfocado en URLs.

Extraer URLs de netstat en tiempo real.
Interfaz con tkinter.
Validación: Resaltar en rojo URLs no válidas (referencia: blacklists).
Reporte: Incluir portada, documentación, código comentado, corridas y conclusión.
6. Ejecución de Comandos Bash vía aiohttp
Fechas: 4 de marzo de 2026 - 30 de marzo de 2026 Instrucciones: Utilizando el framework aiohttp, desarrollar una aplicación web que permita ejecutar comandos de bash remotamente.

Librería base: os (específicamente system).
7. Comunicación Cliente-Servidor (Sockets)
Fechas: 18 de marzo de 2026 - 22 de marzo de 2026 Instrucciones: Establecer una comunicación básica entre dos computadoras para crear un sistema de chat pequeño.

8. Lectura Remota de Directorios (Sockets)
Fechas: 18 de marzo de 2026 - 29 de marzo de 2026 Instrucciones: Desarrollar dos programas (cliente/servidor) que permitan leer el contenido de un directorio en una máquina remota mediante sockets.

9. Módulos en Linux
Fechas: 15 de abril de 2026 - 22 de abril de 2026 Instrucciones: Trabajar en un entorno Linux nativo o Live (no WSL/VM dentro de Windows).

Seguir los pasos técnicos del vídeo proporcionado sobre módulos del kernel.
Entregable: Capturas de pantalla de los procedimientos realizados.
10. Hilos con Semáforos (httpx)
Fechas: 22 de abril de 2026 - 24 de abril de 2026 Instrucciones: Programa en Python que:

Lea una lista de URLs desde un archivo.
Las explore de forma concurrente usando la librería httpx.
Controle la concurrencia mediante semáforos de asyncio.
11. Hilos con Semáforos y Tkinter
Fechas: 22 de abril de 2026 - 28 de abril de 2026 Instrucciones: Evolución del problema anterior integrando una interfaz gráfica con tkinter para visualizar el proceso de exploración de las URLs.

12. Programación de Tarjetas de Vídeo (Tutorial)
Fechas: 24 de abril de 2026 - 1 de mayo de 2026 Instrucciones: Crear un tutorial con ejemplos explicados sobre el uso de aceleración por hardware en:

NVIDIA
AMD
Apple
Genérico (OpenCL)
13. Primitivas de Sincronización de Procesos
Fechas: 29 de abril de 2026 - 4 de mayo de 2026 Instrucciones: Implementar ejemplos de sincronización (excepto BoundedSemaphore).

Requisito: Ejemplo simple con prints para identificar las áreas (sección crítica, etc.).
Documentación: Dibujar diagrama de flujo usando sintaxis Mermaid.
Archivos relacionados: controlZC.py, hilos.md.
14. Puerto UDP 123
Fechas: 13 de mayo de 2026 - 20 de mayo de 2026

Instrucciones: Realizar una investigación del puerto udp 123:

documentación general del funcionamiento del puerto 123
mecanismos de protección en diferentes dispositivos:
router
laptop
celular
etc.
15. (Adicional) Monitoreo de procesos activos en el sistema con Python
Fechas: 13 de mayo de 2026 - 20 de mayo de 2026

Instrucciones: Realizar un programa en python que realice un seguimiento de los procedimientos que se estan ejecutando en la computadora, indicando:

pid

nombre de la tarea

dirección de enlace establecida (si hay)

el puerto de enlace local

el sistema debe tener el manejo de monitoreo en tiempo real, brindar herramientas para ordenar por nombre de proceso o por pid o tiempo de enlace.

el sistema debe tener la generación de reportes (logs)

utilizar: psutil, tkinter

realizar un reporte de esta actividad

16. Diagrama de procesos de Windows
Fechas: 13 de mayo de 2026 - 20 de mayo de 2026

Instrucciones: Realizar un resumen del diagrama de procesos de windows 11.

ampliar la explicación utilizando otra documentación incluyendo AI.

17. (Adicional) Diagrama de procesos de Debian
Fechas: 13 de mayo de 2026 - 20 de mayo de 2026

Instrucciones: Realizar un resumen del diagrama de procesos de windows 11 Debian.

ampliar la explicación utilizando otra documentación incluyendo AI.





    Tareas.



ACtividades

1
Estudiar los siguientes comandos y sus posibles variantes:

ipconfig
netstat
ping
routert
dir
mkdir
cd
rmdir
del
type
notepad
date
find
findstr
tuberias: |, >, < 
Realizar una libreta  (ipynb) en VScode  instalando el complemento jupyter.
subir la libreta

2
realizar un programa que el proceso 0 genere 10000 números y los reparta equitativamente entre cuatro procesos y cada proceso realize la suma.

el proceso 0 mostrará el resultado

utiliza MPI y mpi4py

3
Realizar la simulación del productor-consumidor utilizando corrutinas (async)

utilizar las librerias queue, asyncio

bloquear con candado(s) la zona crítica.

imprimir con colores diferentes cada trabajador.


4
Realizar un programa utilizando tuberías del sistema y la función system de la librería os. para leer en tiempo real las ips versión 4 que aparecen en "netstat". mostrar con rojo aquellas que no son válidas.

Utilizar tkinter.

hint: https://github.com/bitwire-it/ipblocklist

realizar un reporte de esta actividad incluyendo portada, documentación, código comentado, corridas, conclusión.

6
Utilizando el framework aiohttp, realizar un programa que vía web ejecute comandos del bash.

Utilizar la librería: os en especial system


7
realizar un programa que establezca la comunicación entre dos computadoras como un pequeño chat.


8
realizar dos programas que lean en directorio remotamente utilizando sockets.


10
realizar un programa en python que lea de un archivo una lista de urls y las explore usando la librería httpx, semáforos. 

hint:

httpx

semáforo:

import asyncio
import random

async def worker(semaphore, worker_id):
    # This block ensures only 'value' number of workers run at once
    async with semaphore:
        print(f"Worker {worker_id} has started working.")
        # Simulate a task (e.g., API call, file I/O)
        await asyncio.sleep(random.uniform(1, 3))
        print(f"Worker {worker_id} is done.")

async def main():
    # Allow a maximum of 2 concurrent workers
    sem = asyncio.Semaphore(2)
    
    # Create 5 tasks that will compete for the 2 slots
    tasks = [worker(sem, i) for i in range(5)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())

barrier:

import asyncio

async def tarea_trabajadora(nombre, barrier):
    print(f"Tarea {nombre} trabajando...")
    await asyncio.sleep(1)
    print(f"Tarea {nombre} ha llegado a la barrera.")
    
    # Esperar a que las 3 tareas lleguen aquí
    await barrier.wait()
    
    print(f"Tarea {nombre} pasó la barrera.")

async def main():
    # Definir una barrera para 3 partes
    barrera = asyncio.Barrier(3)
    
    # Crear e iniciar las tareas
    await asyncio.gather(
        tarea_trabajadora("A", barrera),
        tarea_trabajadora("B", barrera),
        tarea_trabajadora("C", barrera)
    )

if __name__ == "__main__":
    asyncio.run(main())



11
realizar un programa en python que lea de un archivo una lista de urls y las explore usando la librería httpx, semáforos. Usando tkinter

hint:

httpx

semáforo:

import asyncio
import random

async def worker(semaphore, worker_id):
    # This block ensures only 'value' number of workers run at once
    async with semaphore:
        print(f"Worker {worker_id} has started working.")
        # Simulate a task (e.g., API call, file I/O)
        await asyncio.sleep(random.uniform(1, 3))
        print(f"Worker {worker_id} is done.")

async def main():
    # Allow a maximum of 2 concurrent workers
    sem = asyncio.Semaphore(2)
    
    # Create 5 tasks that will compete for the 2 slots
    tasks = [worker(sem, i) for i in range(5)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())

barrier:

import asyncio

async def tarea_trabajadora(nombre, barrier):
    print(f"Tarea {nombre} trabajando...")
    await asyncio.sleep(1)
    print(f"Tarea {nombre} ha llegado a la barrera.")
    
    # Esperar a que las 3 tareas lleguen aquí
    await barrier.wait()
    
    print(f"Tarea {nombre} pasó la barrera.")

async def main():
    # Definir una barrera para 3 partes
    barrera = asyncio.Barrier(3)
    
    # Crear e iniciar las tareas
    await asyncio.gather(
        tarea_trabajadora("A", barrera),
        tarea_trabajadora("B", barrera),
        tarea_trabajadora("C", barrera)
    )

if __name__ == "__main__":
    asyncio.run(main())




12    Realizar un tutorial mostrando pequeños ejemplos ampliamente explicados del uso de:
nvidia
amd
apple
genérico (opencl)




14

Adicionales 


Realizar un resumen del diagrama de procesos de windows 11.

ampliar la explicación utilizando otra documentación incluyendo AI.


15
Realizar un programa en python que realice un seguimiento de los procedimientos que se estan ejecutando en la computadora, indicando:

pid

nombre de la tarea

dirección de enlace establecida (si hay)

el puerto de enlace local

el sistema debe tener el manejo de monitoreo en tiempo real, brindar herramientas para ordenar por nombre de proceso o por pid o tiempo de enlace.

el sistema debe tener la generación de reportes (logs)

utilizar: psutil, tkinter

realizar un reporte de esta actividad


16
En python y utilizando tkinter:

Realizar una interfaz gráfica del manejo de servicios en linux debian, ubuntu.

Similar al programa systemctl.

El programa debe mostrar todos los servicios activos, detener los servicios seleccionados, cargar servicios, desabilitar servicios. 

Tomar en cuenta que algunos servicios para que puedan ser eliminados se tiene que remontar (mount) la particion en modo lectura y escritura, modificar el servicio y al final verificar que se vuelve a montar partición con sus atributos originales.

Realizar un reporte amplio: portada, explicación de los servicios en Linux, programa bien documentado, varias corridas mostrando los diferentes usos, conclusión.


17
Realizar un resumen del diagrama de procesos de windows 11.

ampliar la explicación utilizando otra documentación incluyendo AI.


ACTIVIDAD FINAL 

En python y utilizando tkinter:

Realizar una interfaz gráfica del manejo de servicios en linux debian, ubuntu.

Similar al programa systemctl.

El programa debe mostrar todos los servicios activos, detener los servicios seleccionados, cargar servicios, desabilitar servicios. 

Tomar en cuenta que algunos servicios para que puedan ser eliminados se tiene que remontar (mount) la particion en modo lectura y escritura, modificar el servicio y al final verificar que se vuelve a montar partición con sus atributos originales.

Realizar un reporte amplio: portada, explicación de los servicios en Linux, programa bien documentado, varias corridas mostrando los diferentes usos, conclusión.







