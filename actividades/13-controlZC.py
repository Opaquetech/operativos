import threading
import time

counter = 0
lock = threading.Lock()

def demo_mutex():
    def worker(i):
        global counter
        print(f"[Hilo {i}] Esperando acceso...")
        with lock:
            print(f"[Hilo {i}] SECCIÓN CRÍTICA (inicio)")
            tmp = counter
            time.sleep(0.1)
            tmp += 1
            counter = tmp
            print(f"[Hilo {i}] SECCIÓN CRÍTICA (fin) -> {counter}")
        print(f"[Hilo {i}] Salió")
    threads = [threading.Thread(target=worker, args=(i,)) for i in range(4)]
    for t in threads: t.start()
    for t in threads: t.join()

if __name__ == '__main__':
    demo_mutex()
