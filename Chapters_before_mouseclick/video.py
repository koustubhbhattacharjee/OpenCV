import cv2 as cv
import numpy as np

cap=cv.VideoCapture(0)

color=(0,255,0)
line_width=3
radius=100
point=(0,0)

def click(event,x,y, flags,param):
    global point,pressed
    if event == cv.EVENT_LBUTTONDOWN:
        print("pressed",x,y)
        point=(x,y)
cv.namedWindow("frame")
cv.setMouseCallback("frame",click)

while(True):
    ret,frame=cap.read()
    frame=cv.resize(frame,(0,0),fx=0.5,fy=0.5)
    cv.circle(frame,point,radius,color,line_width)
    cv.imshow("frame",frame)

    ch=cv.waitKey(1)
    if ch & 0XFF==ord('q'):
        break

cap.release()
cv.destroyAllWindows()
