import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
HOST = "192.168.137.1"
PORT = 8008
REMOTE_ADD = "192.168.137.2"
REMOTE_PORT = 8010
address = (HOST, PORT)
s.bind(address)

while True:
    s.sendto("100:098:098:099:150".encode("utf-8"), (REMOTE_ADD, REMOTE_PORT))
    time.sleep(1)
    print(s)

