from Color import Color
from FiguraGeometrica import FiguraGeometrica

class Cuadrado(FiguraGeometrica,Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def __str__(self):
      return "lado: " + str(self.getAncho()) + ", color: " + str(self.getColor())


    def area(self): # Si no se definiera este metodo, se convirtiria en clase abstracta debido a su herencia de FiguraGeometrica
        return float(self.getAncho()) * float(self.getAncho())