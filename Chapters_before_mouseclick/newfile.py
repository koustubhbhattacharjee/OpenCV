
import cv2 as cv
import numpy as np

value=2**16-1
canvas=value*np.ones((600,600,3),'uint16') 

def func(event,x,y,flags,param):
    global canvas
    print(flags,event)
        
     

cv.namedWindow("Frame")
cv.setMouseCallback("Frame",func)

while True:
    cv.imshow("Frame",canvas)
    ch=cv.waitKey(1)
    if ch & 0xFF == ord('q'):
        break

cv.destroyAllWindows()