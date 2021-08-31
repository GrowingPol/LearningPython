from DispositivoEntrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    contadorTeclados = 0

    @classmethod
    def incrementarcontadorTeclados(cls):
        cls.contadorTeclados += 1
        return cls.contadorTeclados

    def __init__(self,tipoEntrada, marca):
        super().__init__(tipoEntrada, marca)
        self._idTeclado = Teclado.incrementarcontadorTeclados()

    def __str__(self):
        return f"[idTeclado: {self._idTeclado}, {super().__str__()}]"


if __name__ == "__main__":
    teclado1 = Teclado("Bluetooth","HP")
    print(teclado1)
    teclado2 = Teclado("wifi", "Lenovo")
    print(teclado2)