class Empleado:
    def __init__(self,nombre,sueldo):
        self._nombre = nombre
        self._sueldo = sueldo

    @property
    def nombre(self):
        return self._nombre

    @property
    def sueldo(self):
        return self._sueldo

    def __str__(self):
        return f"Empleado: [Nombre: {self._nombre}, sueldo: {self._sueldo}]"