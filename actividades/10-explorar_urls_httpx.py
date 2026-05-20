import asyncio
import httpx

async def fetch(client, url, sem):
    async with sem:
        try:
            r = await client.get(url, timeout=10.0)
            return url, r.status_code, r.elapsed.total_seconds()
        except Exception as e:
            return url, 'ERROR', str(e)

async def main():
    urls = []
    try:
        with open('URLs.txt') as f:
            urls = [l.strip() for l in f if l.strip()]
    except FileNotFoundError:
        print('URLs.txt no encontrado')
        return
    sem = asyncio.Semaphore(5)
    async with httpx.AsyncClient() as client:
        tasks = [fetch(client, u, sem) for u in urls]
        results = await asyncio.gather(*tasks)
        for r in results:
            print(r)

if __name__ == '__main__':
    asyncio.run(main())
