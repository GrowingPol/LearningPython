class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


    def __str__(self):
        return "Nombre: "+ self.nombre + ", Edad: " + str(self.edad)