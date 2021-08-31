class Caja:
    def __init__(self, alto, largo, ancho):
        self.alto = alto
        self.largo = largo
        self.ancho = ancho

    def volumen(self):
        return self.alto * self.largo * self.ancho


while True:
    try:
        height = float(input("Ingrese el alto de la caja: "))
        width = float(input("Ingrese el ancho de la caja: "))
        large = float(input("Ingrese el largo de la caja: "))
        break

    except ValueError:
        print("Ingrese un valor válido por favor")



caja1 = Caja(height,large,width)
print(f"El volumen de la caja es : {caja1.volumen()}")