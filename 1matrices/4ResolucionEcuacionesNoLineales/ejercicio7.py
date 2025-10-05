import numpy as np
from scipy.optimize import fsolve

sistema = lambda v: [ 
    np.exp(v[0]) + v[1]**2 + v[2] - 7, 
    v[0] + np.exp(v[1]) + v[2]**2 - 8, 
    v[0]**2 + v[1] + np.exp(v[2]) - 9 
]   

sol=fsolve(sistema, [1, 1, 1])
print("Ejercicio 7 - solucion aproximada (x,y,z) =", sol)