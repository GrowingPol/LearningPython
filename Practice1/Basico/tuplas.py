# cuando se inicializa ya no se puede cambiar el elemento

#Tupla mantiene el orden, pero ya no se puede modificar

frutas = ("Naranja","Plátano","Guayaba")
print(frutas)

#largo de la tupla
print(len(frutas))

#acceder al elemento
print(frutas[1])
print(frutas[-1])
print(frutas[:2])
print(frutas[1:])

#modificar indirectamente
frutaList = list(frutas)
print(frutaList)
frutaList[1] = "Papaya"
frutas = tuple(frutaList)
print(frutas)

for fruta in frutas:
    print(fruta,end=" ") #Parametros de print

#No podemos agregar elementos a una Tupla, ni tampoco eliminarlos
#Si podemos borrar la tupla

del frutas