import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
#EJERCICIO 2

def ej(vars):
    x, y = vars
    return [np.sin(x) + y**2 - 1, x**2 + y - 2]
plt.show()

# Resolver
sol2 = fsolve(ej, [1, 1])
print("Ejercicio 2:", sol2)

#graficar
# Graficar 
x = np.linspace(-3, 3, 400) 
y = np.linspace(-3, 3, 400) 
X, Y = np.meshgrid(x, y)

plt.contour(X, Y, np.sin(X) + Y**2-1, [0], colors='r')
plt.contour(X, Y, X**2 + Y-2, [0], colors='b')
plt.plot(sol2[0], sol2[1], 'go')
plt.title("Ejercicio 2")
plt.xlabel("x");
plt.ylabel("y")
plt.grid(True);
plt.show()
