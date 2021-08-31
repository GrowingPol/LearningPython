from manejoArchivos import ManejoArchivos

#Manejo de contexto with
#Context Manager
#Al finalizar, se cerrará automátiamente el archivo


with ManejoArchivos("pruebilla.txt") as archivo:
    print(archivo.read())