import socket
import time

# Connect to Device1 and Device2
device1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
device2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

device1.connect(('localhost', 9001))
device2.connect(('localhost', 9002))

print("Connected to Device1 (port 9001) and Device2 (port 9002)")

def log_data(device_name, data):
    timestamp = time.ctime()
    with open("data.txt", "a") as f:
        if device_name == 'Device1':
            temp, humid, ilum = data.split(',')
            f.write(f'{timestamp}: Device1: Temp={temp}, Humid={humid}, Iilum={ilum}\n')
        elif device_name == 'Device2':
            hb, steps, cal = data.split(',')
            f.write(f'{timestamp}: Device2: Heartbeat={hb}, Steps={steps}, Cal={cal}\n')

while True:
    cmd = input("Enter 1 (Device1), 2 (Device2), or 'quit': ").strip()
    if cmd == '1':
        device1.send(b'Request')
        data = device1.recv(1024).decode()
        print('[User] Received from Device1:', data)
        log_data('Device1', data)
    elif cmd == '2':
        device2.send(b'Request')
        data = device2.recv(1024).decode()
        print('[User] Received from Device2:', data)
        log_data('Device2', data)
    elif cmd == 'quit':
        device1.send(b'quit')
        device2.send(b'quit')
        print('[User] Shutting down.')
        break
    else:
        print("Invalid input. Try again.")

device1.close()
device2.close()
