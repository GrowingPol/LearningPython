import psycopg2

conexion = psycopg2.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            query = 'INSERT INTO persona("Nombre", "Apellido", "Email") VALUES(%s, %s, %s)'
            valores = ("Sofia", "Bergara", "sofi@mail.com")
            cursor.execute(query, valores)
            registrosInsertados = cursor.rowcount
            print(f"Registros Insertados: {registrosInsertados}")

            query = 'UPDATE persona SET "Nombre"= %s, "Apellido"= %s, "Email" = %s WHERE id_persona = %s'
            valores = ("Lola", "Beltran", "LolaB@mail.com", 1)
            cursor.execute(query, valores)
            registrosActualizados = cursor.rowcount
            print(f"Registros Actualizados: {registrosActualizados}")

            conexion.commit()
            print("Termina la Transacción, se hizo commit")
except Exception as e:
    conexion.rollback()
    print(f"Ocurrió un error, se hizo rollback: {e}")
finally:
    conexion.close()


#La transacción consiste en la modificación de datos en la base de datos, commit guarda los cambios y rollback no los aplica
#Se considera una transacción a INSERT,DELETE y UPDATE. SELECT puede incluirse en una transacción, pero no es necesario confirmala pues no hace modificaciones