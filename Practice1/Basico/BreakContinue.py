# Imprimir solo letras a

for letra in "Cacahuate":
    if letra == "a" :
        print("a")
        break
else:
    print("fin de ciclo for") # Cuando se usa break, se sale del ciclo for y se salta la condicion else


#Imprimir solo numeros pares

for i in range(6):
    if i%2 != 0:
        continue   # Se salta los ciclos donde la division de i entre dos tenga remanente (numero impares)
    print(i)
else:
    print("Ciclo for range terminado")


