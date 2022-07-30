import numpy as np
import cv2 as cv

img= cv.imread("./Photos/tomatoes.jpg",1)
hsv= cv.cvtColor(img,cv.COLOR_BGR2HSV)
res,thresh = cv.threshold(hsv[:,:,0],25,255,cv.THRESH_BINARY_INV)
cv.imshow("Thresh",thresh)
edges=cv.Canny(img,100,70)
cv.imshow("Canny",edges)
cv.waitKey(0)

#TODO: i dont't understand how thresholding works in cannt with 100 and 70
cv.destroyAllWindows()


#the blobbing of three tomatoes in this image means contour would treat it as one image
#canny can help us here





