# -*- coding: utf-8 -*-

from email.mime import image
from sre_constants import SUCCESS
from typing import Counter
import cv2 as cv
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math
import time

cap = cv.VideoCapture(0)
detector = HandDetector(maxHands=1)
classifier = Classifier("Model/keras_model.h5", "Model/labels.txt")
offset = 20
imgSize = 300
label = ["ha", "le", "hameruha"]
# label = ["ሀ", "ለ", "ሐ"]
font_path = "fonts/absy.ttf"
font_face = cv.FONT_HERSHEY_SIMPLEX
font_scale = 1.7
font_thickness = 2

# Load the font
font = cv.imread(font_path, cv.IMREAD_UNCHANGED)


while True:
    success, frame = cap.read()
    imageOutput = frame.copy()
    hands, frame = detector.findHands(frame, draw=False)

    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']
        imgWhite = np.zeros((imgSize, imgSize, 3), np.uint8) * 255
        imgCrop = frame[y - offset:y + h + offset, x - offset:x + w + offset]
        imgCropShape = imgCrop.shape
        aspectRatio = h / w

        if aspectRatio > 1:
            k = imgSize / h
            wCalc = math.ceil(w * k)
            imgResize = cv.resize(imgCrop, (wCalc, imgSize))
            imgResizeShape = imgResize.shape
            wGap = math.ceil((imgSize - wCalc) / 2)
            imgWhite[:, wGap:wGap + wCalc] = imgResize
        else:
            k = imgSize / w
            hCalc = math.ceil(h * k)
            imgResize = cv.resize(imgCrop, (imgSize, hCalc))
            imgResizeShape = imgResize.shape
            hGap = math.ceil((imgSize - hCalc) / 2)
            imgWhite[hGap:hGap + hCalc, :] = imgResize

        prediction, index = classifier.getPrediction(imgWhite)

        cv.rectangle(imageOutput, (x - offset, y - offset), (x + w + offset, y + h + offset), (255, 0, 255), 4)
        cv.rectangle(imageOutput, (x - offset, y - offset - 50), (x - offset + 90, y - offset - 50 + 50),
                     (255, 0, 255), cv.FILLED)
        # cv.putText(imageOutput, label[index], (x - offset + 10, y - offset - 20), cv.FONT_HERSHEY_COMPLEX, 1.7,
        #            (255, 255, 255), 2)
        cv.putText(imageOutput, label[index], (x - offset + 10, y - offset - 20), font, font_scale, (255, 255, 255), font_thickness, cv.LINE_AA)

        cv.imshow('ImageCrop', imgCrop)
        cv.imshow('ImageWhite', imgWhite)

    cv.imshow('frame', imageOutput)
    key = cv.waitKey(1)
    if key == ord('q'):
        break
