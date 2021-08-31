class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return (self.base + self.altura) * 2


print("PRograma para calcular área y perímetro de un rectángulo")
while True:
    try:

        base1 = float(input("Ingrese la base del rectángulo en metros: "))
        altura1 = float(input("Ingrese la altura del rectángulo en metros: "))
        break

    except ValueError:
        print("Ingrese un dato válido por favor")


rectangulo = Rectangulo(base1,altura1)
print(f"El área del rectángulo es : {rectangulo.area()} mts^2")
print(f"El perímetro del rectángulo es : {rectangulo.perimetro()} mts")


