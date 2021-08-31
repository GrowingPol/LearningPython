nombres = ["Juan", "Karla", "Ricardo", "María"]
print(nombres)

#Conocer el largo de la lista
print(len(nombres))

#elemento 0
print(nombres[0])

#Ultimo elemento de la lista
print(nombres[-1])

#imprimir rango
print(nombres[0:2])  #imprime elemento 0 y 1
print(nombres[:2])   #imprime elemento desde el 0 hasta el 1
print(nombres[1:])   #Imprime elemento desde el 1 hasta el final

#cambiar elementos
nombres[3] = "Pedro"
for nombre in nombres:
    print(nombre)

#Revisar si existe un elemento en la lista
if "Karla" in nombres:
    print("Karla si existe")
else:
    print("el nombre no existe")

#Agregar un elenemto a la lista al final

nombres.append("Marythe")
for nombre in nombres:
    print(nombre)

#Insertar un nuevo elemento en cierta posicion
nombres.insert(1,"Diana")
print(nombres[:])

#Eliminar elementos
nombres.remove("Pedro")
print(nombres)

#remover el ultimo elemento de la lista
nombres.pop()
print(nombres)

#remover el indice indicado de la lista
del nombres[0]
print(nombres)

#limpiar todos los elementos de la lista

nombres.clear()
print(nombres)

#eliminar variaable de lista
del nombres
