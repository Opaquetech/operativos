import socket
import threading

HOST = '0.0.0.0'
PORT = 5000

clients = []

def handle_client(conn, addr):
    with conn:
        name = conn.recv(1024).decode().strip()
        broadcast(f"[SERVER] {name} se ha conectado.\n")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            msg = data.decode().strip()
            broadcast(f"[{name}] {msg}\n")
        broadcast(f"[SERVER] {name} se ha desconectado.\n")

def broadcast(message):
    for c in clients:
        try:
            c.sendall(message.encode())
        except Exception:
            pass

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()
    print(f"Servidor chat escuchando en {HOST}:{PORT}")
    try:
        while True:
            conn, addr = s.accept()
            clients.append(conn)
            threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()
    finally:
        s.close()

if __name__ == '__main__':
    main()
