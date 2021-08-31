try:
    archivo = open("prueba.txt","w",encoding='utf8') #Abre archivo existente, o lo crea automaticamente/ utf8(Trabaja con acentos)
    archivo.write("Hola mundo! Buen día")
except Exception as e:
    print(e)
finally:
    archivo.write("\nAdios Mundo")
    archivo.close()
    print("archivo cerrado")