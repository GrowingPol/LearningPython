import math
#profundizando en el tipo str

#---------------Concatenacion automatica en python

variable = 'Adios'
mensaje = 'Juan' 'Carlos' # Pueden concatenarse sin el signo +, pero solo si son strings, variables no
mensaje+= variable + 'Nos vemos'

#print(mensaje)

#---------------Help
#help(str.split)

#----------------docstring
from mi_clase import MiClase

#help(MiClase)
print(MiClase.__doc__)
print(MiClase.__init__.__doc__)
print(MiClase.mi_metodo.__doc__)
#print(MiClase.mi_metodo)


#-----------Las cadenas str son inmutables, si se modifican, en realidad ahora apuntan a una nueva direccion de memoria