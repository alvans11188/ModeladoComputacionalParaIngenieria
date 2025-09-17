import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
def ej(vars):
    x, y = vars
    return [ np.exp(x) + y - 3, x**2 + y**2 -5]
plt.show()

# Resolver 
sol = fsolve(ej, [1, 1])
print("Ejercicio 4:", sol)

#graficar
x = np.linspace(-3, 3, 400) 
y = np.linspace(-3, 3, 400) 
X, Y = np.meshgrid(x, y)

plt.contour(X, Y, np.exp(X) + Y - 3, [0], colors='r') 
plt.contour(X, Y, X**2 + Y**2 - 5,[0], colors='b') 
plt.plot(sol[0], sol[1], 'go') 
plt.title("Ejercicio 4") 
plt.xlabel("x"); 
plt.ylabel("y") 
plt.grid(True); 
plt.show()