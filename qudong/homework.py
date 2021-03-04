import cv2
import numpy as np
import socket
import time

socket1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sendAddr = ("192.168.137.2", 8008)
f = "115:81:99:98:150"
b = "81:115:99:98:150"
r = "115:115:99:98:150"
l = "81:81:99:98:150"
url = 'http://192.168.137.2:8081//'  # 根据摄像头设置IP及rtsp端口
cap = cv2.VideoCapture(url)  # 读取视频流
lower_blue = np.array([90, 110, 110])
upper_blue = np.array([140, 255, 255])
lower_red = np.array([0, 43, 46])
upper_red = np.array([10, 255, 255])
lower_green = np.array([58,43,46])
upper_green = np.array([77,255,255])
lower_yellow = np.array([30,43,46])
upper_yellow = np.array([36,255,255])

while (cap.isOpened()):
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    cnts, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    center = None
    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        print(x, y)
        if x < 300:
            socket1.sendto(l.encode("utf-8"), sendAddr)
        elif x > 500:
            socket1.sendto(r.encode("utf-8"), sendAddr)
        else:
            socket1.sendto(f.encode("utf-8"), sendAddr)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
