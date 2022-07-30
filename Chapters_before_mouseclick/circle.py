import cv2 as cv
from cv2 import blur
from cv2 import EVENT_LBUTTONDOWN
import numpy as np
from zmq import PROTOCOL_ERROR_WS_UNSPECIFIED
from rescale import rescaleFrame

cap=cv.VideoCapture(0)
val=255
color=(0,val,0)
line_width= 5
radius = 100
point = (0,0)

def click(event,x,y,flags,param):
    global point, pressed
    if event==cv.EVENT_MOUSEMOVE:
        print("Pressed",x,y)
        point=(x,y)
cv.namedWindow("Camera")
cv.setMouseCallback("Camera",click)

while(True):
    ret,frame=cap.read()
    frame = cv.resize(frame,(0,0),fx=0.5,fy=0.5)
    cv.circle(frame, point, radius,color,line_width)
    cv.imshow("Camera",frame)

    ch=cv.waitKey(1)
    if ch & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()