class MiClase:
    variableDeClase = "Hola"

    def __init__(self,variableDeInstancia):
        self.variableDeIntancia = variableDeInstancia



print(MiClase.variableDeClase)
#print(MiClase.variableDeInstancia) # Lanza error porque no se le ha asignado valor y está referenciada a l los objetos y no   a la clase en sí misma

MiClase.variableDeInstancia = "Modificada la Variable de Instancia desde la Clase"
print(MiClase.variableDeInstancia)         #La variable de Instancia se asoció a la clase
objeto1 = MiClase("Variable de Instancia") #La variable de Instancia se asoció al objeto
print(objeto1.variableDeIntancia)
print()

#Podemos acceder a las variables de clase desde el objeto
print("Variable Obj 1: ", objeto1.variableDeClase)

#Podemos acceder a las variables de clase desde el nombre de la clase
print("Variable Clase: ", MiClase.variableDeClase)

print()

#Modificar el valor de la varible de la clase desde el objeto
objeto1.variableDeClase = "Hola Objeto 1"
print("Variable Obj 1: ", objeto1.variableDeClase)
print("Variable Clase: ", MiClase.variableDeClase)
print()


#Modificar el valor de la variable de clase desde la clase
#Se heredará el valor de la variable de clase de la clase, hasta que éste se modifique desde el objeto
objeto2 = MiClase("VariableDeInstancia 2")
objeto3 = MiClase("VatiableDeInstancia 3")
MiClase.variableDeClase = "Hola Clase"
print("Variable Clase: ", MiClase.variableDeClase)
print("Variable Obj 1: ", objeto1.variableDeClase)
print("Variable Obj 2: ", objeto2.variableDeClase)
print("Variable Obj 3: ", objeto3.variableDeClase)
