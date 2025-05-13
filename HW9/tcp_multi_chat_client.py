import socket
import threading

def receive(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                break
            print(data.decode())
        except:
            break

svr_addr = ('localhost', 2500)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(svr_addr)

my_id = input('ID를 입력하세요: ')
sock.sendall(f"[{my_id}]".encode())

thread = threading.Thread(target=receive, args=(sock,))
thread.daemon = True
thread.start()

while True:
    msg = input()
    if msg == 'quit':
        sock.sendall(msg.encode())
        break
    sock.sendall(f"[{my_id}] {msg}".encode())
