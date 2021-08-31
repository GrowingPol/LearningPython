from os import remove
#from manejoDeArchivos import ManejoDeCatalogo
from Archivos.LaboratorioCatalogoPeliculas.catalogoPeliculas.servicio.manejoDeArchivos import ManejoDeCatalogo

class CatalogoPeliculas:

    def __init__(self,rutaArchivo):
        self.rutaArchivo = rutaArchivo

    def agregarPelicula(self,pelicula):
        with ManejoDeCatalogo(self.rutaArchivo,'a') as catalogo:
            catalogo.write("\n")
            catalogo.write(f"{pelicula.__str__()}")

    def listarPeliculas(self):
        with ManejoDeCatalogo(self.rutaArchivo,'r') as catalogo:
            for pelicula in catalogo:
                print(f"\n {pelicula.__str__()}")

    def eliminarCatalogo(self):
        remove(self.rutaArchivo)