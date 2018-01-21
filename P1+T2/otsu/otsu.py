import cv2
import numpy as np

'''
Algoritmo de otsu: escolhe o threshold otimo que minimiza a variancia intraclasse dos pixels limiarizados brancos e pretos
'''



imagemOriginal = cv2.imread("otsu.png", 0)

hist, bins = np.histogram(imagemOriginal.flatten(), 256, [0, 256])

somatorio = np.sum(range(0, 256) * hist)
total = imagemOriginal.shape[0] * imagemOriginal.shape[1]
sumB = 0
wB = 0
maximo = 0
limiar1 = 0
limiar2 = 0

for i in range(0, 256):
    wB = wB + hist[i]
    if(wB == 0): continue
    wF = total - wB
    if(wF == 0): break
    sumB = sumB + i * hist[i]
    mB = sumB / wB
    mF = (somatorio - sumB) / wF
    intermediario = wB * wF * (mB - mF) * (mB - mF)
    if(intermediario >= maximo):
        limiar1 = i
        if(intermediario > maximo):
            limiar2 = i
        maximo = intermediario

thresh = (limiar1 + limiar2) / 2

tr = np.zeros(256, dtype=np.uint8)
for i in range(0, 256):
    if(i < thresh): tr[i] = 0
    else: tr[i] = 255

img_res = tr[imagemOriginal]

cv2.imshow("original", imagemOriginal)
cv2.moveWindow("original", 0, 0)
cv2.imshow("result", img_res)
cv2.moveWindow("result", 512, 0)

cv2.waitKey(0)
cv2.destroyAllWindows()
