import socket
import random

HOST = 'localhost'
PORT = 9002  # Device2 포트

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))          # 수신 대기 설정
server.listen(1)

print('[Device2] Waiting for connection...')
conn, addr = server.accept()
print('[Device2] Connected by', addr)

while True:
    data = conn.recv(1024).decode()
    if data == 'quit':
        print('[Device2] Quit received. Shutting down.')
        break
    elif data == 'Request':
        heartbeat = random.randint(40, 140)
        steps = random.randint(2000, 6000)
        cal = random.randint(1000, 4000)
        response = f'{heartbeat},{steps},{cal}'
        conn.send(response.encode())

conn.close()
