import socket
import threading
import os
import json

HOST = '0.0.0.0'
PORT = 5001
BASE_DIR = os.path.expanduser('~')  # restrict to home directory by default

def handle_client(conn, addr):
    with conn:
        data = conn.recv(4096).decode().strip()
        if not data.startswith('REQUEST:'):
            conn.sendall(b'ERROR: Invalid request')
            return
        path = data[len('REQUEST:'):]
        full = os.path.abspath(os.path.join(BASE_DIR, path.lstrip('/')))
        if not full.startswith(BASE_DIR):
            conn.sendall(b'ERROR: Access denied')
            return
        if not os.path.exists(full):
            conn.sendall(b'ERROR: Not found')
            return
        entries = []
        for name in os.listdir(full):
            p = os.path.join(full, name)
            entries.append({
                'name': name,
                'is_dir': os.path.isdir(p),
                'size': os.path.getsize(p) if os.path.isfile(p) else None
            })
        conn.sendall(json.dumps(entries).encode())

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()
    print(f'Remote list server running on {HOST}:{PORT}')
    try:
        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()
    finally:
        s.close()

if __name__ == '__main__':
    main()
