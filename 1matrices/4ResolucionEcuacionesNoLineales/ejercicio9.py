import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def ej1(vars):
    x, y,z = vars
    return [np.sin(x) + y - 2, y**2 + z - 3, x + z**2 - 4]





sol=fsolve(ej1, [1, 1, 1])
print("Ejercicio 9 - solucion aproximada (x,y,z) =", sol)