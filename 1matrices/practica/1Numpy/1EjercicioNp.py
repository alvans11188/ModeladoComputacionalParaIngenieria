#cree una matriz n x n y sumela con otra matriz 
import numpy as np
n=int(input("Ingrese el tamanio de la matriz"))
columna=fila=n

matriz1=np.zeros((fila,columna))
contador=0
for i in range(fila):
    for j in range(columna):
        #valor = float(input(f"Ingrese valor de [{i}][{j}]"))
        contador=contador+1
        matriz1[i][j]=contador
    
print(matriz1)
print('')

matriz2=np.zeros((fila,columna))
for i in range(fila):
    for j in range(columna):
        #valor = float(input(f"Ingrese valor de [{i}][{j}]"))
        contador=contador+1
        matriz2[i][j]=contador
    
print(matriz2)
print("Matriz resultante de la suma: ",'')
matriz3=np.zeros((fila,columna))
for i in range(fila):
    for j in range(columna):
        matriz3[i][j]=matriz1[i][j]+matriz2[i][j]

print(matriz3)
