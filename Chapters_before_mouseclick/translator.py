import cv2 as cv
from cv2 import blur
import numpy as np
img=cv.imread('Photos/toa-heftiba-G8Fe7Q-9g_8-unsplash.jpg')
def rescaleFrame(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
def translate(img,x,y):
    transMat =np.float32([[1,0,x],[0,1,y]])
    dimesions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimesions)

img_rescaled=rescaleFrame(img,0.1)
translated=translate(img_rescaled,100,100)
cv.imshow('Translated',translated)


def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]

    if rotPoint is None:
        rotPoint=(width//2,height//2)
    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions=(width,height)

    return cv.warpAffine(img,rotMat,dimensions)
rotated=rotate(img_rescaled,45)
cv.imshow('rotated',rotated)
cv.waitKey(0)