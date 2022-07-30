import cv2 as cv
import numpy as np
value=2**16-1
frame1=value*np.ones((600,600,3),'uint16') 
frame=value*np.ones((600,600,3),'uint16')

def func(b):
    global frame, frame1
    frame=frame1
    frame=frame+1
    return np.sum(frame), np.sum(frame1)
for i in range(10):
    a,b=func(1)
    print(a,b)