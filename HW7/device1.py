import socket
import random

HOST = 'localhost'
PORT = 9001

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print('[Device1] Waiting for connection...')
conn, addr = server.accept()
print('[Device1] Connected by', addr)

while True:
    data = conn.recv(1024).decode()
    if data == 'quit':
        print('[Device1] Quit received. Shutting down.')
        break
    elif data == 'Request':
        temp = random.randint(0, 40)
        humid = random.randint(0, 100)
        ilum = random.randint(70, 150)
        response = f'{temp},{humid},{ilum}'
        conn.send(response.encode())

conn.close()
