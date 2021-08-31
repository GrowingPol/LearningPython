from Empleado import Empleado
from Gerente import Gerente

#Polimorfismo sería cuando se tiene un método, y dependiendo el objeto que se tenga en parámetros
#se determina el método que se va a ejecutar

def imprimirDetalles(objeto):
    print(objeto)
    print(type(objeto))
    if isinstance(objeto,Gerente): # Validación de instancia de clase
        print(objeto.departamento)

empleado = Empleado("Juan",5000)
imprimirDetalles(empleado)

gerente = Gerente("Karla", 6000, "Sistemas")
imprimirDetalles(gerente)


