# Tarea 2: MPI Suma (Mecanismos de Comunicación entre Procesos)

**Fechas:** 4 de marzo de 2026 - 11 de marzo de 2026

---

## Descripción

Realizar un programa que demuestre la comunicación entre procesos mediante MPI (Message Passing Interface) realizando operaciones de suma distribuida.

---

## Requisitos del Programa

### Flujo del Programa:
1. **Proceso 0 (Principal):**
   - Genera 10,000 números
   - Los reparte equitativamente entre cuatro procesos

2. **Procesos 1, 2, 3, 4 (Workers):**
   - Reciben su parte de los números
   - Realizan la suma de su porción
   - Envían el resultado al proceso 0

3. **Proceso 0 (Final):**
   - Recibe los resultados de cada proceso
   - Calcula la suma total
   - Muestra el resultado final

---

## Especificaciones Técnicas

**Tecnología:** MPI y mpi4py

### Instalación de Dependencias:
```bash
pip install mpi4py
```

### Distribución de Números:
- Números totales: 10,000
- Procesos workers: 4
- Números por proceso: 2,500 (aproximadamente)

---

## Estructura del Código

```
Proceso 0 → Genera números [0, 1, 2, ..., 9999]
          ↓
          → Divide en 4 partes
          ↓
          → Envía a procesos 1, 2, 3, 4
          ↓
          ← Recibe sumas parciales
          ↓
          → Calcula suma total
          ↓
          → Muestra resultado
```

---

## Evaluación

- [ ] Generación correcta de 10,000 números
- [ ] Distribución equitativa entre procesos
- [ ] Cálculo correcto de sumas parciales
- [ ] Comunicación MPI funcional
- [ ] Resultado final correcto
- [ ] Código bien documentado

---

## Notas

- Usar `mpirun` para ejecutar el programa con múltiples procesos
- Verificar que los resultados sean correctos comparando con suma total
- Documentar tiempos de ejecución

