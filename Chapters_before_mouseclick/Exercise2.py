
import cv2 as cv
from cv2 import EVENT_LBUTTONDOWN
import numpy as np

canvas=np.ones([600,600,3],'uint8')*255
pressed=False
radius=3
color=(0,255,0)

#totally different from what i did. the result i mean

def func(event,x,y,flags,param):
    
    global canvas,pressed
    
    
#    rect1=((x<=150 
 #           and x>=50) 
  #          and (y>=50 
   #         and y<=150))
   # rect2=((x>=200 
    #        and x<=300)
     #       and (y>=50 
      #      and y<=150))
    
    if event==cv.EVENT_LBUTTONDOWN:
        pressed=True
        cv.circle(canvas,(x,y),radius,color,-1)
    
    elif event==cv.EVENT_MOUSEMOVE and pressed==True:
        cv.circle(canvas,(x,y),radius,color,-1)
        print("nothing")

    elif event==cv.EVENT_LBUTTONUP:
        pressed=False
           

cv.namedWindow("Frame")
cv.setMouseCallback("Frame",func)



while True:
    cv.imshow("Frame",canvas)
    ch=cv.waitKey(1)
    if ch & 0xFF == ord('q'):
        break
    elif ch & 0xFF == ord('b'):
        color=(255,0,0)
    elif ch & 0XFF == ord('r'):
        color=(0,0,255)
    elif ch & 0XFF == ord('g'):
        color=(0,255,0)

cv.destroyAllWindows()
    
