#Suma de una matris preestablecida
import numpy as np
from numpy import random
matriz1=random.randint(11,size=(4,4))
print(matriz1)
print('')
matriz2=random.randint(11,size=(4,4))
print(matriz2)
print('')
matriz3=np.zeros((4,4))
for i in range(4):
    for j in range(4):
        matriz3[i][j]=matriz1[i][j]+matriz2[i][j]

print(matriz3)

