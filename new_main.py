
from picamera.array import PiRGBArray
from picamera import PiCamera
import RPi.GPIO as GPIO
import time
import cv2
import numpy as np



GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
iflag=1






cc=13
GPIO.setup(cc,GPIO.OUT)
GPIO.output(cc,True)



x=1
motor1=3
motor11=5
motor2=7
motor22=11

GPIO.setup(motor1,GPIO.OUT)

GPIO.setup(motor2,GPIO.OUT)

GPIO.setup(motor11,GPIO.OUT)

GPIO.setup(motor22,GPIO.OUT)



def forward(tf):
    GPIO.output(motor1, True)
    GPIO.output(motor2, True)
    GPIO.output(motor11,False)
    GPIO.output(motor22,False)
    print("for")
    time.sleep(tf)

def reverse(tf):
    GPIO.output(motor1, False)
    GPIO.output(motor2, False)
    GPIO.output(motor11,True)
    GPIO.output(motor22,True)
    print("rev")
    time.sleep(tf)

def search(tf):
      if (x%3 ==1 ):

            GPIO.output(motor1, True)
            GPIO.output(motor2, False)
            GPIO.output(motor11,False)
            GPIO.output(motor22,True)
            x++
            time.sleep(tf)
      if (x%3==2):
             GPIO.output(motor1, True)
            GPIO.output(motor2, True)
            GPIO.output(motor11,False)
            GPIO.output(motor22,False)
            x++
            time.sleep(tf)
      if(x%3==0):
             GPIO.output(motor1, False)
            GPIO.output(motor2, True)
            GPIO.output(motor11,True)
            GPIO.output(motor22,False)
            x++
            time.sleep(tf)
      print("search")
      time.sleep(tf)
    
def irotate(tf):
      GPIO.output(motor1, True)
      GPIO.output(motor2, False)
      GPIO.output(motor11,False)
      GPIO.output(motor22,True)
      print("irotate")
      time.sleep(tf)
      
def right(tf):
    GPIO.output(motor1, False)
    GPIO.output(motor2, True)
    GPIO.output(motor11,True)
    GPIO.output(motor22,False)
    print("right")
    time.sleep(tf)
def left(tf):
      GPIO.output(motor1, True)
      GPIO.output(motor2, False)
      GPIO.output(motor11,False)
      GPIO.output(motor22,True)
      print("left")
      time.sleep(tf)












##############################
############################



def segment_redcolour(frame): 
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
camera.resolution = (640, 480)
camera.framerate = 16
rawCapture = PiRGBArray(camera, size=(640, 480))
time.sleep(0.001)
if(iflag==1):
      irotate(0.5)
      iflag=0

# aba image anlaysis kam
for image in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
      frame = image.array
      frame=cv2.flip(frame,1)
      hsv1 = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

      mask_red=segment_redcolour(frame)      #masking garnu paro red color ya bata
      loct,area=find_blob(mask_red)
      x,y,w,h=loct 

      if (w*h) < 10:  #area kati rakhni ta??
            found=0
      else:
            found=1
            simg2 = cv2.rectangle(frame, (x,y), (x+w,y+h), 255,2)
      #GPIO.output(LED_PIN,GPIO.LOW)  
      if(found==0):   
            print("vetena") 
            search(1)
    
      elif(found==1):
            print("vetyo")
            if(x<215):
                  left(0.3)
            if(x>430):
                  right(0.3)
            else:
                  forward(0.3)

      cv2.imshow("draw",frame)    
      rawCapture.truncate(0)  # arko frame ko lagi clear frame lastai lang garo yesle garda 
      if(cv2.waitKey(1) & 0xff == ord('q')):
            break

GPIO.cleanup()

