#Determina las dimensiones de la matriz usando numpy
import numpy as np

n=int(input("Ingrese el tamanio de la amtriz"))
fila=columna=n
contador=0
matriz1=np.zeros((fila,columna))

for i in range(fila):
    for j in range(columna):
        contador=contador+1
        matriz1[i][j]=contador

print('las dimensiones de la amtriz 1son: ',matriz1)

#determinacion de las dimensiones
print(np.shape(matriz1))
print('')

print("MATRIZ 2 : ",'')
matriz2=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(matriz2)
print('las dimensiones de la amtriz 2 son: ',np.shape(matriz2))