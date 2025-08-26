#rellene una amtriz con nuemros del 1 al 6 y en la sgte linea del 6 al 1 y asi sucesivamente
#123456
#654321

#intento 1
contador =1
for i in range(1,7):
    for j in range (1,7):
        if (j % 2 != 0):
            print(contador,end=' ')
            contador =+1
        else:
            print(contador,end=' ')
            contador =-1
    print('')

#intento 2
print()
contador =1
for i in range(1,7):
    
    if (i % 2 != 0):
        contador=0
        for j in range(1,7):
            print(j,end=' ')
    else:
        contador = 6
        for j in range (1,7):
            print(contador,end= ' ')
            contador= contador-1
    print('')
        