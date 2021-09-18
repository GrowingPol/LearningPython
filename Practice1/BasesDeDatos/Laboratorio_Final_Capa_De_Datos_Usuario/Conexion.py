import sys
from psycopg2 import pool
from loggerBase import log

class Conexion:
    _DATABASE = 'test_db'
    _HOST = '127.0.0.1'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _MIN_CONN = 1
    _MAX_CONN = 5
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool == None:
            try:
                cls._pool = pool.SimpleConnectionPool(minconn=cls._MIN_CONN,
                                                      maxconn=cls._MAX_CONN,
                                                      database=cls._DATABASE,
                                                      host=cls._HOST,
                                                      port=cls._DB_PORT,
                                                      user=cls._USERNAME,
                                                      password=cls._PASSWORD)
                log.debug(f"Pool Succesfully Created : {cls._pool}")
                return cls._pool

            except Exception as e:
                log.error(f"Exception in obtenerConexion, couldn't create pool: {e}")
                sys.exit()

        else:
            log.debug(f"Pool stare")
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        try:
            _conexion = cls.obtenerPool().getconn()
            log.debug(f"New connection created: {_conexion}")
            return _conexion
        except Exception as e:
            log.error(f"Connection exception: {e}")

    @classmethod
    def liberarConexion(cls,conexion):
        try:
            cls.obtenerPool().putconn(conexion)
            log.debug(f"Connection {conexion} get back to the pool")
        except Exception as e:
            log.error(f"Connection liberation failed, Exception: {e}")

    @classmethod
    def cerrarConexiones(cls):
        try:
            cls.obtenerPool().closeall()
            log.debug("All connections in pool has been closed")
        except Exception as e:
            log.error(f"Exception in CerrarConexiones: {e}")


if __name__ == "__main__":
    pass