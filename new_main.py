
from picamera.array import PiRGBArray
from picamera import PiCamera
import RPi.GPIO as GPIO
import time
import cv2
import numpy as np



GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
iflag=1


ir1=11
ir2=12
ir3=13
ir4=15
GPIO.setup(ir1,GPIO.IN)
GPIO.setup(ir2,GPIO.IN)
GPIO.setup(ir3,GPIO.IN)
GPIO.setup(ir4,GPIO.IN)






motor1=37
motor11=36
motor2=31
motor22=32


GPIO.setup(motor1,GPIO.OUT)

GPIO.setup(motor2,GPIO.OUT)

GPIO.setup(motor11,GPIO.OUT)

GPIO.setup(motor22,GPIO.OUT)



def forward(tim):
    GPIO.output(motor1, 1)
    GPIO.output(motor2, 1)
    GPIO.output(motor11,0)
    GPIO.output(motor22,0)
    print("for")
    time.sleep(tim)
    
def reverse(tim):
    GPIO.output(motor1, False)
    GPIO.output(motor2, False)
    GPIO.output(motor11,True)
    GPIO.output(motor22,True)
    print("rev")
    time.sleep(tim)

def right(tim):
    GPIO.output(motor1, 0)
    GPIO.output(motor2, 1)
    GPIO.output(motor11,1)
    GPIO.output(motor22,0)
    print("right")
    time.sleep(tim)
    
def left(tim):
      GPIO.output(motor1, 1)
      GPIO.output(motor2, 0)
      GPIO.output(motor11,0)
      GPIO.output(motor22,1)
      print("left")
      time.sleep(tim)
      

def stop(tim):
      GPIO.output(motor1, 0)
      GPIO.output(motor2, 0)
      GPIO.output(motor11,0)
      GPIO.output(motor22,0)
      print("stop")
      time.sleep(tim)
    

def search():
      global xxx
      if (xxx == 1):
            left(0.1)
            print("search_left")
             
      if(xxx==2):
            
            forward(0.1)
            print("search_Forward")    
        
      if (xxx==3):
            right(0.1)
            print("search_Right")
           

      if(xxx==4):
            
            forward(0.1)
            print("search_Forward")    
            xxx = 1
           
            
      xxx=xxx+1
      
    
def checkir():
    print(".....")
    print(ir11)
    print(ir22)
    print(ir33)
    print(ir44)
    if(ir11>0 and ir22>0 and ir33>0 and ir44>0):
        left(0)
        print("ir .........left sabai ir ")
    if(ir11>0 and ir22>0):
        right(0.3)
        print("ir .........right 1 ra 2 ")
    if(ir22>0 and ir33>0):
        forward(0.3)
        print("ir .........forward 2 ra 3 ")
    if(ir33>0 and ir44>0):
        left(0.3)
        print("ir .........left 3 ra 4 ")
    if(ir11>0 and ir44>0):
        reverse(0.3)
        print("ir .........reverse 1 ra 4")
    if(ir11>0):
        right(0.3)
        print("ir .........right ")
        print("ir11 matrai")
        
    if(ir22>0):
        forward(0.3)
        print("ir .........forward ")
        print("ir22 atrai ")
    if(ir33>0):
        forward(0.3)
        print("ir .........forward ")
        print("3 matrai ")
    if(ir44>0):
        left(0.3)
        print("ir .........left ")
        print("4 matrai ")
        
    

        
def checkobs():
    global x1, y1, w1, h1, x2,y2, w2,h2
    
    if (x1+w1<320 or x2+w2<320):
        ca=1
        
    if (x1<320 or x2<320):
        ca=2
    if ca is 1:
        if(w1*h1 > 650000 or w2*h2>65000 ):
            right(0.5)
            print("obstacle detect garera right gayo ")
    if ca is 2:
        
        if(w1*h1 > 650000 or w2*h2>65000 ):
            left(0.5)
            print("obstacle detect garera let gayo ")
    elif(w1*h1>130000 or w2*h2>130000):
        reverse(0.5)
        print("agadai nai obsctacle xa so reverse ")
    

##############################
def segment_bluecolour(frame): 
    hsv_roi =  cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask_1 = cv2.inRange(hsv_roi, np.array([26,88,98]), np.array([240,125,125]))
    ycr_roi=cv2.cvtColor(frame,cv2.COLOR_BGR2YCrCb)
    mask_2=cv2.inRange(ycr_roi, np.array((240,43,113)), np.array((208,88,119)))
    mask = mask_1 | mask_2
    kern_dilate = np.ones((8,8),np.uint8)
    kern_erode  = np.ones((3,3),np.uint8)
    mask= cv2.erode(mask,kern_erode)
    mask=cv2.dilate(mask,kern_dilate)    
    cv2.imshow('bluemask',mask)
    return mask  

def segment_greencolour(frame): 
    hsv_roi =  cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask_1 = cv2.inRange(hsv_roi, np.array([178,84,118]), np.array([88,84,118]))
    ycr_roi=cv2.cvtColor(frame,cv2.COLOR_BGR2YCrCb)
    mask_2=cv2.inRange(ycr_roi, np.array((88,85,63)), np.array((174,85,63)))
    mask = mask_1 | mask_2
    kern_dilate = np.ones((8,8),np.uint8)
    kern_erode  = np.ones((3,3),np.uint8)
    mask= cv2.erode(mask,kern_erode)      
    mask=cv2.dilate(mask,kern_dilate)     
    cv2.imshow('greenmask',mask)
    return mask 

        
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
xxx=1

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 16
rawCapture = PiRGBArray(camera, size=(640, 480))
time.sleep(0.001)
if(iflag==1):
      left(1)
      iflag=0

# aba image anlaysis kam
for image in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
      frame = image.array
      frame=cv2.flip(frame,1)
      hsv1 = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

      mask_red=segment_redcolour(frame)      #masking garnu paro red color ya bata
      loct,area=find_blob(mask_red)

      mask_blue=segment_bluecolour(frame)
      loctb,areab=find_blob(mask_blue)

      mask_green=segment_greencolour(frame)
      loctg,areag=find_blob(mask_green)
      
      x,y,w,h=loct
      x1,y1,w1,h1=loctb
      x2,y2,w2,h2=loctg
      
      print(x,y,w,h)
      print(x1,y1,w1,h1)
      print(x2,y2,w2,h2)
      if (w*h) < 10:  #area kati rakhni ta??
            found=0
      else:
            found=1
            simg2 = cv2.rectangle(frame, (x,y), (x+w,y+h), 255,2)
            simg2 = cv2.rectangle(frame, (x1,y1), (x1+w1,y1+h1), 150,2)
            simg2 = cv2.rectangle(frame, (x2,y2), (x2+w2,y2+h2), 50,2)
            



      ir11=GPIO.input(ir1)
      ir22=GPIO.input(ir2)
      ir33=GPIO.input(ir3)
      ir44=GPIO.input(ir4)

      
      checkobs()
      #GPIO.output(LED_PIN,GPIO.LOW)  
      if(found==0):   
            print("vetena")
            checkir()
            search()
            stop(0.05)
            
            
      elif(found==1):
            print("vetyo")
            if(x<215):
                  right(0)
                  print("corrright")
                  #stop(0.1)
            if(x>300):
                   left(0)
                   print("corrleft")
                  #stop(0.1)
            else:
                  forward(0)
                  #stop(0.1)
            if(w*h>2000):
                    forward(0)
                    #stop(0.1)
            
      cv2.imshow("draw",frame)    
      rawCapture.truncate(0)  # arko frame ko lagi clear frame lastai lang garo yesle garda 
      if(cv2.waitKey(1) & 0xff == ord('q')):
            break

GPIO.cleanup()

