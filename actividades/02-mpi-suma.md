# Actividad 02 — MPI Suma (mpi4py)

**Fechas:** 4-11 marzo 2026

## Descripción
Implementar un programa distribuido con MPI (mpi4py) donde el proceso 0 genera 10,000 números, los reparte entre 4 procesos, cada proceso suma su parte y el proceso 0 reúne los resultados.

## Instrucciones
- Usar `mpi4py`.
- Ejecutar con `mpirun -n 4 python3 mpi_suma.py`.

## Código sugerido (al final del documento según solicitud):

```python
# Archivo: mpi_suma.py
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

N = 10000

if rank == 0:
    # generar datos y repartir
    data = list(range(N))
    chunk_size = N // size
    for i in range(1, size):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i != size - 1 else N
        comm.send(data[start:end], dest=i)
    # calcular su propia parte
    my_chunk = data[0:chunk_size]
else:
    my_chunk = comm.recv(source=0)

partial_sum = sum(my_chunk)

# recolectar resultados
sums = comm.gather(partial_sum, root=0)

if rank == 0:
    total = sum(sums)
    print(f"Suma total: {total}")
```

## Entrega
- `mpi_suma.py` en la carpeta de actividad.
- Breve explicación del reparto y ejecución.

---
