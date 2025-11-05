#METODO POR APROXIMACIONE DE MINIMOS CUADRADOS
import numpy as np 
import matplotlib.pyplot as plt 
# Datos experimentales 
x = np.array([0, 1, 2, 3]) 
y = np.array([1, 2, 2, 4]) 
# Ajuste lineal (grado 1)
coef = np.polyfit(x, y, 1) 
p = np.poly1d(coef) 
# Predicción y error 
y_pred = p(x) 
ECM = np.mean((y - y_pred)**2) 
print("Coeficientes del modelo:", coef) 
print(f"Error cuadrático medio: {ECM:.4f}") 
# Gráfica 
plt.scatter(x, y, color='red', label='Datos') 
plt.plot(x, y_pred, color='blue', label=f'Ajuste:y={coef[0]:.2f}x+{coef[1]:.2f}') 
plt.title('Ajuste Lineal por Mínimos Cuadrados') 
plt.xlabel('x') 
plt.ylabel('y') 
plt.legend() 
plt.grid(True) 
plt.show()
