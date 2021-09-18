#Profundizando en sistemas de numeracion
#How to declare values
#First two leters define whic numeration system it is about

#decimal
a = 10

#Binary
a = 0b1010

#Octal
a= 0o12

#Hexadecimal
a= 0xA


#Convertir a un tipo entero, incluyendo base
a = int('23', 10) #la base por default es 10
print(a)
#Base binaria
a = int('10111',2)
print(a)
#Base Octal
a = int('27',8)
print(a)
#Base hexadecimal
a = int('17',16)
print(a)