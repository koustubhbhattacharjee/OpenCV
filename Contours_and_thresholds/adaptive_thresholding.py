import numpy as np
import cv2
from Chapters_before_mouseclick.rescale import rescaleFrame

bw=cv2.imread("./Photos/annie-spratt-Y-JCyxFMXbc-unsplash.jpg", 0)
bw_rescaled=rescaleFrame(bw,
                         scale=0.1)
cv2.imshow("original",
           bw_rescaled)
ret,thresh_basic=cv2.threshold(bw_rescaled,
                               150,
                               255,
                               cv2.THRESH_BINARY)
cv2.imshow("Cv_thresh",
           thresh_basic)


##__________________________________________________________________________________image_type
#|                   ________________________________________________________________OpenCV function.
#|                   |
#|                   |
#V                   V
thres_adapt=cv2.adaptiveThreshold(bw_rescaled,                    #<-------------------------image
                                  255,                            #<-------------------------highest value.
                                  cv2.ADAPTIVE_THRESH_GAUSSIAN_C, #<-------------------kind of adaptive thresholding
                                  cv2.THRESH_BINARY, #<----------------------the kind of small scale thresholding i suppose
                                  115,  #<------------------------size of the kernel.
                                  1)    #<------------------------1 is mean subtraction, so that no group has an offset!



cv2.imshow("CV_adapt",thres_adapt)
cv2.waitKey(0)
cv2.destroyAllWindows