import cv2 as cv
import numpy as np
import inspect

img=cv.imread("./Photos/fuzzy.png")
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
hue,sat,val=np.split(hsv,3,axis=2)
kernel=np.ones((5,5),'uint8')
dilate=cv.dilate(sat,kernel,iterations=1)
res,thresh = cv.threshold(dilate,200,255,cv.THRESH_BINARY)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
objects = np.zeros([img.shape[0], img.shape[1], 3], 'uint8')
index = -1
thickness = -1

for c in contours:
    M = cv.moments(c)
    cx = int(M['m10']/M['m00'])          # 10 represents moment along x=1,y=0 direction

    cy = int(M['m01']/M['m00'])
    print(cx,cy)
    
    r,g,b = int(img[cy][cx][0]),int(img[cy][cx][1]),int(img[cy][cx][2])
    color=(r,g,b)
    print(color)
    cv.drawContours(objects, [c], -1, color, -1)
    
    
cv.imshow("Contours",objects)
cv.imshow("ORiginal",img)
cv.waitKey(0)
cv.destroyAllWindows()
"""-----------Kernel----------
                             |
                             |
                             |
                             V """ 
#blur = cv.GaussianBlur(img, (5,55),0)

#kernel=np.ones((5,5),'unint8')
#dilate=cv.dilate(img,kernel,iterations=1)
