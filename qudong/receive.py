import socket


socket1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket2 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
HOST = "192.168.137.1"
PORT = 8010

socket1.bind((HOST, PORT))
sendAddr = ("192.168.137.2", 8008)
sendData = "100:98:81:81:150"
while True:
    socket2.sendto(sendData.encode("utf-8"), sendAddr)
    # revData = socket1.recvfrom(1024)
    # content, destInfo = revData
    # print(destInfo)



