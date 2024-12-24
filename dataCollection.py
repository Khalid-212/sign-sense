from typing import Counter
import cv2 as cv
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import time

cap = cv.VideoCapture(0)
detector = HandDetector()
offset = 30
imgSize = 300
folder = "data/መ"
counter = 0

while True:
    ret, frame = cap.read()
    hands, frame = detector.findHands(frame)

    if hands:
        hands= hands[0]
        x,y,w,h = hands['bbox']
        imgWhite = np.zeros((imgSize,imgSize,3),np.uint8)*255
        imgCrop = frame[y-offset:y+h+offset,x-offset:x+w+offset]
        imgCropShape = imgCrop.shape
        aspectRatio = h/w
        
        if aspectRatio > 1:
            k=imgSize/h
            wCalc = math.ceil(w*k)
            imgResize = cv.resize(imgCrop,(wCalc,imgSize))
            imgResizeShape = imgResize.shape
            wGap = math.ceil((imgSize-wCalc)/2)
            imgWhite[:,wGap:wGap+wCalc] = imgResize

        else:
            k=imgSize/w
            hCalc = math.ceil(h*k)
            imgResize = cv.resize(imgCrop,(imgSize,hCalc))
            imgResizeShape = imgResize.shape
            hGap = math.ceil((imgSize-hCalc)/2)
            imgWhite[hGap:hGap+hCalc,:] = imgResize
            
        
        cv.imshow('Image',imgCrop)
        cv.imshow('ImageWhite',imgWhite)

    cv.imshow('frame', frame)
    key  = cv.waitKey(1)
    if key == (ord('s')):
        counter +=1
        cv.imwrite(f'{folder}/image_{time.time()}.jpg',imgWhite)
        print(counter)
    elif key == (ord('q')):
        break