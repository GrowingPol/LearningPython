import psycopg2 as bd

conexion = bd.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            query = 'INSERT INTO persona("Nombre", "Apellido", "Email") VALUES(%s, %s, %s)'
            valores = ("Nicola", "Tesla", "tesla@mail.com")
            cursor.execute(query, valores)
            registrosInsertados = cursor.rowcount
            print(f"Registros Insertados: {registrosInsertados}")

            query = 'UPDATE persona SET "Nombre"= %s, "Apellido"= %s, "Email" = %s WHERE id_persona = %s'
            valores = ("Pancho", "Lopez", "Plopez@mail.com", 1)
            cursor.execute(query, valores)
            registrosActualizados = cursor.rowcount
            print(f"Registros Actualizados: {registrosActualizados}")

except Exception as e:
    print(f"Ocurrió un error, se hizo rollback: {e}") #El administrador de recursos, hace rollback por nosotros
else:
    print("Termina la transacción, se hizo commit") # El administrador de recursos with, hace el commit por nosotros
finally:
    conexion.close()

