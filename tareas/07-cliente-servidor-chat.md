# Tarea 7: Comunicación Cliente-Servidor (Sockets) - Chat

**Fechas:** 18 de marzo de 2026 - 22 de marzo de 2026

---

## Descripción

Establecer una comunicación básica entre dos computadoras mediante sockets TCP para crear un sistema de chat simple.

---

## Requisitos del Programa

### Componentes:
1. **Servidor:**
   - Escucha en un puerto específico
   - Acepta conexiones de clientes
   - Recibe y envía mensajes

2. **Cliente:**
   - Se conecta al servidor
   - Envía mensajes
   - Recibe respuestas

### Funcionalidades:
- Comunicación bidireccional
- Múltiples clientes conectados simultáneamente
- Interfaz de usuario simple
- Mensajes con timestamp
- Comando para desconectarse

---

## Especificaciones Técnicas

**Librerías Requeridas:**
- `socket`: Comunicación por sockets
- `threading`: Hilos para manejo de múltiples clientes
- `time`: Timestamps

### Instalación:
```bash
# Librerías estándar de Python
```

---

## Estructura del Programa

### Servidor:
```
Servidor esperando en puerto 5000
    ↓
Cliente 1 se conecta
    ↓
Cliente 2 se conecta
    ↓
Servidor reenvía mensajes entre clientes
```

### Flujo de Comunicación:
```
Cliente A → Servidor → Cliente B
         ← Servidor ←
```

---

## Formato de Mensajes

```
[HH:MM:SS] Usuario: Contenido del mensaje
[HH:MM:SS] Admin: Usuario X se conectó
[HH:MM:SS] Admin: Usuario X se desconectó
```

---

## Protocolo de Comunicación

```
CONNECT:nombre_usuario
MESSAGE:contenido_del_mensaje
DISCONNECT:nombre_usuario
```

---

## Evaluación

- [ ] Servidor escucha en puerto específico
- [ ] Clientes se conectan exitosamente
- [ ] Comunicación bidireccional funcional
- [ ] Manejo de múltiples clientes
- [ ] Timestamps en mensajes
- [ ] Desconexión correcta
- [ ] Código documentado

---

## Notas

- Puede ser en una misma máquina o en máquinas diferentes
- Usar localhost (127.0.0.1) para pruebas en la misma máquina
- Verificar que el puerto no esté en uso
- Implementar manejo de errores de conexión

