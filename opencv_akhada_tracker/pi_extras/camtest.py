import time
import picamera

with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(0.5)
    camera.annonate_text="Hey Smile"

pause()
