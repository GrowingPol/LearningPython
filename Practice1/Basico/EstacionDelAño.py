print("Desea saber a qué estación corresponde un mes del año?")

while True:
    try:
        mes = int(input("Introduzca un mes del año, en formato numérico (1-12): "))
        estacion = None

        if mes == 1 or mes == 2 or mes == 12:
            estacion = "Invierno"
        elif mes == 3 or mes == 4 or mes == 5:
            estacion = "Primavera"
        elif mes == 6 or mes == 7 or mes == 8:
            estacion = "Verano"
        elif mes == 9 or mes == 10 or mes == 11:
            estacion = "Otoño"

        if 12 >= mes >= 1:
            break
        else:
            print("Valor Proporcionado Fuera de Rango")

    except ValueError:
        print("Valor Proporcionado no válido")

mesStr = "N/A"
if mes == 1:
    mesStr = "Enero"
elif mes == 2:
    mesStr = "Febrero"
elif mes == 3:
    mesStr = "Marzo"
elif mes == 4:
    mesStr = "Abril"
elif mes == 5:
    mesStr = "Mayo"
elif mes == 6:
    mesStr = "Junio"
elif mes == 7:
    mesStr = "Julio"
elif mes == 8:
    mesStr = "Agosto"
elif mes == 9:
    mesStr = "Septiembre"
elif mes == 10:
    mesStr = "Octubre"
elif mes == 11:
    mesStr = "Noviembre"
elif mes == 12:
    mesStr = "Diciembre"


print(f"El Mes {mesStr} corresponde a la estación {estacion}")

while True:
        satisfecho = input("Quedaste Satisfecho? si/no :")
        if satisfecho == "si":
            satisfechoBool = 1
        elif satisfecho == "no":
            satisfechoBool = 0
        else:
            print("Respuesta no válida")

        if satisfecho == "si" or satisfecho == "no" :
            break

print("Nos alegra escuchar eso :)") if satisfechoBool else print("Trabajaremos duro para impresionarte!")





