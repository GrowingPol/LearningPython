
class ManejoDeCatalogo:

    def __init__(self,rutaDeArchivo,modo):
        self._archivo = rutaDeArchivo
        self._modo = modo

    def __enter__(self):
        print(f"Accediendo al recurso".center(50,'-'))
        self._archivo = open(self._archivo, self._modo, encoding='utf8')
        return self._archivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Recurso Cerrado".center(50,'-'))
        if self._archivo:
            self._archivo.close()