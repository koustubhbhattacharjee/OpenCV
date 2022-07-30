import cv2 as cv
import numpy as np

from rescale import rescaleFrame

image=cv.imread('Photos\svitlana--zdhZEka7IQ-unsplash.jpg',1)
image2=rescaleFrame(image,0.25)

img_half=cv.resize(image2,(0,0),fx=0.5,fy=0.5)
img_bad_stretch=cv.resize(image2,(600,600))
img_stretch=cv.resize(image2,(600,600),interpolation=cv.INTER_NEAREST)
cv.imshow("1",image2)
#cv.imshow("2",img_half)
#cv.imshow("3",img_bad_stretch)
#cv.imshow("4",img_stretch)


######
M=cv.getRotationMatrix2D((0,0),-30,1)
rotated=cv.warpAffine(image2,M,(image2.shape[1],image2.shape[0]))
cv.imshow("rotate",rotated)




cv.waitKey(0)
cv.destroyAllWindows()



