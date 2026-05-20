from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

N = 10000

if rank == 0:
    data = list(range(N))
    chunk_size = N // size
    for i in range(1, size):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i != size - 1 else N
        comm.send(data[start:end], dest=i)
    my_chunk = data[0:chunk_size]
else:
    my_chunk = comm.recv(source=0)

partial_sum = sum(my_chunk)

sums = comm.gather(partial_sum, root=0)

if rank == 0:
    total = sum(sums)
    print(f"Suma total: {total}")
