import numpy as np
import cv2

img = cv2.imread("faces.jpeg",1)
img = cv2.imread("faces.jpeg",1)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
path="./haarcascade_eye.xml"

eyes_cascade=cv2.CascadeClassifier(path)
eyes=eyes_cascade.detectMultiScale(gray, scaleFactor=1.02, minNeighbors=20, minSize=(10,10))
print(len(eyes))

for (x,y,w,h) in eyes:
    print(x,y,w,h)
    cv2.circle(img,(int(x+w/2),int(y+h/2)),10,(0,255,0),2)
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()