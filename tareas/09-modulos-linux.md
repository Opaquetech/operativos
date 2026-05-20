# Tarea 9: Módulos en Linux

**Fechas:** 15 de abril de 2026 - 22 de abril de 2026

---

## Descripción

Trabajar en un entorno Linux nativo o Live para aprender sobre módulos del kernel de Linux, siguiendo procedimientos técnicos establecidos.

---

## Requisitos

### Entorno:
- ⚠️ Trabajar en Linux nativo o Live (no WSL o VM dentro de Windows)
- Acceso con permisos de administrador (sudo)
- Terminal de comandos

### Opciones de Entorno:
1. **Linux Nativo:** Instalación completa de Linux
2. **Live USB/DVD:** Bootear desde medio removible
3. **Máquina Virtual nativa:** VirtualBox/KVM en Linux

---

## Contenidos a Cubrir

### 1. Introducción a Módulos del Kernel
- Qué son los módulos del kernel
- Ventajas sobre compilación estática
- Ubicación de módulos (`/lib/modules/`)

### 2. Comandos Principales

```bash
# Listar módulos cargados
lsmod

# Obtener información de un módulo
modinfo nombre_modulo

# Cargar un módulo
sudo insmod ruta/modulo.ko
sudo modprobe nombre_modulo

# Descargar un módulo
sudo rmmod nombre_modulo

# Parámetros de módulos
cat /sys/module/nombre_modulo/parameters/
```

### 3. Creación de Módulos Simples
- Estructura básica de un módulo
- Función init_module y cleanup_module
- Compilación con Makefile
- Instalación y prueba

### 4. Debugging de Módulos
- Ver mensajes del kernel con dmesg
- Parámetros de módulo
- Monitoreo de carga/descarga

---

## Procedimientos a Realizar

### Paso 1: Configurar Entorno
```bash
# Instalar herramientas de desarrollo
sudo apt-get install build-essential linux-headers-$(uname -r)
```

### Paso 2: Listar Módulos
```bash
# Ver módulos actualmente cargados
lsmod | head -20

# Ver información detallada
modinfo ext4
```

### Paso 3: Crear Módulo Simple
```c
// hello.c
#include <linux/module.h>
#include <linux/kernel.h>

int init_module(void) {
    printk(KERN_INFO "Módulo cargado!\n");
    return 0;
}

void cleanup_module(void) {
    printk(KERN_INFO "Módulo descargado!\n");
}
```

### Paso 4: Compilar y Cargar
```bash
make
sudo insmod hello.ko
dmesg | tail -5
sudo rmmod hello
```

---

## Entregable

Captura de pantalla de los procedimientos:

- [ ] Entorno Linux funcional
- [ ] Listado de módulos cargados
- [ ] Información de módulo específico
- [ ] Creación de módulo simple
- [ ] Compilación exitosa
- [ ] Carga del módulo
- [ ] Mensajes en dmesg
- [ ] Descarga del módulo

---

## Evaluación

- [ ] Trabajo en Linux nativo/Live
- [ ] Comandos ejecutados correctamente
- [ ] Capturas de pantalla claras
- [ ] Módulo simple compilado
- [ ] Módulo cargado sin errores
- [ ] Documentación de procedimientos

