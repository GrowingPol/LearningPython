class Persona:
    def __init__(self, nombre, aPaterno, aMaterno):
        self.nombre = nombre                 #público
        self._apellidoPaterno = aPaterno     #Protegido
        self.__apellidoMaterno = aMaterno    #Privado

    def __metodoPrivado(self):
        print(self.nombre)
        print(self._apellidoPaterno)
        print(self.__apellidoMaterno)

    def metodoPublico(self):
        self.__metodoPrivado()

    def getApellidoMaterno(self):
        return self.__apellidoMaterno

    def setAppellidoMaterno(self,apellidoMat):
        self.__apellidoMaterno = apellidoMat


p1 = Persona("Pancho","Pérez", "Espinoza")
print(p1.metodoPublico())
print()
print(p1.nombre)
print(p1._apellidoPaterno) #Si se puede acceder porque es un atributo reservado, sin embargo, anuncia una recomendacion de acceder de este método sino con get y set
#print(p1.__apellidoMaterno) Este no va a funcionar porque es un atributo pivado
print(p1.getApellidoMaterno())