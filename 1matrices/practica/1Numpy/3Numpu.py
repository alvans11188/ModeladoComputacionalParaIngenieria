import numpy as np
filas=int(input("Ingrese el numero de filas "))
columnas=int(input("Ingrese el numero de columnas"))

matriz=np.zeros((filas,columnas))
print("Ingrese los datos de la matriz")
for i in range(filas):
    for j in range(columnas):
        valor = float(input(f"Ingrese el elemento [{i}][{j}]"))
        matriz[i][j]=valor
print('')
print(matriz)