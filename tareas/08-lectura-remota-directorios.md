# Tarea 8: Lectura Remota de Directorios (Sockets)

**Fechas:** 18 de marzo de 2026 - 29 de marzo de 2026

---

## Descripción

Desarrollar un sistema cliente-servidor que permita leer el contenido de un directorio en una máquina remota mediante sockets TCP.

---

## Requisitos del Programa

### Servidor (máquina remota):
- Escucha peticiones en un puerto específico
- Acepta rutas de directorios como parámetro
- Lee el contenido del directorio
- Envía lista de archivos/directorios al cliente
- Validación de rutas (no permitir acceso fuera del directorio permitido)

### Cliente (máquina local):
- Se conecta al servidor remoto
- Envía rutas de directorios
- Recibe y muestra contenido
- Interfaz de usuario simple

---

## Especificaciones Técnicas

**Librerías Requeridas:**
- `socket`: Comunicación por sockets
- `os`: Manejo de directorios
- `json`: Serialización de datos (opcional)
- `threading`: Manejo de múltiples clientes

### Instalación:
```bash
# Librerías estándar
```

---

## Estructura del Programa

### Protocolo de Comunicación:

```
Cliente → REQUEST:/ruta/del/directorio
         ← SERVER:archivo1.txt|archivo2.txt|carpeta1/
         
Cliente → REQUEST:/ruta/invalida
         ← ERROR:Acceso denegado
```

---

## Información a Mostrar por Archivo

```
Nombre: documento.txt
Tipo: Archivo
Tamaño: 2,048 bytes
Fecha Modificación: 2026-03-18 14:30:45
Permisos: -rw-r--r--
```

### Para Directorios:
```
Nombre: MiCarpeta
Tipo: Directorio
Contenidos: 5 elementos
Fecha Modificación: 2026-03-18 12:00:00
Permisos: drwxr-xr-x
```

---

## Seguridad

### Consideraciones Importantes:
- ⚠️ Validar que no se acceda a directorios padre (../)
- ⚠️ Restringir a un directorio base permitido
- ⚠️ No exponer permisos de archivos sensibles
- ⚠️ Logging de accesos
- ⚠️ Autenticación (opcional pero recomendado)

---

## Interfaz del Cliente

```
=== Lector Remoto de Directorios ===

Servidor: 192.168.1.100
Puerto: 5001
Estado: Conectado ✓

Ruta actual: /home/user/documentos
[Cambiar ruta]

Contenido:
  - proyecto1/ (directorio)
  - proyecto2/ (directorio)
  - readme.txt (2.5 KB)
  - config.ini (512 B)
```

---

## Evaluación

- [ ] Servidor escucha correctamente
- [ ] Cliente se conecta al servidor
- [ ] Lectura correcta de directorios
- [ ] Información de archivos completa
- [ ] Validación de rutas funcional
- [ ] Seguridad en acceso de directorios
- [ ] Interfaz clara y amigable
- [ ] Código documentado

