import numpy as np
import cv2
 
img = cv2.imread('_1.jpg',0)


clahe = cv2.createCLAHE(clipLimit=50.0, tileGridSize=(4,4))
cl1 = clahe.apply(img)
cv2.imwrite('clahe_2.jpg',cl1)
cv2.imshow('',cl1)
cv2.waitKey(0)
