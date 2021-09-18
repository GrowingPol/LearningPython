from loggerBase import log
from Usuario import Usuario
from CursorDelPool import CursorDelPool

class UsuarioDAO:

    _SELECCIONAR = f"SELECT * FROM usuario"
    _INSERTAR = f'INSERT INTO usuario(id_usuario,username,password) VALUES(%s,%s,%s)'
    _ACTUALIZAR = 'UPDATE usuario SET "username"=%s, "password"=%s WHERE "id_usuario" = %s'
    _ELIMINAR = 'DELETE FROM usuario WHERE "id_usuario" = %s'

    @classmethod
    def seleccionar(cls):
        log.debug("showing users")
        usuarios = ""
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            data = cursor.fetchall()
        for user in data:
            usuario = Usuario(user[0],user[1],user[2])
            usuarios = usuarios + (usuario.__str__() +"\n")
        return usuarios

    @classmethod
    def insertar(cls,usuario):
        with CursorDelPool() as cursor:
            values = (usuario.id_usuario,usuario.username,usuario.password)
            cursor.execute(cls._INSERTAR,values)
        return cursor.rowcount

    @classmethod
    def actualizar(cls,usuario):
        with CursorDelPool() as cursor:
            values = (usuario.username,usuario.password,usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR,values)
        return cursor.rowcount

    @classmethod
    def eliminar(cls,usuario):
        with CursorDelPool() as cursor:
            values = (usuario.id_usuario,)
            cursor.execute(cls._ELIMINAR,values)
        return cursor.rowcount


if __name__ == "__main__":
    usuario1 = Usuario(id_usuario=2,username='almino',password='polimina2')
    UsuarioDAO.insertar(usuario1)