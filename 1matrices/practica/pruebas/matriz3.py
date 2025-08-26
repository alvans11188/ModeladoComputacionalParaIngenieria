#matriz bidimensional en python

for i in range(1,6):
    for j in range(1,6):
        print(f"Elemento [{i}][{j}]")


print('\n')
for i in range(1,7):
    print(i, end=' ')
print('')
# for anidado
#se manejan 2 variables 
for i in range(1,7): #valores entre 1 y 6
    for j in range(1,7):
        print(0, end=' ')
    print('') #salto de linea

#mostrando cordenadas de cada espacio de la amtriz
for i in range(1,7): 
    for j in range(1,7):
        print(f'({i},{j})', end=' ')
    print('') 