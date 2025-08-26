import numpy as np

filas = int(input("Número de filas: "))
columnas = int(input("Número de columnas: "))

matriz = np.zeros((filas, columnas))

print(f"Ingresa los valores para una matriz {filas}x{columnas}:")
for i in range(filas):
    for j in range(columnas):
        valor = float(input(f"Elemento [{i},{j}]: "))
        matriz[i, j] = valor

print("\nMatriz resultante:")
print(matriz)