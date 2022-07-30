import numpy as np
import cv2

def rescaleFrame(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv2.resize(frame,dimensions,interpolation=cv2.INTER_AREA)

bw=cv2.imread(r'C:\Users\kxb173230\Desktop\Books\openCV\Photos\julien-pianetti-Cr9hZrpC1Oc-unsplash.jpg', 0)
bw_rescaled=rescaleFrame(bw,scale=0.3)

#zero loads in bw
height,width=bw_rescaled.shape[0:2]
#first two values from shape

cv2.imshow("Original BW",bw_rescaled)

binary=np.zeros([height,width,1],'uint8')
threshold= 200

for row in range(0,height):
    for columns in range(0, width):
        if bw_rescaled[row][columns]>threshold:
            binary[row][columns]=255
        
#cv2.imshow("Slow Binary", binary)

#very simple thresholding 
ret,thresh=cv2.threshold(bw_rescaled,threshold,255,cv2.THRESH_BINARY)


cv2.imshow("CV_thresh",thresh)
cv2.waitKey(0)
cv2.destroyAllWindows