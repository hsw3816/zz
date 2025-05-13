import socket
import threading
import time

clients = []

def handle_client(conn, addr):
    try:
        id_data = conn.recv(1024)
        client_id = id_data.decode().strip()

        print(f"new client {addr}: {client_id}")

        clients.append(conn)

        while True:
            data = conn.recv(1024)
            if not data:
                break

            message = data.decode()

            if 'quit' in message:
                print(f"{addr} exited")
                break

            print(time.asctime(), f"{addr}:", message)

            for client in clients:
                if client != conn:
                    client.sendall(data)

    except:
        pass
    finally:
        conn.close()
        if conn in clients:
            clients.remove(conn)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 2500))
s.listen()

print('Server Started')

while True:
    conn, addr = s.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.daemon = True
    thread.start()
