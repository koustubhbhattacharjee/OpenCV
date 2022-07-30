import cv2 as cv
import numpy as np
import pandas as pd

def rescaleFrame(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)

#img = cv.imread('istockphoto-687245168-170667a.jpg')
capture=cv.VideoCapture('Videos/videoplayback.mp4')

while True:
    isTrue, frame= capture.read()
    resizedframe= rescaleFrame(frame,2)
    cv.imshow('Video',resizedframe)

    if cv.waitKey(20) & 0XFF==ord("d"):
        break

capture.release()
cv.destroyAllWindows()
#cv.imshow('Idk',img)

cv.waitKey(0)

#end of lecture 1

