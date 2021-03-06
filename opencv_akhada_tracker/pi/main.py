import cv2
import time
import signal
import picamera
import RPi.GPIO as gpio
import move
import imganaly
import gpiozero
import numpy as np

### define ir and motors
gpio.setmode(gpio.BOARD)

button1=gpiozero.Button(13)
button2=gpiozero.Button(14)


#selfie 
camera = picamera.PiCamera()
camera.resolution = (160, 120)
camera.framerate = 16
camera.start_preview()
rawCapture = picamera.array.PiRGBArray(camera, size=(160, 120))
time.sleep(0.5)

#aba image analysis 
for image in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
      frame = image.array
      frame=cv2.flip(frame,1)
      global centre_x
      global centre_y
      centre_x=0.
      centre_y=0.
      hsv1 = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
      mask_red=segment_colour(frame)      #masking red the frame
      loct,area=find_blob(mask_red)
      x,y,w,h=loct
      if (w*h)<10:
        found=0
      else:
        found =1
        cv2.rectangle(mask_red,(x,y),(x+w,y+h),(80,18,200),1)
        
def find_blob(blob):
    largest_contour=0
    cont_index=0
    contours, hierarchy = cv2.findContours(blob, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    for idx, contour in enumerate(contours):
        area=cv2.contourArea(contour)
        if (area >largest_contour) :
            largest_contour=area
            cont_index=idx                           
    r=(0,0,2,2)
    if len(contours) > 0:
        r = cv2.boundingRect(contours[cont_index])
       
    return r,largest_contour

#kam garni
#sflag=0


#if sflag=0:
 #   startrotate()
time.sleep(0.5)
game()
cv2.imshow("draw",frame)    
rawCapture.truncate(0)  # clear
if(cv2.waitKey(27) & 0xff == ord('q')):
    break
gpio.cleanup()
pause()


