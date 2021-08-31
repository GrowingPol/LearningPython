print("Ingrese dos números y se determinará cuál de los dos es el mayor")
while True:
    try:
        number1 = float(input("Ingrese el primer número: "))
        number2 = float(input("Ingrese el segundo número: "))

        if number1 > number2:
            print(f"El número {number1} es mayor que el número {number2}")
        elif number2 > number1:
            print(f"El número {number2} es mayor que el número {number1}")
        elif number2 == number1:
            print(f"El número {number2} es igual que el número {number1}")
        break


    except ValueError:
        print("Ha introducido valores incorrectos")
