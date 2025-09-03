import numpy as np 
 
# Ejercicio 1: Multiplicación de matrices 2x2 
A1 = np.array([[1, 2], 
               [3, 4]]) 
B1 = np.array([[2, 0], 
               [1, 2]]) 
print("Ejercicio 1:\n", np.dot(A1, B1), "\n") 
 
# Ejercicio 2: Multiplicación de matrices 2x3 * 3x2 = 2x2 
A2 = np.array([[1, 2, 3], 
               [4, 5, 6]]) 
B2 = np.array([[7, 8], 
               [9, 10], 
               [11, 12]]) 
print("Ejercicio 2:\n", np.dot(A2, B2), "\n") 
 
# Ejercicio 3: Multiplicación de matrices 3x3 
A3 = np.array([[2, 0, 1], 
               [1, 3, 2], 
               [0, 4, 5]]) 
B3 = np.array([[1, 2, 3], 
               [4, 0, 6], 
               [7, 8, 9]]) 
print("Ejercicio 3:\n", np.dot(A3, B3), "\n") 
 
# Ejercicio 4: Multiplicación de matrices 3x2 * 2x3 = 3x3 
A4 = np.array([[1, 2], 
               [3, 4], 
               [5, 6]]) 
B4 = np.array([[7, 8, 9], 
               [10, 11, 12]]) 
print("Ejercicio 4:\n", np.dot(A4, B4), "\n")