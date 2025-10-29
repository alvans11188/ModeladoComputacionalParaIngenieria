# EJERCICIO 3 
import numpy as np 
import math 
x_points = np.array([0, 1, 2]) 
y_points = np.array([math.e**x for x in x_points]) 
def newton_interp(x_data, y_data, x): 
    n = len(x_data) 
    coef = np.copy(y_data) 
    for j in range(1, n): 
        coef[j:n] = (coef[j:n] - coef[j-1:n-1]) / (x_data[j:n] - x_data[0:n-j]) 
    result = coef[-1] 
    for k in range(n-2, -1, -1): 
        result = result * (x - x_data[k]) + coef[k] 
    return result 
print("P(1.5) =", newton_interp(x_points, y_points, 1.5)) 