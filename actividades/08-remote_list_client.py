import socket
import json

HOST = '127.0.0.1'
PORT = 5001

def request(path):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall(f'REQUEST:{path}'.encode())
    data = s.recv(65536)
    s.close()
    try:
        return json.loads(data.decode())
    except Exception:
        return data.decode()

if __name__ == '__main__':
    path = input('Ruta relativa desde home (ej: /): ')
    res = request(path)
    print(res)
