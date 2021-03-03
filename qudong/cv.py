import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind("192.168.137.2",8008)
data = s.recv(1024)
print(data.decode())