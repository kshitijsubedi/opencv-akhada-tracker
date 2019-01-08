import numpy as np
import cv2

cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()
while True :
	ret, frame1 = cap.read()
	frame=cv2.flip(frame1,1)
	fgmask = fgbg.apply(frame)
	_,contours,_ = cv2.findContours(fgmask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	for c in contours:
			if cv2.contourArea(c) < 500:
					continue
			(x, y, w, h) = cv2.boundingRect(c)
	cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
	cv2.imshow('lastai kada ho ',fgmask)
	cv2.imshow('rgb',frame)
	if cv2.waitKey(1) & 0xFF == ord("q"):
		break
cap.release()
cv2.destroyAllWindows()
