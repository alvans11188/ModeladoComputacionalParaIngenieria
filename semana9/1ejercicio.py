# Ejercicio 1: Lagrange 
import numpy as np 
x_points = np.array([1.0, 2.0, 4.0]) 
y_points = np.array([2.0, 3.0, 1.0]) 
def lagrange_eval(x, xs, ys): 
    n = len(xs) 
    total = 0.0 
    for i in range(n): 
        li = 1.0 
        for j in range(n): 
            if j != i: 
              li *= (x - xs[j]) / (xs[i] - xs[j]) 
        total += ys[i] * li 
    return total 
x_eval = 3.0 
print("P(3) (Lagrange) =", lagrange_eval(x_eval, x_points, y_points)) 