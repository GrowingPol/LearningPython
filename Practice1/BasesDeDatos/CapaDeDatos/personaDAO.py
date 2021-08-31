# DAO - Data Access Object
# DAO es un patrón de Diseño para comunicarse con una base de datos
#DAO tiene las operaciones CRUD (Create,Read,Update,Delete) de una clase de entidad(Persona)
from Conexion import Conexion
from Persona import Persona
from loggerBase import log

class PersonaDAO:

    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona("Nombre","Apellido","Email") VALUES(%s,%s,%s)'
    _UPDATE = 'UPDATE persona SET "Nombre"=%s, "Apellido"=%s, "Email"=%s WHERE "id_persona"=%s'
    _DELETE = 'DELETE FROM persona WHERE "id_persona"=%s'

    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerCursor() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas = []
            for registro in registros:
                persona = Persona(registro[0],registro[1],registro[2],registro[3])
                personas.append(persona)

        Conexion.cerrar()
        return personas

    @classmethod
    def insertar(cls,persona):
        with Conexion.obtenerCursor() as cursor:
            values = (persona.nombre,persona.apellido,persona.email)
            log.debug(f"Persona a insertar: {persona}")
            cursor.execute(cls._INSERTAR,values)
            log.debug(f"Persona insertada: {persona}")
            return cursor.rowcount

        Conexion.cerrar()

if __name__ == '__main__':
    #SELECT
    personas = PersonaDAO().seleccionar()
    for persona in personas:
        log.debug(f"{persona}")

    # INSERT
    persona1 = Persona("Pancho","Barraza","paba1@mail.com")