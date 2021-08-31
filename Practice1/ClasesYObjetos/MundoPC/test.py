from Computadora import Computadora
from Monitor import Monitor
from Raton import Raton
from Teclado import Teclado
from Orden import Orden

raton1 = Raton("wifi","HP")
teclado1 = Teclado("usb","Lenovo")
monitor1 = Monitor("LG","45'")
raton2 = Raton("usb","Think")
teclado2 = Teclado("wifi","Think")
monitor2 = Monitor("LG","8'")
computadora1 = Computadora("HomeOffice",monitor1,teclado1,raton1)
computadora2 = Computadora("Gamer",monitor2,teclado2,raton2)
computadora3 = Computadora("Hibrida", monitor1,teclado2,raton1)

orden = Orden([computadora1,computadora2])

print(computadora1)
print(computadora2)
print("aaaaaaaaaaaaaa")
print(orden)
orden.agregarComputadora(computadora3)
print("Computadora agregada")
print(orden)