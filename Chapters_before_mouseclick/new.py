import numpy as np
import cv2 as cv
from rescale import rescaleFrame

img=cv.imread('Photos\isabella-rubie-photography-ZSgJT4L6dHQ-unsplash.jpg')
img_rescaled=rescaleFrame(img,1)
cv.namedWindow("Image",cv.WINDOW_NORMAL)
cv.imshow("Image",img)
cv.waitKey(0)
