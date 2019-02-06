import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)

motor1=2
motor11=3
motor2=4
motor22=5

def init():
    gpio.setup(motor1,gpio.OUT)

    gpio.setup(motor2,gpio.OUT)

    gpio.setup(motor11,gpio.OUT)

    gpio.setup(motor22,gpio.OUT)
    gpio.output(motor11, True)
    gpio.output(motor22, True)

def forward(tf):
    gpio.output(motor1, True)
    gpio.output(motor2, False)
    time.sleep(tf)

def reverse(tf):
    gpio.output(motor1, False)
    gpio.output(motor2, True)
    time.sleep(tf)

def key_input(event):
    init()
    print 'Key:', event.char
    key_press = event.char
    sleep_time = 0.030

    if key_press.lower() == 'w':
        forward(sleep_time)
    elif key_press.lower() == 's':
        reverse(sleep_time)
    elif key_press.lower() == 'a':
        turn_left(sleep_time)
    elif key_press.lower() == 'd':
        turn_right(sleep_time)
    
root = tk.Tk()
root.bind('<KeyPress>', key_input)
root.mainloop()
