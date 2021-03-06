import cv2
import numpy as np
 
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
 
    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    red_image = cv2.inRange(hsv_image, (0,50,50), (8,170,200))
 
    circles = cv2.HoughCircles(red_image,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)
 
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),2)
        cv2.circle(frame,(i[0],i[1]),2,(0,0,255),3)
 
    cv2.imshow("camera", frame)
    cv2.imshow("red image", red_image)
    key=cv2.waitKey(1)
    if key== 'q':
        break

cap.release()
cv2.destroyAllWindows()

