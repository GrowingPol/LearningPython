from loggerBase import log
from Conexion import Conexion

class CursorDelPool:
    def __init__(self):
        self._conn = None
        self._cursor = None

    def __enter__(self):
        try:
            self._conn = Conexion.obtenerConexion()
            log.debug(f"Connection created: {self._conn}")
            self._cursor = self._conn.cursor()
            log.debug(f"Cursor created: {self._cursor}")
            return self._cursor
        except Exception as e:
            log.error(f"Exception in CursorDelPool __Enter__ : {e}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            log.error(f"Rollback done, Exception in context manager CursorDelPool : {exc_type}, {exc_val}")
            self._conn.rollback()
        else:
            try:
                self._conn.commit()
                self._cursor.close()
                Conexion.liberarConexion(self._conn)
                log.debug(f"Context Manager Exit, commit done, cursor closed, connection returned to pool")
            except Exception as e:
                log.error(f"Exception in CursorDelPool __Exit__ : {e}")
