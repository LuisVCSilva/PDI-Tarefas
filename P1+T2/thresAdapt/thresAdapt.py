import numpy as np 
import cv2

img = cv2.imread("1.jpg")
cv2.imshow("1.jpg",img)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Pb",gray)
cv2.waitKey(0)
 
blur_img = cv2.GaussianBlur(gray,(5,5),0)
cv2.imshow("Desf. Gauss",blur_img)
cv2.waitKey(0)

threshold_img = cv2.adaptiveThreshold(blur_img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,5,4)
cv2.imshow("Adapt1",threshold_img)
cv2.waitKey(0)

threshold_img2 = cv2.adaptiveThreshold(blur_img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,15,3)
cv2.imshow("Adapt2",threshold_img2)
cv2.waitKey(0)
