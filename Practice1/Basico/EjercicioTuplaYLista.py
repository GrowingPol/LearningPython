tupla = (13, 1, 8, 3, 2, 5, 8)
lista = []

for num in tupla:
    if num >= 5:
        continue
    elif num < 5:
        lista.append(num)

print(lista)


