import psycopg2

conexion = psycopg2.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            query = 'UPDATE persona SET "Nombre"= %s, "Apellido"= %s, "Email" = %s WHERE id_persona = %s'
            valores = ("Lola", "Beltran", "LolaB@mail.com",1)
            cursor.execute(query,valores)
            registrosActualizados = cursor.rowcount
            print(f"Registros Actualizados: {registrosActualizados}")

finally:
    conexion.close()