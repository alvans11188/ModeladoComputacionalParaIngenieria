#---- EJERCICIO 3 ------
# EDO: y' = -2*y
def f(t, y):
    return -2 * y
# Condiciones iniciales
t0 = 0
y0 = 1
h = 0.1
print("=== Un paso con h = 0.1 ===")
# ===============================
# Método de Euler
# ===============================
y_euler = y0 + h * f(t0, y0)
print(f"Euler: y(0.1) = {y_euler:.6f}")
# ===============================
# Runge-Kutta de 2do orden (Heun)
# ===============================
k1 = f(t0, y0)
k2 = f(t0 + h, y0 + h*k1)
y_rk2 = y0 + (h/2)*(k1 + k2)
print(f"RK2 (Heun): y(0.1) = {y_rk2:.6f}")
# ===============================
# Runge-Kutta de 4to orden
# ===============================
k1 = f(t0, y0)
k2 = f(t0 + h/2, y0 + (h/2)*k1)
k3 = f(t0 + h/2, y0 + (h/2)*k2)
k4 = f(t0 + h, y0 + h*k3)
y_rk4 = y0 + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
print(f"RK4: y(0.1) = {y_rk4:.6f}")
