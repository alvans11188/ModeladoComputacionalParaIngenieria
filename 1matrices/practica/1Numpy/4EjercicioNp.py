#cree una matriz de 3 dimensiones usando numpy

import numpy as np

n=int(input())
fila=columna=n
matriz1=np.zeros((n,n,n))
contador=0
for i in range(n):
    for j in range(n):
        for k in range(n):
          matriz1[i][j][k]  = contador=contador+1

print(matriz1)

print(np.shape(matriz1))