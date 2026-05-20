# Tarea 12: Programación de Tarjetas de Vídeo (Tutorial)

**Fechas:** 24 de abril de 2026 - 1 de mayo de 2026

---

## Descripción

Crear un tutorial completo con ejemplos explicados sobre el uso de aceleración por hardware (GPU) en diferentes plataformas.

---

## Plataformas a Cubrir

### 1. NVIDIA (CUDA)
- Arquitectura CUDA
- Herramientas: NVIDIA CUDA Toolkit
- Lenguajes: C, C++, Python (PyCUDA, CuPy)
- Características principales

### 2. AMD (ROCm)
- Arquitectura RDNA/CDNA
- Herramientas: AMD ROCm
- Lenguajes: C++, Python (CuPy, JAX)
- Diferencias con CUDA

### 3. Apple (Metal)
- Metal API
- Herramientas: Metal Performance Shaders
- Lenguajes: Swift, Objective-C
- Optimización para M1/M2

### 4. Genérico (OpenCL)
- Standard abierto
- Funciona en múltiples plataformas
- Lenguaje: C
- Ventajas y limitaciones

---

## Contenido del Tutorial

### Sección 1: Introducción
- [ ] Qué es GPU Computing
- [ ] Diferencias GPU vs CPU
- [ ] Casos de uso (ML, científico, gráficos)
- [ ] Arquitectura general

### Sección 2: NVIDIA CUDA
- [ ] Instalación del toolkit
- [ ] Conceptos clave (blocks, threads, grids)
- [ ] Ejemplo 1: Suma de vectores
- [ ] Ejemplo 2: Multiplicación de matrices
- [ ] Optimizaciones comunes

### Sección 3: AMD ROCm
- [ ] Instalación de ROCm
- [ ] Diferencias con CUDA
- [ ] Ejemplo 1: Suma de vectores con HIP
- [ ] Ejemplo 2: Cálculo paralelo
- [ ] Herramientas de debugging

### Sección 4: Apple Metal
- [ ] Características de Metal
- [ ] Metal Performance Shaders
- [ ] Ejemplo: Procesamiento de imágenes
- [ ] Optimización en M1/M2

### Sección 5: OpenCL (Genérico)
- [ ] Conceptos básicos
- [ ] Instalación y setup
- [ ] Ejemplo 1: Vector addition
- [ ] Compatibilidad multiplataforma
- [ ] Ventajas para portabilidad

---

## Ejemplos Incluidos

### Ejemplo Básico: Suma de Vectores

**NVIDIA CUDA (C):**
```c
__global__ void vectorAdd(float *a, float *b, float *c, int n) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < n)
        c[i] = a[i] + b[i];
}
```

**Python (CuPy):**
```python
import cupy as cp
a = cp.arange(1000000)
b = cp.arange(1000000)
c = a + b
```

### Ejemplo Intermedio: Multiplicación de Matrices

**CUDA C++:**
- Implementación naive
- Optimización con memoria compartida
- Comparación de rendimiento

**Python (CuPy/JAX):**
```python
import jax.numpy as jnp
A = jnp.ones((1000, 1000))
B = jnp.ones((1000, 1000))
C = jnp.dot(A, B)
```

---

## Estructura del Documento

```
1. Portada y Tabla de Contenidos
2. Introducción a GPU Computing
3. Comparativa de Plataformas
   3.1 NVIDIA CUDA
   3.2 AMD ROCm
   3.3 Apple Metal
   3.4 OpenCL
4. Ejemplos Prácticos (por plataforma)
5. Benchmarks y Comparativas
6. Mejores Prácticas
7. Conclusiones
8. Referencias y Recursos
```

---

## Entregable

El tutorial debe incluir:

- [ ] Explicación de conceptos fundamentales
- [ ] Instalación paso a paso (para cada plataforma)
- [ ] Al menos 2 ejemplos por plataforma
- [ ] Código comentado y explicado
- [ ] Benchmarks de rendimiento
- [ ] Diagrama de arquitectura (Mermaid)
- [ ] Conclusiones comparativas
- [ ] Links a recursos oficiales

---

## Formato del Documento

- Formato: Markdown (.md) o PDF
- Ejemplos en bloques de código con sintaxis highlighting
- Diagramas: Usar Mermaid para arquitecturas
- Benchmarks: Incluir gráficas o tablas
- Capturas de instalación (si aplica)

---

## Evaluación

- [ ] Cobertura de las 4 plataformas
- [ ] Ejemplos claros y funcionales
- [ ] Explicaciones detalladas
- [ ] Comparativa equilibrada
- [ ] Código bien documentado
- [ ] Recursos de referencia incluidos
- [ ] Presentación profesional

