print("Imagina a que tienes un hijo, éste te pregunta si puedes asistir a su partido.")
print("La respuesta a eso dependerá de dos factores")
loop = 1
while loop == 1:
    vacacionesString = input("¿Estás de Vaciones? Si/No? : ")
    descansoString = input("¿Es tu día de descanso? Si/No? : ")
    if (vacacionesString == "Si" or vacacionesString == "si" or vacacionesString == "No" or vacacionesString == "no") and (descansoString == "Si" or descansoString == "si" or descansoString == "No" or descansoString == "no"):
        loop = 0
    else:
        if not(vacacionesString == "Si" or vacacionesString == "si" or vacacionesString == "No" or vacacionesString == "no"):
            print(f"{vacacionesString} no es una respuesta válida")
        if not (descansoString == "Si" or descansoString == "si" or descansoString == "No" or descansoString == "no"):
            print(f"{descansoString} no es una respuesta válida")




vacacionesSi = vacacionesString == "Si" or vacacionesString == "si" or vacacionesString == "S" or vacacionesString == "s"
vacacionesNo = vacacionesString == "No" or vacacionesString == "no" or vacacionesString == "N" or vacacionesString == "n"
descansoSi = descansoString == "Si" or descansoString == "si" or descansoString == "S" or descansoString == "s"
descansoNo = descansoString == "No" or descansoString == "no" or descansoString == "N" or descansoString == "n"
if vacacionesSi or descansoSi:
    print("Qué bien! Verás a tu hijo jugar!")
elif vacacionesNo and descansoNo:
    print("Tendrá que ser otro día")
