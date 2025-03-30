import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)

msg = sock.recv(1024)
print(msg.decode())

student_id = 20201511
print(student_id)

name = 'Seungwoo Han'
sock.sendall(name.encode())

sock.close()
