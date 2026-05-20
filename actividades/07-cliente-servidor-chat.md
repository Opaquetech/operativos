# Actividad 07 — Comunicación Cliente-Servidor (Sockets) — Chat

**Fechas:** 18-22 marzo 2026

## Descripción
Implementar un chat simple cliente-servidor usando sockets TCP. Permitir múltiples clientes y mensajes con timestamp.

## Requisitos
- Servidor que acepte conexiones entrantes.
- Reenvío de mensajes entre clientes.
- Manejo de varios clientes (hilos o select).
- Formato de mensajes con timestamps.

## Ejemplo de flujo
- Cliente conecta al servidor
- Envía `CONNECT:nombre`
- Envía `MESSAGE:contenido`
- Envía `DISCONNECT` para salir

## Entregables
- `chat_server.py` y `chat_client.py`
- Breve guía de uso

---
*Fin actividad 07.*
