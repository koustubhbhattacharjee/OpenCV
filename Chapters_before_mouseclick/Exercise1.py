


import cv2 as cv
from cv2 import EVENT_LBUTTONDOWN
import numpy as np
import copy


point=(0,0)
colour=(0,0,0)
line_width= 5
thickness=-1
count=1
radius=1
value=2**16-1
canvas=value*np.ones((600,600,3),'uint16')
frame=value*np.ones((600,600,3),'uint16')

def boxes():
    global canvas,frame
    cv.rectangle(canvas,
                (50,50),
                (150,150),
                color=(2**16-1,0,0),
                thickness=-1)

    cv.putText(canvas,
                'Blue',
                fontFace=cv.FONT_HERSHEY_SIMPLEX,
                org=(70,70),
                fontScale=0.5,
                thickness=1,
                color=(0,0,0))

    cv.rectangle(canvas,
                (200,50),
                (300,150),
                color=(0,2**16-1,0),
                thickness=-1)

    cv.putText(canvas,
                'Green',
                fontFace=cv.FONT_HERSHEY_SIMPLEX,
                fontScale=0.5,
                thickness=1,
                org=(220,70),
                color=(0,0,0))
    frame=copy.deepcopy(canvas)

boxes()



def func(event,x,y,flags,param):
    
    global point,radius,line_width,thickness,colour,count,canvas,frame
    
    
    rect1=((x<=150 
            and x>=50) 
            and (y>=50 
            and y<=150))
    rect2=((x>=200 
            and x<=300)
            and (y>=50 
            and y<=150))
    
    if event==cv.EVENT_LBUTTONDOWN:
        if  rect1:
            colour=(2**16-1,0,0)
        elif rect2:
            colour=(0,2**16-1,0)
        else:
            point=(x,y)
    
    elif event==cv.EVENT_MOUSEMOVE and flags==cv.EVENT_FLAG_LBUTTON:
        canvas=copy.deepcopy(frame)                
        radius=round(np.sqrt((x-point[0])**2+(y-point[1])**2))
        cv.circle(canvas, point, radius,colour,line_width)
        

    elif event==cv.EVENT_LBUTTONUP:
        cv.circle(canvas, point, radius,colour,line_width)
        frame=copy.deepcopy(canvas)
           

           
    




cv.namedWindow("Frame")
cv.setMouseCallback("Frame",func)



while True:
    cv.imshow("Frame",canvas)
    ch=cv.waitKey(1)
    if ch & 0xFF == ord('q'):
        break
cv.imwrite("Img1.jpg",canvas) 
cv.destroyAllWindows()

    
    

    

