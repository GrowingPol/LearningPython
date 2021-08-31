import psycopg2 as bd
from loggerBase import log
import sys

class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _conexion = None
    _cusor = None

    @classmethod
    def obtenerConexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion = bd.connect(user= cls._USERNAME,
                                           password= cls._PASSWORD,
                                           host= cls._HOST,
                                           port= cls._DB_PORT,
                                           database= cls._DATABASE)

                log.debug(f"Conexion establecida: {cls._conexion}")
                return cls._conexion

            except Exception as e:
                log.debug(f"Ocurrió una excepción: {e}")
                sys.exit()

        else:
            return cls._conexion

    @classmethod
    def obtenerCursor(cls):
        if cls._cusor is None:
            try:
                cls._cusor = cls.obtenerConexion().cursor()
                log.debug(f"Se abrió el cursor: {cls._cusor}")
                return cls._cusor
            except Exception as e:
                log.debug(f"Exceptcion, No se pudo obtener Cursor: {e} ")
                sys.exit()
        else:
            return cls._cusor

    @classmethod
    def cerrar(cls):
        if cls._cusor != None:
            cls._cusor.close()
            cls._cusor = None
            log.debug(f"El cursor se ha cerrado: {cls._cusor}")
        else:
            log.debug(f"El cursor ya se encontraba cerrado: {cls._cusor}")

        if cls._conexion != None:
            cls._conexion.close()
            cls._conexion = None
            log.debug(f"La conexión se ha cerrado: {cls._conexion}")
        else:
            log.debug(f"No hay conexión existente: {cls._conexion}")

        return None







if __name__ == '__main__':
    Conexion.obtenerConexion()
    Conexion.obtenerCursor()
    Conexion.cerrar()
    Conexion.cerrar()
