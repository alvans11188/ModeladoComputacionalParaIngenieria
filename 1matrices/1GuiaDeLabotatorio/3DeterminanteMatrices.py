import numpy as np
print("DETERMINANTE DE UNA MATRIZ\n")
#EJERCICIO 1
A1=np.array([[4,2],[3,1]])
det1=np.linalg.det(A1)
print("Ejercicio 1 - Determinante:\n",det1,"\n")
if (det1==0):
    print("NO TIENE INVERSA")
else:
    print("TIENE INVERSA")

    
#EJERCICIO 2: 
A2=np.array([[1,2,3],[0,1,4],[5,6,0]])
det2=np.linalg.det(A2)
print("Ejercicio 2 - Determinante:\n",det2,"\n")

#EJERCICIO 3
A3 = np.array([[2, 0, 1, 3], 
               [1, 2, 0, 4], 
               [3, 1, 2, 5], 
               [0, 2, 3, 1]]) 
det3 = np.linalg.det(A3) 
print("Ejercicio 3 - Determinante:\n", det3, "\n") 

#EJERCICIO 4 : terminantede una matriz 3x3 triangular
A4 = np.array([[2, 1, 0], 
                [0, 3, 4], 
                [0, 0, 5]]) 
det4 = np.linalg.det(A4) 
print("Ejercicio 4 - Determinante:\n", det4, "\n")