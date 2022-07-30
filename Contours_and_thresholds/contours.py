from xml.etree.ElementTree import Comment
import numpy as np
import cv2 as cv

img = cv.imread('./Photos/detect_blob.png', 1)

gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 115, 1)


# contour
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
img2 = img.copy()
index = -1
thickness = 4
color = (255, 0, 255)


# cv.drawContours(img2, contours, index, color, thickness)
# cv.imshow("Contour", img2)


objects = np.zeros([img.shape[0], img.shape[1], 3], 'uint8')
# the frame used

for c in contours:
    cv.drawContours(objects, [c], -1, color, -1)    # why is [c] in that shape, -1 indicates all contours
    # last -1 is for fill
    area = cv.contourArea(c)
    perimeter = cv.arcLength(c, True)
    M = cv.moments(c)
    cx = int(M['m10']/M['m00'])          # 10 represents moment along x=1,y=0 direction

    cy = int(M['m01']/M['m00'])          # 01 represents moment along x=0, y= 1 direction
    cv.circle(objects, (cx, cy), 4, (0, 0, 255), -1)   # 4 is the radius, -1 is fill
    print("area: {}, perimeter {}, cx {}, cy {}".format(area, perimeter, cx, cy))
cv.imshow("Frame", objects)
cv.waitKey(0)
cv.destroyAllWindows()
