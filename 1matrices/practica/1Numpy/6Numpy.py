#NUMEROS ALEATORIOS EN NUMPY
#se tocara el modulo random 
from numpy import random

numero = random.randint(10)
#el 10 indicara que generara un nuemro aleatorio entre 1 y 10, pero sin el 10
print(numero)

for i in range(10):
    numero = random.randint(10)
    print(numero)

#otra funcion principal es otra que es rand
numero2=random.rand() #generara un numero decimal entre 0 y 1
print(numero2) #se generara con muchos decimales, para acotar esto se usara lo siguiente:
print(round(numero2,3)) #se realizara un redondero hasta 3 decimales
 
#otra obcion es si desea generar un numero entre cierto rango se realizara lo siguiente

print(round(numero2,3)+5) # de esta forma se genera entre 5 y 6

