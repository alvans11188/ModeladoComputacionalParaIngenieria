#cree una matriz 6x6 con las siguientes caracteristicas

#A
#A B
#A B A
#A B A B
#A B A B A
#A B A B A B

#intento 1
for i in range(1,7):
    for j in range(1,7):
        if (i%2!=0):
            print('A',end=' ')
        else:
            print('B',end=' ')
    print('')

print('')
#intento 2
contador=1
for i in range(1,7):
    for j in range(1,7):
        if((i%2)&(j%2)==0):
            print('A',end=' ')
        else:
            print('B',end=' ')

    print('')
    contador=contador+1
print('')

#intento 3
contador=1
for i in range(1,7):
    for j in range(1,i+1):
        if((j%2)!=0):
            print('A',end=' ')
        else:
            print('B',end=' ')

    print('')
    contador=contador+1
print('')