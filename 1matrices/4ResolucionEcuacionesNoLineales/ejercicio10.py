import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def ej1(vars):
    x, y,z = vars
    return [x**2 + y - 1, y**2 + z - 2, z**2 + x - 3]





sol=fsolve(ej1, [1, 1, 1])
print("Ejercicio 9 - solucion aproximada (x,y,z) =", sol)