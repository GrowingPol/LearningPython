class Persona:

    contadorPersonas = 0

    def __init__(self,nombre,edad):
        Persona.contadorPersonas += 1
        self.idPersona = Persona.contadorPersonas
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Persona [{self.idPersona}, {self.nombre}, {self.edad}]"


persona1 = Persona("Juan", 18)
print(persona1)
persona2 = Persona("Maria", 20)
print(persona2)
persona3 = Persona("Eduardo", 30)
print(persona3)
print(Persona.contadorPersonas)