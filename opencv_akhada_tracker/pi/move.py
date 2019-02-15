import gpiozero
import cv2
import time
import signal
import picamera
import RPi.GPIO as gpio


motor1=3
motor11=5
motor2=7
motor22=11

def init():
    gpio.setup(motor1,gpio.OUT)

    gpio.setup(motor2,gpio.OUT)

    gpio.setup(motor11,gpio.OUT)

    gpio.setup(motor22,gpio.OUT)
    gpio.output(motor11, True)
    gpio.output(motor22, True)

def forward(tf):
    gpio.output(motor1, True)
    gpio.output(motor2, True)
    gpio.output(motor11,False)
    gpio.output(motor22,False)
    print("for")
    time.sleep(tf)

def reverse(tf):
    gpio.output(motor1, False)
    gpio.output(motor2, False)
    gpio.output(motor11,True)
    gpio.output(motor22,True)
    print("rev")
    time.sleep(tf)

init()
forward(5)
reverse(5)
gpio.cleanup()