from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, alto, ancho, color):
        FiguraGeometrica.__init__(self, alto,ancho)
        Color.__init__(self, color)


    def __str__(self):
        return "Alto: " + str(self.getAlto()) + ", Ancho: " + str(self.getAncho()) + ", Color: " + str(self.getColor())

    def area(self):
        return self.getAncho() * self.getAlto()


