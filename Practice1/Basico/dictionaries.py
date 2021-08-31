diccionario = {
    "IDE": "Integrated Development Environment",
    "OOP": "Object Oriented Programming",
    "DBMS": "Database Management System"
}

print(diccionario)
#largo
print(len(diccionario))
#acceder a elementos (valor de llaves)
print(diccionario["IDE"])
#otra forma
print(diccionario.get("OOP"))

#modificar valores
diccionario["IDE"] = "Integrated development environment"
print(diccionario["IDE"])

#iterar
for termino in diccionario: #Terminó será cada una de las llaves
    print(termino)
for termino in diccionario:
    print(diccionario[termino]) #valor asociado a las llaves

for termino in diccionario.values(): #Accedemos a los valores, pero no a las llaves
    print(termino)

#Comprobar existencia de elementos
print("IDE" in diccionario)

#Agregar elementos
diccionario["PK"] = "Primary Key"
print(diccionario)

#remover elementos
diccionario.pop("DBMS")
print(diccionario)

#limpiar
diccionario.clear()
print(diccionario)

#eliminar diccionario
del diccionario
print(diccionario)