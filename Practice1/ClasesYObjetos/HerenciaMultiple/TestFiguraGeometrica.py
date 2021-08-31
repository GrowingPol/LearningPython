from Cuadrado import Cuadrado
from Rectangulo import Rectangulo
from FiguraGeometrica import FiguraGeometrica

cuadrado1 = Cuadrado(10, "Rojo")
rectangulo1 = Rectangulo(3,4,"Verde")

print(cuadrado1.__str__())
print()
print(str(cuadrado1.area()))

print()

print(Cuadrado.mro()) #Orden de ejecución de las clases
print()

print(rectangulo1.__str__())
print(rectangulo1.area())

'''No se puede instanciar una clase abstracta'''
#figuraGeometrica1 = FiguraGeometrica()
