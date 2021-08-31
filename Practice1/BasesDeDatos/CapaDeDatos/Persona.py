from loggerBase import log

class Persona:

    def __init__(self,idPersona=None,nombre=None,apellido=None,email=None):
        self._idPersona = idPersona
        self._nombre = nombre
        self._apellido = apellido
        self._email = email

    def __str__(self):
        return f"ID: {self._idPersona}, Nombre: {self._nombre}, Apellido: {self._apellido}, Email: {self._email}"

    @property
    def idPersona(self):
        return self._idPersona

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    @property
    def email(self):
        return self._email

    @idPersona.setter
    def setIdPersona(self,idPersona):
        self._idPersona = idPersona

    @nombre.setter
    def setNombre(self,nombre):
        self._nombre = nombre

    @apellido.setter
    def setApellido(self,apellido):
        self._apellido = apellido

    @email.setter
    def setEmail(self,email):
        self._email = email


if __name__ == "__main__":
    persona1 = Persona(1,"Juan","Perez","jperez@gmail.com")
    log.debug(persona1)

    #simaular un insert sin escribir idPersona
    persona1 = Persona(nombre='Pablo', apellido='Escobar',email='Paes@mail.com')
    log.debug(persona1)

    #simular un DELETE
    persona1 = Persona(idPersona=1)
    log.debug(persona1)