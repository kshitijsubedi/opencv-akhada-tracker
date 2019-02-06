import gpiozero
import cv2
import time
import signal
import picamera
import RPi.GPIO as gpio

# i believe i can fly

# time ra pause use garnu parxa ki kya ho?
motor1=2
motor11=3
motor2=4
motor22=5
motor3=4
motor33=6

GPIO.setup(MOTOR1B, GPIO.OUT)
GPIO.setup(MOTOR1E, GPIO.OUT)

GPIO.setup(MOTOR2B, GPIO.OUT)
GPIO.setup(MOTOR2E, GPIO.OUT)


def forward():
    gpio.output(motor1, gpio.high)
    gpio.output(motor11, gpio.low)
    gpio.output(motor2,gpio.high)
    gpio.output(motor22, gpio.low)
    gpio.output(motor3,gpio.high)
    gpio.output(motor33, gpio.low)

    pass

def reverse():
    gpio.output(motor1,gpio.low)
    gpio.output(motor11, gpio.high)
    gpio.output(motor2, gpio.low)
    gpio.output(motor22, gpio.high)
    gpio.output(motor3, gpio.low)
    gpio.output(motor33, gpio.high)
    pass

def right():
    gpio.output(motor1, gpio.high)
    gpio.output(motor11, gpio.low)
    gpio.output(motor2,gpio.high)
    gpio.output(motor22, gpio.low)
    gpio.output(motor3,gpio.high)
    gpio.output(motor33, gpio.low)
    pass

def left():
    gpio.output(motor1, gpio.high)
    gpio.output(motor11, gpio.low)
    gpio.output(motor2,gpio.high)
    gpio.output(motor22, gpio.low)
    gpio.output(motor3,gpio.high)
    gpio.output(motor33, gpio.low)
    pass

def rotate():
    gpio.output(motor1, gpio.high)
    gpio.output(motor11, gpio.low)
    gpio.output(motor2,gpio.high)
    gpio.output(motor22, gpio.low)
    gpio.output(motor3,gpio.high)
    gpio.output(motor33, gpio.low)
    pass
