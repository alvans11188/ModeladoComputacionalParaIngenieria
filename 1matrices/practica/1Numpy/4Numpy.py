#UNION DE 2 ARRAYS
#DIVISION DE UN ARRAY
#BUSQUEDA EN UN ARRAY
import numpy as np

#se tienen los 2 arreglos de 1 dimension
arreglo1=np.array([1,2,3])
arreglo2=np.array([4,5,6])


#se usara la funcion concatenate  , se encargara de unir los 2 arrays
#es importante que tengan las mismas dimensiones sino nos e pdoran juntar
arreglo3=np.concatenate((arreglo1,arreglo2))
print(arreglo1,'\n',arreglo2,'\n',arreglo3)

#se añade axis=0 para la concatenacion dependiendo del numero de dimensiones que requeramos
print('')
arreglo4=np.array([[1,2,3],[4,5,6]])
arreglo5=np.array([[4,5,6],[7,8,9]])
arreglo6=np.concatenate((arreglo4,arreglo5),axis=0)
print(arreglo6)

#DIVISION DE UN ARRAY
arreglo7=np.array_split(arreglo1,3)
print(arreglo7)

#BUSQUEDA EN UN ARRAY
#la funcion where devolvera donde se encuentra un determinado elemento, devolvera la posicion

buscar=np.where(arreglo3==1)
print(buscar)

arreglo8=np.array([1,2,1,1,2,3,2,4,3,3,])
buscar=np.where(arreglo8==2)
print(buscar)