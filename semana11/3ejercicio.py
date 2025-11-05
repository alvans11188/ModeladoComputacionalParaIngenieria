#EJERCICIO 3
#Aislamiento térmico — relación entre el espesor de aislamiento (cm) y la pérdida de calor (W) medida 
#en un panel. Queremos un modelo lineal para estimar la pérdida de calor según el espesor. 
#METODO POR APROXIMACIONE DE MINIMOS CUADRADOS
import numpy as np 
import matplotlib.pyplot as plt 
# Datos experimentales 
x = np.array([2, 4, 6, 8]) 
y = np.array([120, 95, 70, 50]) 
# Ajuste lineal (grado 1)
coef = np.polyfit(x, y, 1) 
p = np.poly1d(coef) 
# Predicción y error 
y_pred = p(x) 
ECM = np.mean((y - y_pred)**2) 
#prediccion para x=5cm
y_pred_5cm = p(5)
print("Coeficientes del modelo:", coef) 
print(f"Prediccion para X=5 cm : {y_pred_5cm:.2f} W")
print(f"Error cuadrático medio: {ECM:.4f}") 
# Gráfica 
plt.scatter(x, y, color='red', label='Datos') 
plt.plot(x, y_pred, color='blue', label=f'Ajuste:y={coef[0]:.2f}x+{coef[1]:.2f}') 
plt.scatter(5, y_pred_5cm, color='green', label=f'Predicción para X=5 cm: {y_pred_5cm:.2f} W')
plt.title('Ajuste Lineal por Mínimos Cuadrados') 
plt.xlabel('Espesor de aislamieno (cm)') 
plt.ylabel('Perdida de calor (W)') 
plt.legend() 
plt.grid(True) 
plt.show() 