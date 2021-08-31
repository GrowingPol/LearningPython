class Aritmetica:
    """Clase Aritmetica para sumar"""
    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2

    def sumar(self):
        return self.operando1 + self.operando2

    def restar(self):
        return self.operando1 - self.operando2

    def dividir(self):
        return self.operando1 / self.operando2

    def multiplicar(self):
        return self.operando1 * self.operando2


#Crear nuevo objeto
aritmetica = Aritmetica(10,3)
print(aritmetica.dividir())