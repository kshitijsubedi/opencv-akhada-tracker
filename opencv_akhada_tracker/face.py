import numpy as np
import cv2
faceCascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
#eye_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')
#smilecascade =cv2.CascadeClassifier('haarcascades/haarcascade_smile.xml')
cap = cv2.VideoCapture(0)
while True:
    ret, img = cap.read()
    img = cv2.flip(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=5,minSize=(20, 20))
    #eyes = eye_cascade.detectMultiScale(gray)
    #smile=smilecascade.detectMultiScale(gray)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    #for (ex,ey,ew,eh) in eyes:
        #cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
   #for (xx, yy, ww, hh) in smile:
   #    cv2.rectangle(img,(xx,yy),(xx+ww,yy+hh),(0,255,0),2)
    cv2.imshow('ma haina ! ',img)
    k = cv2.waitKey(30)
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
