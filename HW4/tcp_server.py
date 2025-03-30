import socket
import re

HOST = ''
PORT = 9999

def calculate(expr):
    expr = expr.replace(" ", "")
    match = re.match(r'(-?\d+)([+\-*/])(-?\d+)', expr)
    if not match:
        return "잘못된 입력입니다."

    a, op, b = match.groups()
    a, b = int(a), int(b)

    try:
        if op == '+':
            return str(a + b)
        elif op == '-':
            return str(a - b)
        elif op == '*':
            return str(a * b)
        elif op == '/':
            return "{:.1f}".format(a / b)
        else:
            return "지원하지 않는 연산자입니다."
    except Exception as e:
        return f"오류: {e}"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen()

    print(f"서버가 {PORT}번 포트에서 대기 중...")

    while True:
        conn, addr = s.accept()
        with conn:
            print(f"{addr}에서 연결됨")
            expr = conn.recv(1024).decode()
            result = calculate(expr)
            conn.sendall(result.encode())
