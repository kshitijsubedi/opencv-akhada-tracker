import cv2
img=cv2.imread("jp1.jpg")
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(grey,scaleFactor=1.05,minNeighbors=5)
print(type(faces))
print(faces)
for x,y,w,h in faces :
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(45,150,310),2)

cv2.imshow("haha",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

