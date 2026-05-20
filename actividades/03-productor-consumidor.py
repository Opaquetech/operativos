import asyncio
import random

async def productor(q, id):
    for i in range(10):
        item = f"item-{id}-{i}"
        await q.put(item)
        print(f"[P{id}] producido: {item}")
        await asyncio.sleep(random.random())

async def consumidor(q, id):
    while True:
        item = await q.get()
        print(f"[C{id}] consumido: {item}")
        q.task_done()
        await asyncio.sleep(random.random())

async def main():
    q = asyncio.Queue()
    producers = [asyncio.create_task(productor(q, i)) for i in range(2)]
    consumers = [asyncio.create_task(consumidor(q, i)) for i in range(2)]

    await asyncio.gather(*producers)
    await q.join()
    for c in consumers:
        c.cancel()

if __name__ == '__main__':
    asyncio.run(main())
