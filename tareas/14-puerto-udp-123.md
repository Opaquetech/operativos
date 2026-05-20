# Tarea 14: Investigación - Puerto UDP 123 (NTP)

**Fechas:** 13 de mayo de 2026 - 20 de mayo de 2026

---

## Descripción

Realizar una investigación técnica completa del puerto UDP 123, que es utilizado por el protocolo NTP (Network Time Protocol), incluyendo funcionamiento, mecanismos de protección y riesgos de seguridad.

---

## Contenidos a Investigar

### 1. Documentación General del Funcionamiento

- [ ] Qué es UDP 123 (NTP)
- [ ] Protocolo NTP vs SNTP
- [ ] Arquitectura cliente-servidor
- [ ] Capas de transporte (TCP/IP)
- [ ] Formato de paquetes NTP
- [ ] Estratos de servidores NTP
- [ ] Referencias RFC (5905, 4330)

### 2. Mecanismos de Protección en Diferentes Dispositivos

#### Router
- [ ] Filtrado de paquetes UDP/123
- [ ] Firewall stateful
- [ ] NAT/PAT
- [ ] ACL (Listas de Control de Acceso)
- [ ] Rate limiting
- [ ] Proxy NTP
- [ ] Autenticación NTP

#### Laptop/PC
- [ ] Firewall local del SO
- [ ] Servicios de tiempo confiables
- [ ] Configuración de cliente NTP
- [ ] Windows Time Service
- [ ] Linux: chrony, ntpd, systemd-timesyncd
- [ ] Validación de servidores
- [ ] NTS (Network Time Security)

#### Celular/Smartphone
- [ ] Sincronización automática
- [ ] Protección nativa del SO
- [ ] Restricciones de red
- [ ] NITZ (Network Identity and Time Zone)
- [ ] Operador de red vs NTP directo
- [ ] Permisos de aplicaciones

#### Otros Dispositivos (IoT, Servidores, etc.)
- [ ] Servidores dedicados
- [ ] Dispositivos IoT
- [ ] Equipos industriales
- [ ] Consideraciones especiales

---

## Riesgos y Vulnerabilidades

- [ ] Spoofing de paquetes NTP
- [ ] Ataques de amplificación
- [ ] DDoS mediante reflexión NTP
- [ ] Man-in-the-middle
- [ ] Inyección de hora falsa
- [ ] Degradación de servicio

---

## Buenas Prácticas

- [ ] Servidores autorizados
- [ ] Autenticación NTP
- [ ] Monitoreo de sincronización
- [ ] Actualización de firmware
- [ ] Segmentación de red
- [ ] Logging de eventos

---

## Estructura del Reporte

```
1. Portada
   - Título
   - Fecha
   - Autor
   - Asignatura

2. Tabla de Contenidos

3. Introducción
   - Importancia de sincronización de tiempo
   - Rol de UDP 123

4. Fundamentos de NTP
   4.1 Protocolo NTP
   4.2 UDP 123 vs otros protocolos
   4.3 Arquitectura

5. Funcionamiento Técnico
   5.1 Estructura de paquete NTP
   5.2 Proceso de sincronización
   5.3 Estratos y jerarquía

6. Mecanismos de Protección
   6.1 Router
   6.2 Laptop
   6.3 Celular
   6.4 Otros dispositivos

7. Riesgos y Vulnerabilidades
   7.1 Vectores de ataque
   7.2 Impacto potencial

8. Mejores Prácticas
   8.1 Configuración segura
   8.2 Monitoreo

9. Herramientas para Análisis
   - netstat
   - wireshark
   - ntpstat
   - chronyc

10. Conclusiones

11. Referencias
    - RFC 5905
    - RFC 4330
    - Documentación de NTP
```

---

## Archivos de Referencia

Existe una investigación previa en: `investigacion-puerto-udp-123.md`

---

## Formato del Reporte

- Formato: Markdown (.md) o PDF
- Mínimo 15 páginas (si PDF)
- Incluir diagramas (Mermaid)
- Tablas comparativas
- Código de ejemplo (si aplica)
- Capturas de pantalla de herramientas

---

## Evaluación

- [ ] Investigación completa
- [ ] Funcionamiento técnico explicado
- [ ] Mecanismos de protección cubiertos
- [ ] Riesgos identificados
- [ ] Recomendaciones prácticas
- [ ] Estructura clara
- [ ] Referencias incluidas
- [ ] Presentación profesional

