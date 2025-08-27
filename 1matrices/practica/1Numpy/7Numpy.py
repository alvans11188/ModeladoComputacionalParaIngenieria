#MUCHOS NUMEROS ALEATORIOS

from numpy import random
#enteros desde 0 y 10
numero = random.randint(10) 
print(numero)

#generacion de una matriz de 1 fila y 20 columnas
matriz1 = random.randint(10,size=(20)) 
print(matriz1)
print('')
#generacion de una matriz de 3 fila y 5 columnas
matriz1 = random.randint(10,size=(3,5)) 
print(matriz1)


#tambien es posible realizar con la funcion rand
#pero como no se puede incluir el parametros de hasta donde generar numeros aleatorios, simplemente seran puros decimales
matriz2 = random.rand(3,5) 
print(matriz2)