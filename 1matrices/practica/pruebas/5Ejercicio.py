#cree una matriz triangular inferior
#1 0 0 0 0 0
#1 1 0 0 0 0
#1 1 1 0 0 0
#1 1 1 1 0 0
#1 1 1 1 1 0
#1 1 1 1 1 1
#error se imprime una matriz triangular superior Dx
for i in range(1,7):
    for j in range(1,7):
        if(i<=j):
            print (1,end=' ')
        else:
            print(0,end=' ')
    print('')
print('')
#matriz triangular superior
for i in range(1,7):
    for j in range(1,7):
        if(i>=j):
            print (1,end=' ')
        else:
            print(0,end=' ')
    print('')