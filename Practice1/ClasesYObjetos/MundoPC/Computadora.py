
class Computadora:
    contadorComputadoras = 0

    @classmethod
    def incrementarContadorCompu(cls):
        cls.contadorComputadoras += 1
        return cls.contadorComputadoras

    def __init__(self, nombre, monitor, teclado, raton):
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton
        self.idComputadora = Computadora.incrementarContadorCompu()

    def __str__(self):
        return f""" 
        
        {self._nombre}: {self.idComputadora},
        monitor: {self._monitor},
        teclado: {self._teclado},
        raton: {self._raton}"""

    @property
    def nombre(self):
        return self._nombre

    @property
    def monitor(self):
        return self._monitor

    @property
    def teclado(self):
        return self._teclado

    @property
    def raton(self):
        return self._raton

    @nombre.setter
    def setNombre(self,nombre):
        self._nombre = nombre

    @monitor.setter
    def setMonitor(self, monitor):
        self._monitor = monitor

    @nombre.setter
    def setTeclado(self, teclado):
        self._teclado = teclado

    @raton.setter
    def setRaton(self, raton):
        self._raton = raton

