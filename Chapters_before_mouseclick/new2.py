import numpy as np
import cv2 as cv
from rescale import rescaleFrame

color1=cv.imread("Photos\svitlana--zdhZEka7IQ-unsplash.jpg",1)
color=rescaleFrame(color1,0.15)
cv.imshow("Image",color)
cv.moveWindow("Image",0,0)
print(color.shape)
height,width,channels=color.shape

b,g,r=cv.split(color)


zeros=np.empty((np.size(g[:,0]),np.size(g[0,:])))

print(np.shape(g),np.shape(zeros))

rgb_split=np.empty([height,width*3,3],'uint8')
rgb_split[:,width:width*2]=cv.merge([g,g,g])
rgb_split[:,0:width]=cv.merge([b,b,b])
rgb_split[:,2*width:width*3]=cv.merge([r,r,r])
cv.imshow("Channels",rgb_split)

hsv=cv.cvtColor(color,cv.COLOR_BGR2HSV)
h,s,v=cv.split(hsv)
hsv_split=np.concatenate((h,s,v),axis=1)
cv.imshow("HSV",hsv_split)
cv.waitKey(0)
cv.destroyAllWindows()



