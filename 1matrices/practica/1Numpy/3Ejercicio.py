#cambia entre dimensiones de un arreglo n x n usando libreria numpy

import numpy as gaaa # el np peude ser cambiado por otras prefijos sin afectar a la funcion general

#n=int(input("Ingrese el tamanio de la matriz"))
#fila=columna=n
fila=2
columna=4
matriz1=gaaa.zeros((fila,columna))
contador=0
for i in range(fila):
    for j in range(columna):
        
        matriz1[i][j]= contador=contador+1

print(matriz1)

#intercambio entre filas y columnas
matriz1=matriz1.reshape(4,2)
print(matriz1)
