#SELECCION ALEATORIA

#permite escoge aleatoriamente un objeto
#similar a un sorteo, escogiendo 1 o varios

from numpy import random

nombres=["alex","juan","likidin","joshua"]
ganador= random.choice(nombres) #devuelve un elemento
print("El ganador es ", ganador)

