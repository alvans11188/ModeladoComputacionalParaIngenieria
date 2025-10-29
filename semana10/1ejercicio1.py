import numpy as np 
def divided_differences(xs, ys): 
    n = len(xs) 
    table = np.zeros((n, n))
    table[:,0] = ys 
    for j in range(1, n): 
        for i in range(n - j): 
            table[i,j] = (table[i+1,j-1] - table[i,j-1]) / (xs[i+j] - xs[i]) 
            coef = table[0, :] 
    return coef, table 
def newton_eval(coef, xs, x): 
    n = len(coef) 
    result = coef[n-1] 
    for k in range(n-2, -1, -1): 
        result = result * (x - xs[k]) + coef[k] 
    return result 
xs = np.array([1.0, 2.0, 3.0, 4.0]) 
ys = np.array([1.0, 4.0, 9.0, 16.0]) 
coef, table = divided_differences(xs, ys) 
print('Coeficientes (diferencias divididas, desde f[x0]):', coef) 
print('\nTabla completa de diferencias divididas:\n', table) 
# Evaluación en x=2.5 
x_test = 2.5 
y_test = newton_eval(coef, xs, x_test) 
print(f'P_3({x_test}) =', y_test)