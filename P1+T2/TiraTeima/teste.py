#!/usr/bin/python

from __future__ import print_function
from geopy.geocoders import Nominatim
from io import BytesIO
import Image
import urllib

import random
import os.path
import cv2
import numpy as np
import sys

def RecuperaRegiao (centro):
 url = "http://maps.googleapis.com/maps/api/staticmap?center="+str(centro[0])+", "+str(centro[1])  +"&size=800x800&zoom=15&maptype=satellite"
 buffer = BytesIO(urllib.urlopen(url).read())
 raw = Image.open(buffer)
 img = np.array(raw).copy()
 return img

def Preprocessa(image):
 img = cv2.imread(image,1)
 img = cv2.medianBlur(img,3)
 #kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
 #kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
 #img_prewittx = cv2.filter2D(img, -1, kernelx)
 #img_prewitty = cv2.filter2D(img, -1, kernely)
 #img = cv2.medianBlur(img,5)
 kernel = np.array([[1, 0, -1],
                   [1, -1, -1],
                   [1, 0, 1]]).astype(float)
 img = cv2.filter2D(img,-5,kernel)
 #img = img_prewittx + img_prewitty
 return img

def DetectaCirculos (imagem,tolerancia):
 #cv2.imshow("",imagem)
 #cv2.waitKey(0)

 maxRaio = 200
 minRaio = 100
 minDist = (maxRaio+minRaio)*1.5
 #cv2.imwrite(str(random.random())+".jpg",imagem)
 #cv2.imshow("Detectando circulos",imagem)
 #cv2.waitKey(0)
 circles = cv2.HoughCircles(imagem,cv2.HOUGH_GRADIENT,1,minDist,param1=50,param2=tolerancia,minRadius=minRaio,maxRadius=maxRaio)
 return circles

def getLocalAtual (centroRegiao):
 #print("Carregando imagem da Web")
 centroRegiaoStr = str(centroRegiao[0]) + ", " + str(centroRegiao[1])
 geolocator = Nominatim()
 try:
  localAtual = geolocator.reverse(centroRegiaoStr).raw["address"]["state"]
 except geopy.geocoders.exc.GeocoderUnavailable as e:
  getLocalAtual()
 return localAtual

def scanRegiao (localAtual):
 #print ("Escaneando Regiao ",localAtual)
 nomeArq = str(("Regiao " + str(str(localAtual[0]) + "," + str(localAtual[1])) + ".jpg"))
 if os.path.isfile("[RAW] " + nomeArq):
  #print ("Carregando imagem do arquivo")
  aux = cv2.imread("[RAW] " + nomeArq)
  imagemOriginal = Preprocessa(("[RAW] " + nomeArq))
 else:
  imagemOriginal = RecuperaRegiao(localAtual)
  cv2.imwrite("[RAW] " + nomeArq,imagemOriginal)
  aux = cv2.imread("[RAW] " + nomeArq)
  imagemOriginal = Preprocessa("[RAW] " + nomeArq)
 imagemOriginal = cv2.cvtColor(imagemOriginal,cv2.COLOR_RGB2GRAY)
 
 circles = DetectaCirculos(imagemOriginal,60)

 if circles is not None:
	circles = np.round(circles[0, :]).astype("int")
 
	for (x, y, r) in circles:
		cv2.circle(aux, (x, y), r, (0, 255, 0), 4)
		cv2.rectangle(aux, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
 
	# show the output image
	#cv2.imwrite("[SEG] " + nomeArq,aux)

 return len(circles) if circles is not None else 0
#P1 = -16.802408, -47.639134
#P2 = -16.802408, -47.594969
#P3 = -16.836638, -47.639134
#P4 = -16.836638, -47.594969
P1 = -13.745748, -50.617370
P4 = -18.179858, -48.013616
'''
p1---p2
|    |
|    |
p3---p4
'''

#-16.822408,-47.614969
def main():
 print(scanRegiao((-16.822408,-47.614969)))
''''
 nPivos = 0
 decrescesor = 0.02;
 i=P1[0];
 while i>=P4[0]:
  j = P4[1];
  while j>=P1[1]:
   it = scanRegiao((i,j))
   print("Regiao (",i,j,") possui ",it,"pivos")
   nPivos += it
   j -= decrescesor;	
  i -= decrescesor;
 print (nPivos," pivos encontrados")
'''

if __name__ == '__main__':
 main()
