from Archivos.LaboratorioCatalogoPeliculas.catalogoPeliculas.dominio.pelicula import Pelicula
from Archivos.LaboratorioCatalogoPeliculas.catalogoPeliculas.servicio.catalogoPeliculas import CatalogoPeliculas
print("Catálogo de películas")
print("El siguiente catálogo puede contener hasta cuatro películas y puede editarlo como guste.")
catalogo1 = CatalogoPeliculas("peliculas.txt")
pelicula = Pelicula('')

while True:
    print("""Ingrese el número de la acción que desea realizar:
    1.- Agregar Película
    2.- Mostrar Listado
    3.- Eliminar Catálogo
    4.- Salir de la Aplicación    
    """)
    try:
        accion = int(input())
    except Exception as e:
        print(f"\n {e},\nIngrese una opción válida")

    if accion == 1:
        try:
            nombrePelicula = str(input(f"\nIngrese el nombre de una película: "))
            pelicula.setNombre = nombrePelicula
            catalogo1.agregarPelicula(pelicula)
            print(f"La pelicula {nombrePelicula} ha sido agregada")
        except Exception as e:
            print(f"\n {e},\nIngrese la palícula de manera correcta")

    elif accion == 2:
        print("Películas en Catálogo:")
        try:
            catalogo1.listarPeliculas()
        except Exception as e:
            print(f"No se pudo acceder al catálogo, error: {e}")

    elif accion == 3:

        try:
            catalogo1.eliminarCatalogo()
        except Exception as e:
            print(f"No se pudo acceder al catálogo, error: {e}")

        print("Catálogo Eliminado")

    elif accion == 4:
        print("Saliendo del programa")
        break

    else:
        print("El npumero de acción no es válido")