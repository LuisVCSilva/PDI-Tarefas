# -*- coding: utf-8 -*-

import cv2
import numpy as np

def getLookupTable_R(x):
    
    if x < 128:
        return 0
    elif x < 192:
        return 4 * x - 512
    else:
        return 256
    
def getLookupTable_G(x):
    
    if x < 64:
        return 4 * x 
    elif x < 192:
        return 256
    else:
        return -4 * x + 1024

def getLookupTable_B(x):
    
    if x < 64:
        return 256
    elif x < 128:
        return -4 * x + 512
    else:
        return 0 



if __name__ == '__main__':
    tabelaR = np.ones((256, 1), dtype = 'uint8' ) * 0
    tabelaG = np.ones((256, 1), dtype = 'uint8' ) * 0
    tabelaB = np.ones((256, 1), dtype = 'uint8' ) * 0

    for i in range(256):

        tabelaR[i][0] = getLookupTable_R(i)
        tabelaG[i][0] = getLookupTable_G(i)
        tabelaB[i][0] = getLookupTable_B(i)


    imgOriginal = cv2.imread("raiox.png", 1)

    img_PB = cv2.cvtColor(imgOriginal, cv2.COLOR_BGR2GRAY)

    imgR = cv2.LUT(img_PB, tabelaR)
    imgG = cv2.LUT(img_PB, tabelaG)
    imgB = cv2.LUT(img_PB, tabelaB)

    combImg = cv2.merge((imgB,imgG,imgR))    

    cv2.imshow("resultado", combImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


