#include <iostream>
#cree una amtriz 6 x 6 que imprima lo que esta acontinuacion

#1 7 13 19 25 31
#2 8 14 20 26 32
#3 9 15 21 27 33
#4 10 16 22 28 34
#5 11 17 23 29 35
#6 12 18 24 30 36
contador=0
for i in range(1,7):
    contador=contador+1
    contador2=contador
    for j in range(1,7):
        print(contador2,end=' ')
        contador2=contador2+6
    print('')