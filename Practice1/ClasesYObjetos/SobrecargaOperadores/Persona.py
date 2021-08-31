
class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    # El parámetro other será lo que se "sumará" a éste objeto
    def __add__(self, other):
        return self.nombre + " " + other.nombre

    def __sub__(self, other):
        return self.edad - other.edad



if __name__ == "__main__":
    persona1 = Persona("Juan",5)
    persona2 = Persona("Carlos",3)
    print(persona1 + persona2)
    print(persona1 - persona2)