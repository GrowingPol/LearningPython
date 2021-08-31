
class Monitor:
    contadorMonitores = 0

    @classmethod
    def incrementarcontadorMonitores(cls):
        cls.contadorMonitores += 1
        return cls.contadorMonitores

    def __init__(self, marca, tamano):
        self._marca = marca
        self._tamano = tamano
        self._idMonitor = Monitor.incrementarcontadorMonitores()

    def __str__(self):
        return f"[id: {self._idMonitor}, marca: {self._marca}, tamaño: {self._tamano}]"

    @property
    def idMonitor(self):
        return self._idMonitor

    @property
    def marca(self):
        return self._marca

    @property
    def tamano(self):
        return self._tamano

    @idMonitor.setter
    def setIdMonitor(self,idMonitor):
        self.idMonitor = idMonitor

    @marca.setter
    def setMarca(self,marca):
        self.marca = marca

    @tamano.setter
    def setTamano(self,tamano):
        self._tamano = tamano


if __name__ == "__main__":
    monitor1 = Monitor("HP","4 Pulgadas")
    print(monitor1)
    monitor2 = Monitor("Gamer", "20 Pulgadas")
    print(monitor2)