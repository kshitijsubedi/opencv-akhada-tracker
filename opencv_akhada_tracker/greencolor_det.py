import cv2
import numpy as np

lowerBound=np.array([33,80,40])
upperBound=np.array([120,255,255])

cam= cv2.VideoCapture(0)
kernelOpen=np.ones((5,5))
kernelClose=np.ones((10,10))


while True:
    ret, img1=cam.read()
    cv2.imshow("",img1)
    img=cv2.flip(img1,1)
    img=cv2.resize(img,(450,400))
    imgHSV= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(imgHSV,lowerBound,upperBound)
    
    #morphology
    kernelOpen=np.ones((5,5)) # dots haru hatuna
    kernelClose=np.ones((20,20)) # holes close garna
    maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
    maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)
    _,conts,_=cv2.findContours(maskClose,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(img,conts,-1,(0,255,70),3)
    for i in range(len(conts)):
        x,y,w,h=cv2.boundingRect(conts[i])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255), 2)
    cv2.imshow("maskClose",maskClose)
    cv2.imshow("maskOpen",maskOpen)
    cv2.imshow("mask",mask)
    cv2.imshow("cam",img)
    cv2.waitKey(10)

