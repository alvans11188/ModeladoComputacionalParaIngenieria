#METODO DE GAUSS-JORDAN 
 
import numpy as np
def gauss_jordan(A, b): 
    n = len(b) 
    M = np.hstack([A.astype(float), b.reshape(-1,1)]) 
     
    for k in range(n): 
        M[k] = M[k] / M[k][k] 
        for i in range(n): 
            if i != k: 
                M[i] = M[i] - M[i][k] * M[k] 
    return M[:, -1] 
 
# Ejemplo 1 
A = np.array([[1, 2], 
              [3, -1]]) 
b = np.array([5, 4]) 
print("Solución Ejercicio 1 (Gauss-Jordan):", gauss_jordan(A, b)) 
 
# Ejemplo 2 
A = np.array([[2, 1, -1], 
              [-3, -1, 2], 
              [-2, 1, 2]]) 
b = np.array([8, -11, -3]) 
print("Solución Ejercicio 2 (Gauss-Jordan):", gauss_jordan(A, b)) 