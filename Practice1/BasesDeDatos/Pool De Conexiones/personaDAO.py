# DAO - Data Access Object
# DAO es un patrón de Diseño para comunicarse con una base de datos
#DAO tiene las operaciones CRUD (Create,Read,Update,Delete) de una clase de entidad(Persona)

from Persona import Persona
from loggerBase import log
from Cursor_Del_Pool import CursorDelPool
from Conexion import Conexion

class PersonaDAO:

    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona("Nombre","Apellido","Email") VALUES(%s,%s,%s)'
    _UPDATE = 'UPDATE persona SET "Nombre"=%s, "Apellido"=%s, "Email"=%s WHERE "id_persona"=%s'
    _DELETE = 'DELETE FROM persona WHERE "id_persona"=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas = []
            for registro in registros:
                persona = Persona(registro[0],registro[1],registro[2],registro[3])
                personas.append(persona)
            return personas

    @classmethod
    def insertar(cls,persona):
        with CursorDelPool() as cursor:
            values = (persona.nombre,persona.apellido,persona.email)
            log.debug(f"Persona a insertar: {persona}")
            cursor.execute(cls._INSERTAR,values)
            log.debug(f"Persona insertada: {persona}")
            return cursor.rowcount

    @classmethod
    def actualizar(cls,persona):
        with CursorDelPool() as cursor:
            values = (persona._nombre,persona._apellido,persona._email,persona._idPersona)
            log.debug(f"Persona a actualizar: {persona}")
            cursor.execute(cls._UPDATE,values)
            log.debug(f"persona actualizada: {persona}")
            return cursor.rowcount

    @classmethod
    def delete(cls,persona):
        with CursorDelPool() as cursor:
            values = (persona._idPersona,)
            log.debug(f"Persona a elminar : {persona}")
            cursor.execute(cls._DELETE,values)
            log.debug(f"Persona eliminada : {persona}")
            return cursor.rowcount


if __name__ == '__main__':

    # SELECT
    personas = PersonaDAO().seleccionar()
    for persona in personas:
        log.debug(f"{persona}")

    # INSERT
    persona1 = Persona(nombre="Alonzo",apellido="Ada",email="Ada@mail.com")
    personas_Insertadas = PersonaDAO().insertar(persona1)
    log.debug(f"Personas Insertadas: {personas_Insertadas}")

    #UPDATE
    persona1 = Persona(idPersona=3, nombre="Carlos",apellido="Sayonara",email="claraontas@mail.com")
    personas_Actualizadas = PersonaDAO().actualizar(persona1,)

    #DELETE
    persona1 = Persona(idPersona=8)
    personas_Borradas = PersonaDAO().delete(persona1)
    log.debug(f"Personas eliminadas: {personas_Borradas}")


    # SELECT
    personas = PersonaDAO().seleccionar()
    for persona in personas:
        log.debug(f"{persona}")

