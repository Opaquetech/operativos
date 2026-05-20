# Tarea 6: Ejecución de Comandos Bash vía aiohttp

**Fechas:** 4 de marzo de 2026 - 30 de marzo de 2026

---

## Descripción

Desarrollar una aplicación web asincrónica que permita ejecutar comandos bash remotamente a través de HTTP utilizando el framework aiohttp.

---

## Requisitos del Programa

### Arquitectura:
- **Servidor Web:** aiohttp
- **Ejecutor de Comandos:** os.system() o subprocess
- **Comunicación:** Peticiones HTTP GET/POST

### Funcionalidades:
1. Servidor aiohttp que escucha peticiones HTTP
2. Recibe comandos bash como parámetros
3. Ejecuta los comandos en el servidor
4. Retorna resultados al cliente
5. Manejo de errores y excepciones

---

## Especificaciones Técnicas

**Librerías Requeridas:**
- `aiohttp`: Framework web asincrónico
- `os` o `subprocess`: Ejecución de comandos
- `asyncio`: Programación asincrónica

### Instalación:
```bash
pip install aiohttp
```

---

## Estructura Esperada

### Servidor:
```
http://localhost:8080/execute?cmd=ls
http://localhost:8080/execute?cmd=whoami
http://localhost:8080/execute?cmd=df
```

### Cliente (ejemplo):
```python
import aiohttp
import asyncio

async def execute_command(cmd):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'http://localhost:8080/execute?cmd={cmd}') as resp:
            return await resp.text()
```

---

## Seguridad

### Consideraciones Importantes:
- ⚠️ Validar y sanitizar comandos
- ⚠️ Limitar lista de comandos permitidos (whitelist)
- ⚠️ No permitir caracteres peligrosos
- ⚠️ Usar autenticación (opcional)
- ⚠️ Logging de comandos ejecutados

---

## Endpoints Esperados

| Endpoint | Método | Parámetro | Descripción |
|----------|--------|-----------|-------------|
| `/execute` | GET/POST | cmd | Ejecuta comando bash |
| `/health` | GET | - | Verifica estado del servidor |
| `/info` | GET | - | Información del servidor |

---

## Evaluación

- [ ] Servidor aiohttp funcional
- [ ] Aceptación de comandos bash
- [ ] Ejecución correcta de comandos
- [ ] Retorno de resultados al cliente
- [ ] Manejo de errores
- [ ] Seguridad en validación de comandos
- [ ] Documentación completa

