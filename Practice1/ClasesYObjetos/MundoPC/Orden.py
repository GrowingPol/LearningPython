class Orden:
    contadorOrdenes = 0

    @classmethod
    def incrementarContadorOrdenes(cls):
        cls.contadorOrdenes += 1
        return cls.contadorOrdenes

    def __init__(self,computadoras):
        self._computadoras = list(computadoras)
        self._idOrden = Orden.incrementarContadorOrdenes()

    def agregarComputadora(self,computadora):
        self._computadoras.append(computadora)

    def __str__(self):
        computadoraStr = ''
        for computadora in self._computadoras:
            computadoraStr += computadora.__str__()

        return f"""
        Orden: {self._idOrden}, Computadoras:
        {computadoraStr}"""

    @property
    def computadoras(self):
        return self._computadoras

    @computadoras.setter
    def setComputadoras(self,computadoras):
        self._computadoras = computadoras

    @property
    def idOrden(self):
        return self._idOrden

    @idOrden.setter
    def setIdOrden(self,idOrden):
        self._idOrden = idOrden