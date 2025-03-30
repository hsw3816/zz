import socket

HOST = 'localhost'
PORT = 9999

while True:
    expr = input("계산식 입력 (예: 20 + 17) 또는 q: ")

    if expr.lower() == 'q':
        print("프로그램을 종료합니다.")
        break

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(expr.encode())
        result = s.recv(1024).decode()
        print("결과:", result)
