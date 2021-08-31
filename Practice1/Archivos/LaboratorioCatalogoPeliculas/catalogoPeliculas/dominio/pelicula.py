class Pelicula:

    def __init__(self,nombre):
        self._nombre = nombre

    def __str__(self):
        return f"{self._nombre}"

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def setNombre(self,nombre):
        self._nombre = nombre
