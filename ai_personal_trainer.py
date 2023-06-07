import cv2
import time
import os
import pose_module as pm
import numpy as np

cap = cv2.VideoCapture('video/1.mp4')
detector = pm.poseDetector()
count = 0
dir = 0
pTime = 0

while True:
    success, img = cap.read()
    # img = cv2.resize(img, (1290, 720))
    # img = cv2.imread('image/1.jpg')
    img = detector.findPose(img, False)
    lmList = detector.getPosition(img, False)
    if isinstance(len(lmList), int):
        # # Right arm
        # detector.findAngle(img,12, 14, 16)
        # Left arm
        angle = detector.findAngle(img,11, 13, 15)
        per = np.interp(angle, (210, 305), (0, 100))
        bar = np.interp(angle, (210, 305), (3200, 1000))
        # print(angle, per) 

        # Check for the dumbbell curls
        color = (255, 0, 255)
        if per == 100:
            color = (0, 255, 0)
            if dir == 0:
                count += 0.5
                dir = 1
        if per == 0:
            if dir == 1:
                count += 0.5
                dir = 0
            
        cv2.rectangle(img, (70, 1000), (170, 3200), color, 2)
        cv2.rectangle(img, (70, int(bar)), (170, 3200), color, cv2.FILLED)
        # Rectangle behind count
        cv2.rectangle(img, (50, 3325), (200, 3500), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, f'{int(per)} %', (50, 900), cv2.FONT_HERSHEY_PLAIN, 10,
                    color,15)
        
        cv2.putText(img, f'{int(count)}', (50, 3500), cv2.FONT_HERSHEY_PLAIN, 15,
                    (255,0,0),20)
    
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (50, 200), cv2.FONT_HERSHEY_PLAIN, 10,
                (0, 0, 255),20)
    
    cv2.namedWindow('custom window', cv2.WINDOW_KEEPRATIO)
    cv2.imshow('custom window', img)
    key = cv2.waitKey(1)
    if key > 0:
        break
