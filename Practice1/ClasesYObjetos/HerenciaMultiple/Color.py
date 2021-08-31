class Color:
    def __init__(self, color):
        self.__color = color

    def __str__(self):
        return "Color: " + str(self.__color)

    def setColor(self,color):
        self.__color = color

    def getColor(self):
        return self.__color