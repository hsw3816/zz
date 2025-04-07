import socket

# 서버 정보
SERVER_IP = '127.0.0.1'
SERVER_PORT = 9999

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    user_input = input('Enter the message("send mboxId message" or "receive mboxId"):')
    client_socket.sendto(user_input.encode(), (SERVER_IP, SERVER_PORT))

    if user_input.lower() == 'quit':
        break

    data, _ = client_socket.recvfrom(1024)
    print(data.decode())

client_socket.close()
