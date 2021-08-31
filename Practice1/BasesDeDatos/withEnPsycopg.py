import psycopg2

conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_db'
)

'''------------------------------------uso de with y placeholders'''
# el cursor se cierra automaticamente al terminar el with
#conexion no se cierra al terminar al with, debe usarse un bloque try finally para asegurarse
try:
    with conexion:
        with conexion.cursor() as cursor:
            query= "Select * from persona where id_persona = %s" # %s es un place holder, se le asigna valor después
            idPersona = 1
            cursor.execute(query,(idPersona,)) #Para dar valor a los placeholders, se debe señalar una tupla, por eso la coma
            registros = cursor.fetchone()
            print(registros)
except Exception as e:
    print(e)
finally:
    conexion.close()


'''------------------------------------uso de fetchall y for'''
print("Otra conexión".center(50,'-'))
conexion = psycopg2.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            #query= "Select * from persona where id_persona IN (1,2)"
            query = "Select * from persona where id_persona IN %s"
            entrada = input("Ingrese los ID a buscar, separe por comas")
            llavesPrimarias = tuple((entrada.split(',')))
            print(llavesPrimarias)
            cursor.execute(query,(llavesPrimarias,))
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)

except Exception as e:
    print(e)
finally:
    conexion.close()