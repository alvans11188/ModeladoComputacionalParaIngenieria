#cree 2 matrices y realice la suma correspondiente
#creacion de 2 matrices , generadas continuamente

import numpy as np
n=int(input())
fila=columna=n
contador=0
matriz1=np.zeros((fila,columna))
for i in range(fila):
    for j in range(columna):
        contador=contador+1
        matriz1[i][j]=contador

print(matriz1)

matriz2=np.zeros((fila,columna))
for i in range(fila):
    for j in range(columna):
        contador+=1
        matriz2[i][j]=contador

print(matriz2)