import psycopg2

conexion = psycopg2.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            query = 'DELETE FROM persona WHERE "id_persona" IN %s'
            entrada = input("Ingrese los ID de las columnas a eliminarse, separadospor coma: ")
            valores = (tuple(entrada.split(',')),)
            cursor.execute(query,valores)
            registrosEliminados = cursor.rowcount
            print(f"Registros Eliminados: {registrosEliminados}")

finally:
    conexion.close()