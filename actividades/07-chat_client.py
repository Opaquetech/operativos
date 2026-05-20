import socket
import threading

HOST = '127.0.0.1'
PORT = 5000

def recv_loop(s):
    while True:
        data = s.recv(4096)
        if not data:
            break
        print(data.decode(), end='')

def main():
    name = input('Nombre: ')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall((name+'\n').encode())
    threading.Thread(target=recv_loop, args=(s,), daemon=True).start()
    try:
        while True:
            msg = input()
            if msg.lower() in ('/quit','/exit'):
                break
            s.sendall(msg.encode())
    finally:
        s.close()

if __name__ == '__main__':
    main()
