#Bool contiene True y False

#Tipos numericos, False when n=0 and True when 0<n>0

valor = 30
resultado = bool(valor)
print(f"{resultado}")

#String type, False when string is empty, True if not

valor = "1"
resultado = bool(valor)
print(f"{resultado}")

#List type, False when list is empty, True if not

valor = [2]
resultado = bool(valor)
print(f"{resultado}")

#List type, False when list is empty, True if not

valor = ()
resultado = bool(valor)
print(f"{resultado}")

#dictionary type, False when list is empty, True if not

valor = {"1":'juan'}
resultado = bool(valor)
print(f"{resultado}")

#Can be used in control sentences (if '': something else: something else)