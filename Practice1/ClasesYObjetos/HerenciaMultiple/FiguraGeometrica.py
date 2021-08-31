#ABC = Abstract Base Class
from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self, alto, ancho):
        self.__alto = alto
        self.__ancho = ancho

    def __str__(self):
        return "alto: " + str(self.alto) + ", ancho: " + str(self.ancho)

    def setAncho(self, ancho):
        self.__ancho = ancho

    def getAncho(self):
        return self.__ancho

    def setAlto(self, alto):
        self.__alto = alto

    def getAlto(self):
        return self.__alto

    @abstractmethod   #obliga a las clases hijas a ddefinir éste método
    def area(self):
        pass


