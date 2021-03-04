# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 18:41:33 2018
#QQ群：476842922（欢迎加群讨论学习
@author: Administrator
"""
#以下是最常用的读取视频流的方法
import cv2
import numpy as np
lower_red = np.array([170, 100, 100])
upper_red = np.array([179, 255, 255])
url = 'http://192.168.137.2:8081//'#根据摄像头设置IP及rtsp端口
cap = cv2.VideoCapture(url)#读取视频流
while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_red, upper_red)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    cnts, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Display the resulting frame
    cv2.imshow('mask',mask)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
