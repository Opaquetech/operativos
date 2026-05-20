# Tarea 5: Visualización de URLs en Tiempo Real (netstat)

**Fechas:** 4 de marzo de 2026 - 23 de marzo de 2026

---

## Descripción

Programa similar al de visualización de IPs, pero enfocado en extraer y validar URLs que se conectan desde la computadora en tiempo real usando `netstat`.

---

## Requisitos del Programa

### Funcionalidades Principales:
1. **Extracción de URLs:**
   - Leer salida de `netstat` en tiempo real
   - Extraer direcciones remotas (URLs/dominios)
   - Parsear direcciones IP a nombres de dominio (si es posible)

2. **Interfaz Gráfica:**
   - Implementar con tkinter
   - Mostrar URLs/dominios conectados
   - Actualización dinámica en tiempo real

3. **Validación de URLs:**
   - Resaltar en rojo URLs no válidas
   - Consultar blacklists conocidas
   - Indicar URLs sospechosas o potencialmente maliciosas
   - Usar referencia: listas de blacklists públicas

---

## Especificaciones Técnicas

**Librerías Requeridas:**
- `os`: Ejecución de comandos
- `tkinter`: Interfaz gráfica
- `subprocess`: Captura de salida
- `socket`: Resolución de dominios
- `urllib`: Validación de URLs (opcional)
- `requests`: Para validar URLs (opcional)

### Instalación:
```bash
pip install requests
```

---

## Estructura del Programa

```
┌──────────────────────────────────────────┐
│     Interfaz Tkinter - URLs              │
├──────────────────────────────────────────┤
│ URL/Dominio       │ Estado   │ Validación │
├──────────────────────────────────────────┤
│ google.com        │ ACTIVE   │ ✓ VÁLIDA   │
│ github.com        │ ACTIVE   │ ✓ VÁLIDA   │
│ malicious.xyz     │ ACTIVE   │ ✗ BLOQUEADA│
│ 142.251.32.142    │ ACTIVE   │ ?          │
└──────────────────────────────────────────┘
```

---

## Extracción de URLs desde netstat

**Proceso:**
1. Ejecutar `netstat -n` o `netstat -b` (con procesos)
2. Parsear las conexiones remotas
3. Intentar resolución inversa (IP → dominio)
4. Validar cada URL/dominio

---

## Validación de URLs

**Criterios:**
- Validar formato de URL
- Consultar listas negras conocidas
- Verificar certificados SSL (si aplica)
- Detectar patrones sospechosos

**Blacklists de referencia:**
- PhishTank
- URLhaus
- Google Safe Browsing
- Listas comunitarias

---

## Entregable

El reporte debe incluir:

- [ ] Portada del proyecto
- [ ] Documentación técnica
- [ ] Código comentado y explicado
- [ ] Capturas de corridas
- [ ] Análisis de URLs detectadas
- [ ] Conclusiones

---

## Evaluación

- [ ] Extracción correcta de URLs desde netstat
- [ ] Resolución de dominios funcional
- [ ] Interfaz gráfica clara y actualizada
- [ ] Validación de URLs correcta
- [ ] Identificación de URLs sospechosas
- [ ] Reporte profesional entregado

