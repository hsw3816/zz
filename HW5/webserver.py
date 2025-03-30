from socket import *
import os

# 서버 생성
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('', 80))
s.listen(10)

print("웹 서버 실행 중... (http://127.0.0.1/)")

while True:
    c, addr = s.accept()
    data = c.recv(1024)
    msg = data.decode(errors='ignore')
    req = msg.split('\r\n')
    
    if len(req) < 1:
        c.close()
        continue

    print(f"[요청 from {addr}] {req[0]}")
    request_line = req[0]
    
    try:
        filename = request_line.split()[1][1:]  # /index.html → index.html
    except:
        c.close()
        continue

    if filename == '':
        filename = 'index.html'

    if not os.path.exists(filename):
        response = 'HTTP/1.1 404 Not Found\r\n\r\n'
        response += '<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>'
        response += '<BODY>Not Found</BODY></HTML>'
        c.send(response.encode('euc-kr'))
    else:
        if filename.endswith('.html'):
            mimeType = 'text/html'
            with open(filename, 'r', encoding='utf-8') as f:
                data = f.read()
            header = 'HTTP/1.1 200 OK\r\n'
            header += 'Content-Type: ' + mimeType + '\r\n'
            header += '\r\n'
            c.send(header.encode())
            c.send(data.encode('utf-8'))

        elif filename.endswith('.png'):
            mimeType = 'image/png'
            with open(filename, 'rb') as f:
                data = f.read()
            header = 'HTTP/1.1 200 OK\r\n'
            header += 'Content-Type: ' + mimeType + '\r\n'
            header += '\r\n'
            c.send(header.encode())
            c.send(data)

        elif filename.endswith('.ico'):
            mimeType = 'image/x-icon'
            with open(filename, 'rb') as f:
                data = f.read()
            header = 'HTTP/1.1 200 OK\r\n'
            header += 'Content-Type: ' + mimeType + '\r\n'
            header += '\r\n'
            c.send(header.encode())
            c.send(data)
        else:
            response = 'HTTP/1.1 404 Not Found\r\n\r\n'
            response += '<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>'
            response += '<BODY>Not Found</BODY></HTML>'
            c.send(response.encode('euc-kr'))

    c.close()
