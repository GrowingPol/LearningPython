from Producto import Producto

class Orden:
    contadorOrdenes = 0

    def __init__(self, productos):
        self._idOrden = self._incrementarContadorOrdenes()
        self._productos = list(productos)

    def agregarProducto(self, producto):
        self._productos.append(producto)

    def calcularTotal(self):
        total = 0

        for producto in self._productos:
            total += producto.precio
        return total

    def __str__(self):
        productos_str = ''

        for producto in self._productos:
            productos_str  += producto.__str__() +' |'

        return f"Orden: {self._idOrden}, Productos: [{productos_str}]"

    @classmethod
    def _incrementarContadorOrdenes(cls):
        cls.contadorOrdenes += 1
        return cls.contadorOrdenes


if __name__ == "__main__":
    producto1 = Producto("camisa", 50)
    producto2 = Producto("pantalon", 800)
    producto3 = Producto("calzones",10)
    producto4 = Producto("Corbata",200.0)
    producto5 = Producto("Tennis",260.0)
    producto6 = Producto("Lentes", 300.0)
    productos1 = [producto1,producto2]
    productos2 = [producto3, producto4]

    orden1 = Orden(productos1)
    print(orden1)
    orden2 = Orden(productos2)
    print(orden2)
    orden1.agregarProducto(producto5)
    print(orden1)
    orden2.agregarProducto(producto6)
    print(orden2)
    print(orden1.calcularTotal())
    print(orden2.calcularTotal())