from pyimagesearch.shapedetector import ShapeDetector
import argparse
import imutils
import cv2

imgOriginal = cv2.imread("1.png")
imgAjusteTam = imutils.resize(imgOriginal, width=300)
taxaTamOrigTamNovo = imgOriginal.shape[0] / float(imgAjusteTam.shape[0])

img_pb = cv2.cvtColor(imgAjusteTam, cv2.COLOR_BGR2GRAY)
imgBorrada = cv2.GaussianBlur(img_pb, (5, 5), 0)
thresh = cv2.threshold(imgBorrada, 60, 255, cv2.THRESH_BINARY)[1]

contornos = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
contornos = contornos[0] if imutils.is_cv2() else contornos[1]
sd = ShapeDetector()

for c in contornos:
	M = cv2.moments(c)
	cX = int((M["m10"] / M["m00"]) * taxaTamOrigTamNovo)
	cY = int((M["m01"] / M["m00"]) * taxaTamOrigTamNovo)
	shape = sd.detect(c)

	c = c.astype("float")
	c *= taxaTamOrigTamNovo
	c = c.astype("int")
	cv2.drawContours(imgOriginal, [c], -1, (0, 255, 0), 2)
	cv2.putText(imgOriginal, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
		0.5, (255, 255, 255), 2)

	cv2.imshow("imgOriginal", imgOriginal)
	cv2.waitKey(0)
