from DispositivoEntrada import DispositivoEntrada

class Raton(DispositivoEntrada):
    contadorRatones = 0

    @classmethod
    def incrementarContadorRatones(cls):
        cls.contadorRatones += 1
        return cls.contadorRatones

    def __init__(self,tipoEntrada, marca):
        super().__init__(tipoEntrada,marca)
        self._idRaton = Raton.incrementarContadorRatones()

    def __str__(self):
        return f"[idRaton: {self._idRaton}, {super().__str__()}]"

    # @property
    # def idRaton(self):
    #     return self._idRaton
    #
    # @idRaton.setter
    # def idRaton(self,idRaton):
    #     self._idRaton = idRaton



if __name__ == "__main__":
    raton1 = Raton("wifi","HP")
    print(raton1)
    raton2 = Raton("usb", "laser")
    print(raton2)

