import numpy as np
import cv2 as cv
import imutils
import time
import datetime

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from PIL import Image
import os
import io

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

motionCounter = 0
count = 0

cap = cv.VideoCapture(0)
if not cap.isOpened():
    
    print("Cannot open camera")
    exit()

avg = None
    
while True:
    
    ret, frame = cap.read()
    
    if not ret:
        print("Can't recieve a frame")
        break

    text = "No Movement" + " " + time.asctime()

    frame = imutils.resize(frame, width=800)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    gray = cv.GaussianBlur(gray, (21,21), 0)

    if avg is None:
        avg = gray.copy().astype("float")
        continue

    cv.accumulateWeighted(gray, avg, 0.2)
    frameDelta = cv.absdiff(gray, cv.convertScaleAbs(avg))
    thresh = cv.threshold(frameDelta, 25, 255, cv.THRESH_BINARY) [1]

    thresh = cv.dilate(thresh, None, iterations=1)
    cnts = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    for c in cnts:
        if cv.contourArea(c) < 500:
            continue
        
        (x,y,w,h) = cv.boundingRect(c)
        cv.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
        text = "Movement" + " " + time.asctime()
        cv.putText(frame, text, (10,20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)
        
        motionCounter +=1

        if motionCounter >= 10:
            count += 1
            title = "Snapshot " + "Day " + str(time.localtime()[2]) + " Hour " + str(time.localtime()[3]) + " Minute " + str(time.localtime()[4]) + " Second " + str(time.localtime()[5]) + ".jpg"
            cv.imwrite("tmp.jpg", frame)
            file1 = drive.CreateFile({'title': title, 'mimeType':'image/jpeg'})
            file1.SetContentFile("tmp.jpg")
            file1.Upload()
            #cv.imwrite("Snapshot " + "Day " + str(time.localtime()[2]) + " Hour " + str(time.localtime()[3]) + " Minute " + str(time.localtime()[4]) + " Second " + str(time.localtime()[5]) + ".jpg", frame)
            motionCounter = 0

        

    if len(cnts) < 1:
        cv.putText(frame, text, (10,20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
    
    cv.imshow('Feed', frame)
    cv.imshow('Threshold', thresh)
    cv.imshow('Delta', frameDelta)
    
    if cv.waitKey(1) == ord('q'):
        break
    
cap.release()
cv.destroyAllWindows()
