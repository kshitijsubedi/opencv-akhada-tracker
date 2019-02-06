import gpiozero
import cv2
import time
import signal
import picamera
import RPi.GPIO as gpio
import Tkinter as tk

# i believe i can fly

# time ra pause use garnu parxa ki kya ho?

motor1=2
motor11=3
motor2=4
motor22=5

gpio.setup(motor1, gpio.OUT)
gpio.setup(motor11, gpio.OUT)

gpio.setup(motor2, gpio.OUT)
gpio.setup(motor22, gpio.OUT)



def forward():
    gpio.output(motor1, gpio.high)
    gpio.output(motor11, gpio.low)
    gpio.output(motor2,gpio.high)
    gpio.output(motor22, gpio.low)
    time.sleep(0.5)
    pass

def reverse():
    gpio.output(motor1,gpio.low)
    gpio.output(motor11, gpio.high)
    gpio.output(motor2, gpio.low)
    gpio.output(motor22, gpio.high)
    pass

def right():
    gpio.output(motor1, gpio.high)
    gpio.output(motor11, gpio.low)
    gpio.output(motor2,gpio.high)
    gpio.output(motor22, gpio.low)
 
    pass

def left():
    gpio.output(motor1, gpio.high)
    gpio.output(motor11, gpio.low)
    gpio.output(motor2,gpio.high)
    gpio.output(motor22, gpio.low)
    pass

def rotate():
    gpio.output(motor1, gpio.high)
    gpio.output(motor11, gpio.low)
    gpio.output(motor2,gpio.high)
    gpio.output(motor22, gpio.low)
    pass
def startrotate():
    gpio.output(motor1, gpio.high)
    gpio.output(motor11, gpio.low)
    gpio.output(motor2,gpio.high)
    gpio.output(motor22, gpio.low)

    sflag=1
    pass