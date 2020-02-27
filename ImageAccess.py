import numpy as np
import matplotlib.pyplot as plt
import cv2
 
img = cv2.imread('Figure_1.png',cv2.IMREAD_GRAYSCALE)
#cv2.imshow('Figure_1',img)
img2 = cv2.imread('Figure_3.png',cv2.IMREAD_GRAYSCALE)
#cv2.imshow('Figure_3',img2)
if(cv2.imshow('Figure_1',img)==cv2.imshow('Figure_3',img2)):
   print "match found"
else:
   print "not found"
plt.imshow(img, cmap='gray',interpolation='bicubic')
plt.show()
cv2.waitkey(0)
cv2.distroyAllWindows()
