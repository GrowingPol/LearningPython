print("Introduzca los datos del libro que le gustarpia rentar")
freeDelivery = "N/A"
while True:
    try:
        book = input("Título del Libro: ")
        id = int(input("Id del Libro: "))
        price = float(input("Precio del Libro: "))
        freeDeliveryStr = input("Tiene Envío Gratis? : ")
        if freeDeliveryStr == "si" or freeDeliveryStr == "Si":
            freeDelivery = "Si"
        elif freeDeliveryStr == "No" or freeDeliveryStr == "no":
            freeDelivery = "No"
        break
    except ValueError:
        print("Los valores ingresados son incorrectos")

#Imprimir varias líneas en un print
print(f'''
    Libro: {book}
    Id: {id}
    Precio: ${price}
    Envío Gratis: {freeDelivery}''')