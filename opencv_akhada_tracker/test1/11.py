import cv2
import numpy as np

vid=cv2.VideoCapture(0)

while True:
    _, frame=vid.read()
    hsv=cv2.GaussianBlur(frame,(5,5),0)
    lower=np.array([38,86,0])
    higher=np.array([121,255,255])
    mask=cv2.inRange(hsv,lower,higher)

    _,contours,_=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    print(contours)
    for contour in contours:
        area=cv2.contourArea(contour)
        if area>1000:
            cv2.drawContours(frame,contours,-1,(0,255,0),3)

    cv2.imshow("",mask)
    cv2.imshow("",hsv)
    cv2.imshow("  ",frame)
    key=cv2.waitKey(1)
    if key == 'q':
        break
    
vid.release()
cv2.destroyAllWindows()
