from loggerBase import log
from UsuarioDAO import UsuarioDAO
from Usuario import Usuario

print('''Bienvenido al Menu CRUD de la tabla de usuarios!
Aquí podrá realizar consultas y modificaciones a los registros de la tabla, 
ingrese un número para realizar una acción:''')
while True:
    task = int(input('''    1) Listar Usuarios
    2) Agregar Usuario
    3) Actualizar Usuario
    4) Eliminar Usuario
    5) Salir del programa
    --> '''))

    if task == 1:
        print("Usuarios registrados:")
        select = UsuarioDAO.seleccionar()
        log.info(f"User List readed")
        print(select)
    elif task == 2:
        try:
            print("Ingrese ID,usuario y contraseña del usuario a agregarse, separadas por un espacio entre cada una")
            values =input("-->").split(" ")
            usuario = Usuario(id_usuario=int(values[0]),username=values[1],password=values[2])
            UsuarioDAO.insertar(usuario)
            log.info(f"User create done: {usuario.__str__()}")
        except Exception as e:
            log.error(f'Exception in Insertar Usuario: {e}')
    elif task == 3:
        try:
            print("Ingrese ID,usuario y contraseña del usuario a actualizarse, separadas por un espacio entre cada una")
            values = input("-->").split(" ")
            usuario = Usuario(id_usuario=int(values[0]), username=values[1], password=values[2])
            UsuarioDAO.actualizar(usuario)
            log.info(f"User updated: {usuario.__str__()}")
        except Exception as e:
            log.error(f'Exception in Actualizar Usuario: {e}')
    elif task == 4:
        try:
            print("Ingrese ID del usuario a eliminarse")
            values = int(input("-->"))
            usuario = Usuario(id_usuario=values)
            UsuarioDAO.eliminar(usuario)
            log.info(f"User Deleted: {usuario}")
        except Exception as e:
            log.error(f'Exception in Eliminar Usuario: {e}')

    elif task == 5:
        log.info("Exiting Program")
        break
    else:
        print("Ingrese una acción valida por favor")

if __name__ == "__main__":
    pass