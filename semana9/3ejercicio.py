# =============================================== 
# EJERCICIO 3 - Interpolación de Lagrange 
# Puntos: (-1,1), (0,0), (2,4) 
# =============================================== 
import numpy as np
import matplotlib.pyplot as plt 
 
# Datos 
x_points = np.array([-1.0, 0.0, 2.0]) 
y_points = np.array([1.0, 0.0, 4.0]) 
x_eval = 1.0 
 
# ---- Función para obtener coeficientes del polinomio de Lagrange ---- 
def lagrange_poly_coeffs(xs, ys): 
    n = len(xs) 
    result = np.zeros(n) 
    for i in range(n): 
        xs_excl = np.delete(xs, i) 
        numer_coeffs = np.poly(xs_excl) 
        denom = np.prod(xs[i] - xs_excl) 
        if len(numer_coeffs) < len(result): 
            numer_coeffs = np.pad(numer_coeffs, (len(result) - len(numer_coeffs), 0), 'constant') 
        result = result + ys[i] * numer_coeffs / denom 
    return result 
 
# ---- Construir polinomio y evaluar ---- 
coeffs = lagrange_poly_coeffs(x_points, y_points) 
P = np.poly1d(coeffs) 
y_eval = P(x_eval) 
 
print("=== EJERCICIO 3 ===") 
print("Polinomio interpolador P(x):") 
print(P) 
print(f"P({x_eval}) = {y_eval:.6f}") 

