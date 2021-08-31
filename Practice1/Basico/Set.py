#No puede tener duplicados
#No mantiene ningún orden, no tiene índices
#No se pueden modificar sus elementos, pero si agregar y remover elementos

planetas = {"Marte", "Jupiter", "Venus"}
print(planetas)
#largo
print(len(planetas))
#Revisar si el elemento esta en el set
print("Marte" in planetas)

#agregar elementos al set
planetas.add("Tierra")
print(planetas)
#eliminar con remove posiblemente arroja excepcion si el elemento no está
planetas.remove("Venus")
print(planetas)
#eliminar con discard no arroja excepcion si ele elemento ya no está
planetas.discard("Venus")
planetas.discard("Jupiter")
print(planetas)

#eliminar el set
del planetas
print(planetas)