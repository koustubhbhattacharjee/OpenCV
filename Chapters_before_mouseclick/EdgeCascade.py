import cv2 as cv
from cv2 import blur
def rescaleFrame(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
img=cv.imread('Photos\svitlana--zdhZEka7IQ-unsplash.jpg')
img_rescaled=rescaleFrame(img,0.2)
blur=cv.GaussianBlur(img_rescaled,(7,7),cv.BORDER_DEFAULT)
#edge detection
canny=cv.Canny(blur,125,175)


#dilate the imag
dilated=cv.dilate(canny,(3,3),iterations=5)

#Eroding
erode=cv.erode(dilated,(3,3),iterations=5)


#resizing and crop
resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('resize',resized)

#cv.imshow('Canny',erode)
cv.waitKey(0)
