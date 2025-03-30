import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', 9000))
s.listen(1)

while True:
    client, addr = s.accept()
    print('Connection from', addr)

    client.sendall(f"Hello {addr[0]}".encode())

    name = client.recv(1024).decode()
    print(name)

    client.close()
