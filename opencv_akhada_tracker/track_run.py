import cv2

# this one works

cap= cv2.VideoCapture(0)
rel,frame=cap.read()
while True:

    box=cv2.selectROI("tracking",frame)
    tracker=cv2.TrackerKCF_create()
    while True:

        rel,frame=cap.read()
        ok=tracker.init(frame,box)
        ok,newbox = tracker.update(frame)
        print ok,newbox
        if ok:
            p1 = (int(newbox[0]), int(newbox[1]))
            p2 = (int(newbox[0] + newbox[2]), int(newbox[1] + newbox[3]))
            cv2.rectangle(frame, p1, p2, (200, 0, 0))

        cv2.imshow("haha",frame)
        if cv2.waitKey(1)==27:
            break
    if cv2.waitKey(1) == 27:
        break
        
