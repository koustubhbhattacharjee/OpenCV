import cv2 as cv
from cv2 import blur

def rescaleFrame(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

img=cv.imread('Photos\marko-brecic-n08SJtxUVFE-unsplash.jpg')
img_rescaled=rescaleFrame(img,0.1)
gray=cv.cvtColor(img_rescaled,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)


blur=cv.GaussianBlur(img_rescaled,(3,3),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)
cv.waitKey(0)