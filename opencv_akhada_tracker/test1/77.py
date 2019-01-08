import cv2

tracker=cv2.TrackerKCF_create()
cap=cv2.VideoCapture(0)
while True:
    
    ref,frame=cap.read()
    boxlist=[]
    color= 250
    while True:
        multitracker = cv2.MultiTracker_create()
        box=cv2.selectROI('Multitracker',frame)
        boxlist.append(box)
        print("selecting bounding boxes {}".format(boxlist))
        multi=multitracker.add(cv2.trackerKCF_create(),frame,boxlist)
        suc,boxes=multitracker.update(frame)
        for i,newbox in enumerate(boxes):
            p1=(int(newbox[0]),int(newbox[1]))
            p2=(int(newbox[0]+newbox[2]),int(newbox[1]+newbox[3]))
            cv2.rectangle(frame,p1,p2,color[i],2,1)
    cv2.imshow('Multitracker',frame)
    if cv2.waitKey(1)==27:
            break
        
cap.release()
cv2.destroyAllWindows()
