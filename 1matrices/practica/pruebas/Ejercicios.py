#rellenar de 1 solo la diagonal de la matriza y el resto con 0
#intento 1
for i in range(1,6):
    for j in range (1,6):
        print(0,end='')
    print('')
print('')
#intento 2
for i in range(1,6):
    for j in range (1,6):
        if (i==j): 
            print(1,end=' ')
        else:
            print(0,end=' ')
    print(' ')