class ManejoArchivos: #Se puede utilizar para ptros recursos como bases de datos
    def __init__(self,nombre):
        self.nombre = nombre

    def __enter__(self):
        print("entrando al recurso".center(50,'-'))
        self.nombre = open(self.nombre,'r',encoding='utf8')
        return self.nombre

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Cerramos el recurso'.center(50,'-'))
        if self.nombre:
            self.nombre.close()