a = 0
b = 5

number = float(input("introduzca un número para saber si está dentro del rango: "))
dentroRango = 0 <= number <= 5

if dentroRango:
    print(f"El numero {number} está dentro de rango")
else:
    print(f"El numero {number} está fuera de rango")