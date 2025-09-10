# MÉTODO DE TRIANGULACIÓN DE GAUSS
import numpy as np 
def gauss_elimination(A, b): 
    n = len(b) 
    M = np.hstack([A.astype(float), b.reshape(-1,1)])
    for k in range(n): 
        # Pivoteo parcial 
        max_row = np.argmax(abs(M[k:,k])) + k 
        M[[k, max_row]] = M[[max_row, k]] 
         
        for i in range(k+1, n): 
            factor = M[i][k] / M[k][k] 
            M[i] = M[i] - factor * M[k] 
     
    # Sustitución regresiva 
    x = np.zeros(n) 
    for i in range(n-1, -1, -1): 
        x[i] = (M[i, -1] - np.dot(M[i,i+1:n], x[i+1:n])) / M[i,i] 
    return x 

# Ejemplo 1 
A = np.array([[2, 3], 
              [1, -1]]) 
b = np.array([8, 1]) 
print("Solución Ejercicio 1 (Gauss):", gauss_elimination(A, b)) 
 
# Ejemplo 2 
A = np.array([[3, 2, -1], 
              [2, -2, 4], 
              [-1, 0.5, -1]]) 
b = np.array([1, -2, 0]) 
print("Solución Ejercicio 2 (Gauss):", gauss_elimination(A, b))