
from picamera.array import PiRGBArray
from picamera import PiCamera
import RPi.GPIO as GPIO
import time
import cv2
import numpy as np

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
  
#Image analysis aba

def segment_colour(frame): 
    hsv_roi =  cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask_1 = cv2.inRange(hsv_roi, np.array([160, 160,10]), np.array([190,255,255]))
    ycr_roi=cv2.cvtColor(frame,cv2.COLOR_BGR2YCrCb)
    mask_2=cv2.inRange(ycr_roi, np.array((0.,165.,0.)), np.array((255.,255.,255.)))
    mask = mask_1 | mask_2
    kern_dilate = np.ones((8,8),np.uint8)
    kern_erode  = np.ones((3,3),np.uint8)
    mask= cv2.erode(mask,kern_erode)      #Eroding
    mask=cv2.dilate(mask,kern_dilate)     #Dilating
    cv2.imshow('mask',mask)
    return mask   #rato color ko mask send garni

def find_blob(blob):
    largest_contour=0
    cont_index=0
    _,contours, hierarchy = cv2.findContours(blob, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    for idx, contour in enumerate(contours):
        area=cv2.contourArea(contour)
        if (area >largest_contour) :
            largest_contour=area
            cont_index=idx              
    r=(0,0,0,0)
    if len(contours) > 2:
        r = cv2.boundingRect(contours[cont_index])
    return r,largest_contour

camera = PiCamera()
camera.resolution = (160, 120)
camera.framerate = 16
rawCapture = PiRGBArray(camera, size=(160, 120))
time.sleep(0.001)
 
# aba image anlaysis kam
for image in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
      frame = image.array
      frame=cv2.flip(frame,1)
      hsv1 = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
      mask_red=segment_colour(frame)      #masking garnu paro red color ya bata
      loct,area=find_blob(mask_red)
      x,y,w,h=loct     
      if (w*h) < 10:  #area kati rakhni ta??
            found=0
      else:
            found=1
            simg2 = cv2.rectangle(frame, (x,y), (x+w,y+h), 255,2)
      flag=0
      #GPIO.output(LED_PIN,GPIO.LOW)   
      if(found==0):   
            print("vetena")        # aba opponent vetena re kata jani ta rotate garu paro ni
            #if flag==0:
            #      rightturn()
            #      time.sleep(0.05)
            #else:
            #      leftturn()
            #      time.sleep(0.05)
            #rotate()
            #time.sleep(0.0125)
    
      elif(found==1):
            print("vetyo")
            



      cv2.imshow("draw",frame)    
      rawCapture.truncate(0)  # arko frame ko lagi clear frame lastai lang garo yesle garda 
      if(cv2.waitKey(1) & 0xff == ord('q')):
            break

GPIO.cleanup()
