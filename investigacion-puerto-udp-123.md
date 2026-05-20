# Investigación: puerto UDP 123

## 1. ¿Qué es el puerto UDP 123?
- El puerto UDP 123 es el puerto reservado por IANA para el protocolo NTP (Network Time Protocol) y variantes ligeras como SNTP (Simple NTP).
- NTP se usa para sincronizar el reloj de los equipos con servidores de tiempo confiables.
- Es un servicio de capa de aplicación que corre sobre UDP porque necesita baja latencia y no establece una conexión persistente.

## 2. Funcionamiento general del puerto 123
- NTP es un protocolo cliente-servidor.
- El cliente envía una petición al servidor NTP en UDP/123.
- El servidor responde con un paquete que incluye marcas de tiempo de origen, recepción y transmisión.
- El cliente calcula el retraso de ida y vuelta y el desplazamiento del reloj para ajustar su hora local.
- NTP puede usar modos unicast, multicast y broadcast, aunque el modo unicast es el más común en internet.
- SNTP es una versión simplificada que usa el mismo puerto y operación básica, pero sin todos los cálculos avanzados de NTP.

## 3. Documentación técnica breve
- IANA: puerto 123 UDP reservado para NTP.
- RFC 5905 describe Network Time Protocol versión 4.
- RFC 4330 describe Simple Network Time Protocol (SNTP).
- NTP usa un formato de paquete con campos como:
  - Leap Indicator
  - Version Number
  - Mode
  - Stratum
  - Poll Interval
  - Precision
  - Timestamp de referencia, origen, recepción y transmisión

## 4. Riesgos y vectores de ataque
- Por ser UDP, el puerto es susceptible a spoofing y ataques de amplificación.
- Un servidor NTP mal configurado puede ser usado en ataques DDoS mediante reflexión/envenenamiento.
- NTP puede servir información incorrecta si el servidor no es confiable.
- El tráfico NTP sin autenticar puede ser manipulado por un atacante en la red.

## 5. Mecanismos de protección por tipo de dispositivo

### Router
- Filtrado de paquetes: bloquear o permitir solo tráfico NTP a/desde servidores de tiempo autorizados.
- Firewall stateful: inspeccionar y permitir únicamente respuestas válidas de NTP.
- NAT/PAT: proteger la red interna evitando exponer servidores NTP internos al internet.
- Listas de control de acceso (ACL): permitir solo hosts o rangos IP confiables en UDP/123.
- Rate limiting: limitar la tasa de peticiones NTP para evitar abusos y ataques de amplificación.
- Proxy NTP / Relay: algunos routers ofrecen mecanismos para reenviar y controlar solicitudes hacia servidores de tiempo externos.
- NTP Authentication/Autokey/NTS: si el router soporta NTP, configurarlo con mecanismos de autenticación para verificar servidores.

### Laptop
- Firewall local: bloquear puertos no necesarios y permitir NTP solo para el servicio de tiempo del sistema.
- Servicio de tiempo: usar servicios de tiempo confiables (por ejemplo, `time.windows.com`, `pool.ntp.org`, servidores de la organización).
- Configuración de cliente:
  - En Windows: usar el servicio `Windows Time` y servidores autorizados.
  - En Linux: usar `chrony`, `ntpd` o `systemd-timesyncd` y configurar fuentes seguras.
- No ejecutar un servidor NTP en la laptop si no es necesario.
- Usar NTP seguro: si la infraestructura lo permite, habilitar NTS (Network Time Security) o autenticación basada en claves.
- Intervalos y poll: configurar el intervalo de sincronización para que no genere tráfico excesivo.
- Monitoreo y registros: revisar logs de sincronización y detección de anomalías en el tiempo.

### Celular
- Los teléfonos móviles generalmente no exponen puertos de escucha hacia el exterior.
- El sistema operativo móvil (Android/iOS) sincroniza el tiempo con servidores NTP o mediante el operador móvil.
- Protección nativa:
  - El acceso a red de las aplicaciones está controlado por el sistema.
  - El puerto UDP 123 generalmente no está abierto a conexiones entrantes.
- Los operadores móviles y los APN suelen gestionar la sincronización de tiempo desde la red interna.
- En dispositivos móviles, el riesgo principal es la confianza en el servidor de tiempo usado; por eso es importante que el OS o la operadora usen servidores verificados.
- Algunos móviles también pueden recibir información de tiempo por NITZ (Network Identity and Time Zone) vía la red celular en lugar de NTP.

### Otros dispositivos (etc.)
- Servidores: proteger NTP con firewalls, autenticación, límites de tráfico y usar servidores de tiempo internos/privados.
- IoT: muchos dispositivos IoT usan NTP para la hora; deben configurarse para usar servidores de tiempo confiables y mantenerse aislados de redes públicas.
- Equipos industriales: igual que los servidores, deben tener controles de acceso a UDP/123 y preferir sincronización interna con servidores de confianza.

## 6. Buenas prácticas generales
- Solo permitir NTP hacia/desde servidores de tiempo autorizados.
- Usar autenticación NTP cuando sea posible (NTS, Autokey, claves simétricas).
- Evitar servidores NTP públicos no confiables.
- Mantener firmware/OS actualizado para corregir vulnerabilidades de NTP.
- Monitorizar el estado de sincronización y detectar respuestas incorrectas o cambios de hora inusuales.
- Considerar alternativas seguras como PTP o servicios de tiempo basados en TLS si la infraestructura lo requiere.
