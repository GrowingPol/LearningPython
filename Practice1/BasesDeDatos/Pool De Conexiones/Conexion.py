from psycopg2 import pool
from loggerBase import log
import sys
# Connection pool manages an specific number of conexion "slots",
# Every time a client ask for a conexion, pool lease one of its slots until max is reached,
# for deoccupate slots, client must let pool know it

class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CONN = 1 #Min number of connections oppened
    _MAX_CONN = 5 #Max number of connections oppened
    _pool = None


    @classmethod
    def obtenerPool(cls):
        if cls._pool == None:
            try:
                cls._pool = pool.SimpleConnectionPool(minconn=cls._MIN_CONN,
                                                      maxconn=cls._MAX_CONN,
                                                      database=cls._DATABASE,
                                                      user=cls._USERNAME,
                                                      password=cls._PASSWORD,
                                                      host=cls._HOST,
                                                      port=cls._DB_PORT)
                log.debug(f"Creacion de pool exitosa: {cls._pool}")
                return cls._pool

            except Exception as e:
                log.error(f"Error al conectar el pool: {e}")
                sys.exit()

        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        log.debug(f"Conexion obtenida del pool: {conexion}")
        return conexion

    @classmethod
    def liberarConexion(cls,conexion):
        cls.obtenerPool().putconn(conexion) # Toma el pool actual, y regresa el objeto coneion al pool.
        log.debug(f"Regresó la conexión al pool: {conexion}")

    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()
        log.debug(f"Se cerraron todas las conexiones")



if __name__ == '__main__':
    conexion1 = Conexion.obtenerConexion()
    conexion2 = Conexion.obtenerConexion()
    conexion3 = Conexion.obtenerConexion()
    conexion4 = Conexion.obtenerConexion()
    conexion5 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion5)
    conexion6 =Conexion.obtenerConexion()

