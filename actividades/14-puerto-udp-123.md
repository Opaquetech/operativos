# Actividad 14 — Investigación: Puerto UDP 123 (NTP)

**Fechas:** 13-20 mayo 2026

## Descripción
Reporte sobre el puerto UDP 123 usado por NTP: funcionamiento, riesgos y mecanismos de protección en routers, laptops, celulares y otros dispositivos.

## Contenido resumido (report):
- Definición: UDP/123 reservado por IANA para NTP/SNTP.
- Funcionamiento: cliente envía petición, servidor responde con marcas de tiempo; cálculo de offset y delay.
- Documentación técnica: RFC 5905 (NTPv4), RFC 4330 (SNTP).
- Riesgos: spoofing, amplificación/reflection, envenenamiento de hora.
- Protecciones:
  - Routers: ACLs, rate limiting, filtrado, NTS
  - Laptops: firewall local, `chrony`/`ntpd`/`systemd-timesyncd`, NTS
  - Celulares: sincronización por operador (NITZ), restricciones de SO
  - IoT/Servidores: usar servidores internos y autenticados

## Referencia
Ver también `investigacion-puerto-udp-123.md` en la raíz del proyecto.

---
*Fin actividad 14.*
