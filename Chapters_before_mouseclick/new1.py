import numpy as np
import cv2 as cv
from rescale import rescaleFrame

x=2**16-1
white=x*np.ones([150,200,3],'uint16')

cv.imshow("White",white)
print(white[0,0,:])

#cv.namedWindow("Image",cv.WINDOW_NORMAL)
#cv.imshow("Image",img)
#cv.destroyAllWindows()
cv.waitKey(0)
