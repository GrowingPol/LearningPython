class PersonaHumana:
    def __init__(self, nombre, edad):  # Todos los elementos de una clase en python deben recibir argumento self
        self.nombre = nombre
        self.edad = edad


# Modificar Valores
PersonaHumana.nombre = "Alejandro"
PersonaHumana.edad = 29

# Acceder a los valores
print(PersonaHumana.nombre)
print(PersonaHumana.edad)

# Creación de un objeto
persona1 = PersonaHumana("Pepe", 12)
print(persona1.nombre)
print(persona1.edad)

persona2 = PersonaHumana("Marco", 40)