from loggerBase import log
from Conexion import Conexion

class CursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug(f" Inicio de __enter__")
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb): # type,value and traceback(details) of exception
        log.debug(f" __exit__ executed")
        if exc_val:
            self._conexion.rollback()
            log.error(f"Exception ocurred: {exc_type}, {exc_val}")
        else:
            self._conexion.commit()
            log.error(f"Commit done")
            self._cursor.close()
        Conexion.liberarConexion(self._conexion)
        log.debug(f"Conexion liberada: {self._conexion}")



if __name__ == "__main__":

    with CursorDelPool() as cursor:
        log.debug(f"Dentro de with")
        cursor.execute(f"SELECT * FROM persona")
        log.debug(f"{cursor.fetchall()}")
