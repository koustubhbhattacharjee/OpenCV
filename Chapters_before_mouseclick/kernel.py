import cv2 as cv
from cv2 import blur
import numpy as np
from rescale import rescaleFrame

image=cv.imread('Photos\svitlana--zdhZEka7IQ-unsplash.jpg',1)
image2=rescaleFrame(image,0.5)
kernel=np.ones((5,5),'uint8')
dilate=cv.dilate(image2,kernel,iterations=1)
erode=cv.erode(image2,kernel,iterations=1)
cv.imshow("dilate",dilate)
cv.imshow("erode",erode)
cv.waitKey(0)
cv.destroyAllWindows()