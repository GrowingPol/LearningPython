'''Clase Pública'''

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre


p1 = Persona("Juan")
print(p1.nombre)

p1.nombre = "Pepe"
print(p1.nombre)
print()

'''Clase Privada''' #Se agrega dble guion bajo a los atributos/ Solo modificable dentro de la clase

class PersonaPrivada:
    def __init__(self, n):
        self.__nombre = n
        self.__edad = 20

    @property               #decorador
    def get_Nombre(self):
        return self.__nombre

    def set_Nombre(self, nombre):
        self.__nombre = nombre

    def get_Edad(self):
        return self.__edad

    def set_Edad(self, edad):
        self.__edad = edad


p2 = PersonaPrivada("Daniel")
#print(p2.__nombre) MArca error
print(p2.get_Nombre) # Ya que tiene decorador de property. no es necesario los paréntesis para su ejecución
print(p2.get_Edad())
print()

p2.__nombre = "Pancho"

#p2.nombre = "Alex"
#print(p2.__nombre) marca error
p2.set_Nombre("Alex")
p2.set_Edad(1)
#p2.__edad = 5 #no lo toma
print(p2.get_Nombre)
print(p2.get_Edad())