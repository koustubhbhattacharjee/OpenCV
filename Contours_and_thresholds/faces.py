from matplotlib.colors import rgb_to_hsv
import numpy as np
import cv2 as cv
from Chapters_before_mouseclick.rescale import rescaleFrame


#! WHY DOES SATURATION*INVERSEHUE WORK?

#Ans: Probably because people's faces tend to be redder than their surroudings, than not?
#Human skin is saturated compared it to it's more clear hued surroundings.
#Makes sense. 

img=cv.imread("./Photos/faces.jpeg",1)
img_read=rescaleFrame(img,scale=0.2)
hsv=cv.cvtColor(img_read,cv.COLOR_BGR2HSV)
h=hsv[:,:,0]
s=hsv[:,:,1]
v=hsv[:,:,2]
hsv_split=np.concatenate((h,s,v),axis=1)
ret, min_sat=cv.threshold(s,40,255,cv.THRESH_BINARY)
cv.imshow("Sat filter",min_sat)

ret,max_hue=cv.threshold(h,15,255,cv.THRESH_BINARY_INV)
cv.imshow("Hue Filter",max_hue)
final=cv.bitwise_and(min_sat,max_hue) #<----------works because these are all binary values here
cv.imshow("Final",final)


#cv.imshow('Split',hsv_split)
cv.waitKey(0)
cv.destroyAllWindows


