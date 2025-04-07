import socket

mailboxes = {}

HOST = '127.0.0.1'
PORT = 9999

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))
print(f"UDP 서버가 {HOST}:{PORT}에서 대기 중입니다.")

while True:
    data, addr = server_socket.recvfrom(1024)
    message = data.decode().strip()

    if message.lower() == 'quit':
        print("클라이언트 종료 요청. 서버 종료.")
        break

    if message.startswith("send "):
        try:
            _, mbox_id, *msg_parts = message.split()
            msg = " ".join(msg_parts)
            if mbox_id not in mailboxes:
                mailboxes[mbox_id] = []
            mailboxes[mbox_id].append(msg)
            server_socket.sendto("OK".encode(), addr)
        except Exception as e:
            server_socket.sendto(f"Error: {e}".encode(), addr)

    elif message.startswith("receive "):
        _, mbox_id = message.split()
        if mbox_id in mailboxes and mailboxes[mbox_id]:
            msg = mailboxes[mbox_id].pop(0)
            server_socket.sendto(msg.encode(), addr)
        else:
            server_socket.sendto("No messages".encode(), addr)

    else:
        server_socket.sendto("Invalid command".encode(), addr)

server_socket.close()
