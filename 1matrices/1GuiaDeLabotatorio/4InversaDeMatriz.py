import numpy as np
print("INVERSA DE MATRICES\n")
#EJERCICIO 1: inversa matriz 2x2
A1=np.array([[4,7],[2,6]])
inv1=np.linalg.inv(A1)
print("EJERCICIO 1 - INVERSA DE A1:\n",inv1,"\n")

#EJERCICIO 2: inversa matriz  3x3
A2 = np.array([[1, 2, 3], 
               [0, 1, 4], 
                [5, 6, 0]]) 
inv2 = np.linalg.inv(A2) 
print("Ejercicio 2 - Inversa de A2:\n", inv2, "\n") 

# Ejercicio 3: Matriz inversa de una 4x4 
A3 = np.array([[1, 2, 0, 1], 
               [0, 1, 3, 2], 
               [2, 0, 1, 1], 
               [1, 1, 0, 1]]) 
inv3 = np.linalg.inv(A3) 
print("Ejercicio 3 - Inversa de A3:\n", inv3, "\n")

# Ejercicio 4: Matriz inversa de una triangular superior 3x3 
A4 = np.array([[2, 1, 1], 
                [0, 3, 2], 
               [0, 0, 4]]) 
inv4 = np.linalg.inv(A4) 
print("Ejercicio 4 - Inversa de A4:\n", inv4, "\n")