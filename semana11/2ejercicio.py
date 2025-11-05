#METODO POR APROXIMACIONE DE MINIMOS CUADRADOS
# AJUSTE CUADRÁTICO GRADO 2 
import numpy as np 
import matplotlib.pyplot as plt
x = np.array([1, 2, 3, 4]) 
y = np.array([6, 11, 18, 27]) 
# Ajuste cuadrático 
coef = np.polyfit(x, y, 2) 
p = np.poly1d(coef) 
y_pred = p(x) 
ECM = np.mean((y - y_pred)**2) 
print("Coeficientes del modelo:", coef) 
print(f"Error cuadrático medio: {ECM:.4f}") 
# Gráfica 
x_fit = np.linspace(min(x), max(x), 100) 
plt.scatter(x, y, color='red', label='Datos experimentales') 
plt.plot(x_fit, p(x_fit), color='green', label='Ajuste cuadrático') 
plt.title('Ajuste Polinomial por Mínimos Cuadrados') 
plt.xlabel('x') 
plt.ylabel('y') 
plt.legend() 
plt.grid(True) 
plt.show() 