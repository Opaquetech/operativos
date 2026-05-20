# Tarea 4: Visualización de IPv4 en Tiempo Real (netstat)

**Fechas:** 4 de marzo de 2026 - 15 de marzo de 2026

---

## Descripción

Desarrollar un programa que lea en tiempo real las direcciones IPv4 enlazadas a la computadora usando `netstat` e implemente validación de direcciones IP con interfaz gráfica.

---

## Requisitos del Programa

### Funcionalidades Principales:
1. **Lectura en Tiempo Real:**
   - Utilizar `netstat` del sistema operativo
   - Capturar salida mediante tuberías y `os.system()`
   - Actualizar periódicamente

2. **Interfaz Gráfica:**
   - Implementar con tkinter
   - Mostrar IPs enlazadas en la computadora
   - Actualización dinámica

3. **Validación de IPs:**
   - Marcar en rojo IPs que no sean válidas
   - Usar referencia: ipblocklist
   - Indicar si una IP está bloqueada o es sospechosa

---

## Especificaciones Técnicas

**Librerías Requeridas:**
- `os`: Para ejecutar comandos del sistema
- `tkinter`: Para interfaz gráfica
- `subprocess`: Para capturar salida de netstat
- `ipaddress`: Para validación de direcciones IP

### Instalación:
```bash
pip install ipaddress  # Viene con Python 3.3+
```

---

## Estructura del Programa

```
┌──────────────────────────────────────┐
│     Interfaz Tkinter                 │
├──────────────────────────────────────┤
│ IP Local      │ Estado   │ Validación │
├──────────────────────────────────────┤
│ 192.168.1.5   │ ACTIVE   │ ✓ VÁLIDA   │
│ 10.0.0.1      │ ACTIVE   │ ✓ VÁLIDA   │
│ 192.168.1.100 │ ACTIVE   │ ✗ BLOQUEADA│
└──────────────────────────────────────┘
```

---

## Entregable

El reporte debe incluir:

- [ ] Portada del proyecto
- [ ] Documentación técnica
- [ ] Código comentado
- [ ] Capturas de corridas del programa
- [ ] Conclusiones y observaciones

---

## Validación de IPs

**Criterios:**
- Rango privado: 192.168.x.x, 10.x.x.x, 172.16-31.x.x
- IPs de loopback: 127.x.x.x
- IPs multicast: 224-239.x.x.x
- Consultar ipblocklist para IPs sospechosas

---

## Evaluación

- [ ] Lectura correcta de netstat
- [ ] Captura de tuberías del sistema
- [ ] Interfaz gráfica funcional
- [ ] Validación de IPs correcta
- [ ] Actualización en tiempo real
- [ ] Reporte completo entregado

