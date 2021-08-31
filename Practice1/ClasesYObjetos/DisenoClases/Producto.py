

class Producto:
    contadorProductos = 0

    def __init__(self, nombre, precio):
        self._idProducto = Producto._incrementarIdProducto()
        self._nombre = nombre
        self._precio = precio

    def __str__(self):
        return f"ID Producto: {self._idProducto}, Nombre: {self._nombre}, Precio: {self._precio}"

    @classmethod
    def _incrementarIdProducto(cls):
        cls.contadorProductos += 1
        return cls.contadorProductos

    @property
    def idProducto(self):
        return self._idProducto

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return self._precio

    @nombre.setter
    def setNombre(self,nombre):
        self._nombre = nombre

    @precio.setter
    def setPrecio(self, precio):
        self._precio = precio




if __name__ == "__main__":
    producto1 = Producto("camisa", 100)
    print(producto1)
    producto1 = Producto("pantalón", 150.0)
    print(producto1)