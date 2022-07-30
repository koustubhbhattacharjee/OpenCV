import cv2 as cv
import numpy as np


img=cv.imread('./Photos/detect_blob.png',1)
                
gray=cv.cvtColor(img,cv.COLOR_RGB2GRAY)
grad_val=np.gradient(gray)
grad_val_2=np.gradient(grad_val)
print(grad_val)

for i,j in np.array(grad_val_2)[].shape:
    count=0
    if grad_val_2[i,j]==0:
        print(i,j)
        count+=1
    
    if count==0:
        print("nothing")
    
    



#thresh= cv.adaptiveThreshold(gray,255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 115,1)