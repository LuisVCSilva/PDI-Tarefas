import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('img.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Dividi a img em 5000 celulas, 20x20 cada
celulas = [np.hsplit(row,100) for row in np.vsplit(gray,50)]

# Passa pra array
x = np.array(celulas)

# Separa o testee do treino
treino = x[:,:50].reshape(-1,400).astype(np.float32) # Size = (2500,400)
teste = x[:,50:100].reshape(-1,400).astype(np.float32) # Size = (2500,400)

# Cria rotulos
k = np.arange(10)
treino_rotulos = np.repeat(k,250)[:,np.newaxis]
teste_rotulos = treino_rotulos.copy()

# Treina e testea com k=5
knn = cv2.ml.KNearest_create()
knn.train(treino,cv2.ml.ROW_SAMPLE,treino_rotulos)
ret,resultado,vizinhos,distancia = knn.findNearest(teste,k=5)

# Checa acuracia da classificacao
# Compara resultadoados da classificacao com informacao do dataset
correspondencias = resultado==teste_rotulos
acertos = np.count_nonzero(correspondencias)
acuracia = acertos*100.0/resultado.size
print acuracia

np.savez('dadosKnn.npz',treino=treino, treino_rotulos=treino_rotulos)

with np.load('dadosKnn.npz') as data:
    print data.files
    treino = data['treino']
    treino_rotulos = data['treino_rotulos']
