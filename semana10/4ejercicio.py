# EJERCICIO 4 
import numpy as np 
import math 
x_points = np.array([0, math.pi/4, math.pi/2]) 
y_points = np.sin(x_points) 
def newton_interp(x_data, y_data, x): 
    n = len(x_data) 
    coef = np.copy(y_data) 
    for j in range(1, n): 
        coef[j:n] = (coef[j:n] - coef[j-1:n-1]) / (x_data[j:n] - x_data[0:n-j]) 
    result = coef[-1] 
    for k in range(n-2, -1, -1): 
        result = result * (x - x_data[k]) + coef[k] 
    return result 
x_eval = math.pi / 3 
print("P(pi/3) =", newton_interp(x_points, y_points, x_eval)) 
print("Valor real =", math.sin(x_eval))