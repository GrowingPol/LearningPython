#Profundizando tipo float

a= 3.0
#constructor float puede recibir int y str
a= float(10)
print(f'a: {a:.1f}')
a= float('20')
print(f'a: {a:.3f}')

#Notacion exponencial (Valores positivos y negativo)
a= 3e5 #un 3 con 5 ceros a la derecha
print(f'a : {a}')
a= 3e-10 #un 3 en el décimo decimal
print(f'a : {a:.10f}')