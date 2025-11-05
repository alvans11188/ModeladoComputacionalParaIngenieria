#METODO POR APROXIMACIONE DE MINIMOS CUADRADOS
import numpy as np 
import matplotlib.pyplot as plt
x = np.array([10, 20, 30, 40]) 
y = np.array([6, 25, 60, 110]) 
# Ajuste cuadrático 
coef = np.polyfit(x, y, 2) 
p = np.poly1d(coef) 
y_pred = p(x) 
ECM = np.mean((y - y_pred)**2) 
y_pred_25 = p(25)
print("Coeficientes del modelo:", coef)
print(f"Prediccion para X=5 cm : {y_pred_25:.2f} W")
print(f"Error cuadrático medio: {ECM:.4f}") 
# Gráfica 
x_fit = np.linspace(min(x), max(x), 100) 
plt.scatter(x, y, color='red', label='Datos experimentales') 
plt.scatter(25, y_pred_25, color='green', label=f'Predicción para X=5 cm: {y_pred_25:.2f} W')
plt.plot(x_fit, p(x_fit), color='green', label='Ajuste cuadrático') 
plt.title('Ajuste Polinomial por Mínimos Cuadrados') 
plt.xlabel('Velocidad x (m/s)') 
plt.ylabel('Distancia y (m)') 
plt.legend() 
plt.grid(True) 
plt.show() 