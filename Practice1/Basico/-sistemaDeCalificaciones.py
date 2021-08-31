
while True:
    try:
        calificacion = float(input("Introduzca la calificación decimal que obtuvo el estudiante: "))
        if(0 <= calificacion <= 10):
            break
        else:
            print("Valor Fuera De Rango")


    except ValueError:
        print("Valor no Válido")
nota = "Null"
if calificacion >= 0 and calificacion < 6 :
    nota = "F"
elif calificacion >= 6 and calificacion < 7 :
    nota = "D"
elif (7 <= calificacion < 8):
    nota = "C"
elif (8 <= calificacion < 9):
    nota = "B"
elif (9 <= calificacion <= 10):
    nota = "A"

print(f"La calificación del alumno de {calificacion} vale por una {nota}")