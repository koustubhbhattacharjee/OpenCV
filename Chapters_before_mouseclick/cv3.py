import numpy as np
import cv2
from rescale import rescaleFrame

color1=cv2.imread("Photos\svitlana--zdhZEka7IQ-unsplash.jpg",1)
color2=rescaleFrame(color1,0.15)
gray=cv2.cvtColor(color2,cv2.COLOR_RGB2GRAY)
cv2.imwrite('gray.jpg',gray)
b=color2[:,:,0]
g=color2[:,:,1]
r=color2[:,:,2]
rgba=cv2.merge((b,g,r,2*g))
cv2.imwrite("rgba.png",rgba)
