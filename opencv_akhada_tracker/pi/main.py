import gpiozero
import cv2
import time
import signal
import picamera
import RPi.GPIO as gpio
import move
import imganaly



camera=PiCamera()
camera.start_preview()
gpio.setmode(gpio.BOARD)

#pin lai define garni
button1=gpiozero.Button(13)
button2=gpiozero.Button(14)

led=13

#selfie 
camera = PiCamera()
camera.resolution = (160, 120)
camera.framerate = 16
rawCapture = PiRGBArray(camera, size=(160, 120))
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
      
#yo arko file ma garnu parxa

# pin set garni
gpio.setup(led,gpio.out)


#kam garni

gpio.output(led,False)
gpio.output(led, gpio.high)

time.sleep(0.5)

      cv2.imshow("draw",frame)    
      rawCapture.truncate(0)  # clear
      if(cv2.waitKey(27) & 0xff == ord('q')):
            break
gpio.cleanup()
pause()

#draft
# flag 
