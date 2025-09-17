import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

#EJERCICIO 3

def ej(vars):
    x, y = vars
    return [x**3 - y, x + y**2 - 4]
plt.show()

# Resolver
sol3 = fsolve(ej, [1, 1])
print("Ejercicio 3:", sol3)


# Graficar 
x = np.linspace(-3, 3, 400) 
y = np.linspace(-3, 3, 400) 
X, Y = np.meshgrid(x, y)


plt.contour(X, Y, X**3 - Y, [0], colors='r')
plt.contour(X, Y, X + Y**2 - 4, [0], colors='b')
plt.plot(sol3[0], sol3[1], 'go')
plt.title("Ejercicio 3")
plt.xlabel("x"); plt.ylabel("y")
plt.grid(True); plt.show()


