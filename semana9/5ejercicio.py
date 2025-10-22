# ===============================================
# EJERCICIO 5 - Interpolación de Lagrange
# Enfriamiento de un líquido
# Puntos: (0,90), (5,70), (10,55)
# ===============================================

import numpy as np
import matplotlib.pyplot as plt

# ---- Datos ----
x_points = np.array([0.0, 5.0, 10.0])     # Tiempo (min)
y_points = np.array([90.0, 70.0, 55.0])   # Temperatura (°C)
x_eval = 7.0                              # Evaluar a los 7 minutos

# ---- Función para obtener coeficientes del polinomio de Lagrange ----
def lagrange_poly_coeffs(xs, ys):
    n = len(xs)
    result = np.zeros(n)
    for i in range(n):
        xs_excl = np.delete(xs, i)
        numer_coeffs = np.poly(xs_excl)           # coef. del polinomio (x - x_j)
        denom = np.prod(xs[i] - xs_excl)          # denominador del L_i
        if len(numer_coeffs) < len(result):
            numer_coeffs = np.pad(numer_coeffs, (len(result) - len(numer_coeffs), 0), 'constant')
        result = result + ys[i] * numer_coeffs / denom
    return result

# ---- Construir polinomio y evaluar ----
coeffs = lagrange_poly_coeffs(x_points, y_points)
P = np.poly1d(coeffs)
y_eval = P(x_eval)

print("=== EJERCICIO 5 ===")
print("Polinomio interpolador P(x):")
print(P)
print(f"P({x_eval}) = {y_eval:.6f} °C")

# ---- Graficar ----
x_plot = np.linspace(0, 10, 200)
y_plot = P(x_plot)

plt.figure(figsize=(7,4))
plt.plot(x_plot, y_plot, label='Polinomio de Lagrange')
plt.scatter(x_points, y_points, color='orange', label='Datos originales')
plt.scatter([x_eval], [y_eval], color='red', marker='x', label=f'P({x_eval}) = {y_eval:.2f}°C')
plt.title("Enfriamiento de un líquido - Interpolación de Lagrange")
plt.xlabel("Tiempo (min)")
plt.ylabel("Temperatura (°C)")
plt.grid(True)
plt.legend()
plt.show()
