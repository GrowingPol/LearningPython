class Persona:
    def __init__(this, n, e, *v, **a): #self puede ser cambiado por cualquiera variable, siempre y cuando se respete después
        this.nombre = n       #Los Parámetros de las funciones en las clases tambien pueden ser cualquiera, pues los
        this.edad = e         # atributos realmente toman su valor
        this.valores = v      # *v para tuplas
        this.diccionario = a


    def desplegar(self):
        print("Nombre: ", self.nombre)
        print("edad", self.edad)
        print("tupla:", self.valores )
        print("diccionario:", self.diccionario)


'''Asterisco significa que se tomaran todos los valores como tupla(siendo un parámetro opcional)
Doble Asterisco (Parámetro tambien opcional), tomará todos los keywords'''


p1 = Persona("Juan",30)
print(p1.desplegar())
print()

p2 = Persona("Maria", 12, 4,3,5,6)
print(p2.desplegar())
print()

p3 = Persona("Dulce", 20, 10,2, m="manzana", p="platano")
print(p3.desplegar())
print()

