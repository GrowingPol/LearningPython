class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):   #El metodo __Str__ viene desde la clase "Objeto" y sirve para
        return("nombre: "+ self.nombre + ", edad: "+ str(self.edad))


class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo): #Definir metodo init con atributos de clase padre más los de la clase hijaa
        super().__init__(nombre, edad) #inicializar Valores de la clase padre
        self.sueldo = sueldo           #Inicializar valores correspondientes a la clase

    def __str__(self):
        return(super().__str__() + ", Sueldo: " + str(self.sueldo)) #Con super se llaman metodos de la clase padre


motociclista = Empleado("Pancho",33,3000)
hombre = Persona("Manuel", 20)

print(motociclista)
print(hombre)

motociclista.nombre = "Carlos"




