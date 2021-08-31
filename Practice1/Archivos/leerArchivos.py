archivo = open("prueba.txt",'r',encoding="utf8")

'''--------------------Metodo 1--------------------'''
# for linea in archivo:
#     print(linea)

'''--------------------Metodo 2--------------------'''
#---------Leer lineas
# print(archivo.readlines()) #regresa una lista

#---------Leer una sola línea
# print(archivo.readlines()[1]) #regresa una lista, yse puede acceder linea por linea


'''--------------------Anexar texto a un archivo (leer y copiar)--------------------'''
archivo2 = open("copia.txt",'a',encoding='utf8') #a-append
archivo2.write(archivo.read())
archivo.close()
archivo2.close()