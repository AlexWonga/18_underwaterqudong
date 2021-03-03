
import cv2
import numpy as np

url = 'http://192.168.137.2:8081//'#根据摄像头设置IP及rtsp端口
cap = cv2.VideoCapture(url)#读取视频流
lower_blue = np.array([90, 110, 110])
upper_blue = np.array([140, 255, 255])
lower_red = np.array([170,100,100])
upper_red = np.array([179,255,255])

while (cap.isOpened()):
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_red, upper_red)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None,iterations=2)
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    # res = cv2.bitwise_and(frame, frame, mask=mask)
    # cnt = cv2.findContours(mask.)
    # cv2.imshow("frame",frame)
    # cv2.imshow('mask',mask)
    # cv2.imshow('res',res)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

