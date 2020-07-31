import numpy as np
import cv2

def empty(a):
    pass

img = cv2.imread('E:\lamborghini.jpg')
imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,480)

cv2.createTrackbar("Hue Min","TrackBars",0,255,empty)
cv2.createTrackbar("Hue Max","TrackBars",230,255,empty)
cv2.createTrackbar("Saturation Min","TrackBars",83,255,empty)
cv2.createTrackbar("Saturation Max","TrackBars",255,255,empty)
cv2.createTrackbar("Value Min","TrackBars",99,255,empty)
cv2.createTrackbar("Value Max","TrackBars",255,255,empty)

while True:
    img = cv2.imread('E:\lamborghini.jpg')
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    hueMin = cv2.getTrackbarPos("Hue Min","TrackBars")
    hueMax = cv2.getTrackbarPos("Hue Max","TrackBars")
    SaturationMin = cv2.getTrackbarPos("Saturation Min","TrackBars")
    SaturationMax = cv2.getTrackbarPos("Saturation Max","TrackBars")
    ValueMin = cv2.getTrackbarPos("Value Min","TrackBars")
    ValueMax = cv2.getTrackbarPos("Value Max","TrackBars")
    print(hueMin,SaturationMin,ValueMin)
    print(hueMax,SaturationMax,ValueMax)
    lowerb = np.array([hueMin,SaturationMin,ValueMin])
    upperb = np.array([hueMax,SaturationMax,ValueMax])
    mask = cv2.inRange(imgHSV,lowerb,upperb)
    imgResult = cv2.bitwise_and(img,img,mask=mask)

    cv2.imshow('img',img)
    cv2.imshow('imgHSV',imgHSV)
    cv2.imshow('Mask',mask)
    cv2.imshow('imgResult',imgResult)
    cv2.waitKey(1)
