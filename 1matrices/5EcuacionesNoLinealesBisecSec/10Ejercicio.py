# EJERCICIO 10: f(x) = ln(x+2) - x
import math

def f(x): 
    return math.log(x+2) - x

def bisection_iterations(f,a,b,tol=1e-12,maxit=100):
    fa,fb = f(a), f(b)
    if fa*fb > 0: 
        raise ValueError("No cambio de signo en [a,b]")
    rows = []
    for k in range(1,maxit+1):
        r = (a+b)/2.0
        fr = f(r)
        rows.append((k,a,b,r,fr))
        if abs(fr) < tol or (b-a)/2.0 < tol: 
            break
        if fa*fr < 0:
            b,fb = r,fr
        else:
            a,fa = r,fr
    return rows

def secant_iterations(f,x0,x1,tol=1e-12,maxit=100):
    rows = []
    for k in range(1,maxit+1):
        fx0,fx1 = f(x0), f(x1)
        if fx1 == fx0: 
            raise ZeroDivisionError("Denominador cero en secante")
        x2 = x1 - fx1*(x1-x0)/(fx1-fx0)
        fx2 = f(x2)
        rows.append((k,x0,x1,x2,fx1,fx2))
        if abs(x2-x1) < tol or abs(fx2) < tol: 
            break
        x0,x1 = x1,x2
    return rows

# Datos del ejercicio 10
a,b = 0.0, 2.0
x0,x1 = 0.5, 2.0

bis = bisection_iterations(f,a,b)
sec = secant_iterations(f,x0,x1)

print("Bisección (primeras 6 iteraciones / última):")
for row in bis[:6]: 
    print(f"iter= {row[0]}, a={row[1]:.12f}, b={row[2]:.12f}, r={row[3]:.12f}, f(r)={row[4]:.3e}")
print("...",bis[-1])

print("\nSecante (todas las iteraciones):")
for row in sec: 
    print(f"iter= {row[0]}, x0={row[1]:.12f}, x1={row[2]:.12f}, x2={row[3]:.12f}, f(x1)={row[4]:.3e}, f(x2)={row[5]:.3e}")

print("\nResultado final:")
print("Bisección raíz =", bis[-1][3], "iter =", bis[-1][0])
print("Secante raíz   =", sec[-1][3], "iter =", sec[-1][0])
