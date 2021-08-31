from Empleado import Empleado

class Gerente(Empleado):
    def __init__(self, nombre, sueldo, departamento):
        super().__init__(nombre,sueldo)
        self._departamento = departamento

    @property
    def departamento(self):
        return self._departamento

    def __str__(self):
        return f"Gerente [Departamento: {self._departamento}] {super().__str__()}"




