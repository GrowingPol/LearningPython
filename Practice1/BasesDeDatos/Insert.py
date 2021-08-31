import psycopg2

conexion = psycopg2.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            query = 'INSERT INTO persona("Nombre", "Apellido", "Email") VALUES(%s, %s, %s)'
            valores = ("Carlos", "Lara", "clara@mail.com")
            cursor.execute(query,valores)
            registrosInsertados = cursor.rowcount #Nos dice el numero de filas afectadas
            print(f"Registros Insertados: {registrosInsertados}")
            #conexion.commit() # No es necesario un commit(salvar cambios) cuando se usa with pues se hace automático
finally:
    conexion.close()