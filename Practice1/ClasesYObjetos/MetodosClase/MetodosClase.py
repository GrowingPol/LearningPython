# contexto Estático estodo lo que se refiere a la clase en sí misma
# Contexto Dinámico se refiere a la ultilización de instancias de una clase

class MiClase:
    variableClase = "VariableClase"

    def __init__(self):
        self.variableInstancia = "Variable de Instancia"

    @staticmethod
    def metodoEstatico(): # no se asigna self, porque self se asocia a los objetos, no hay parametros
        print("Metodo Estático") # method se asocia a la clase
        print(MiClase.variableClase)
       # print(MiClase.variableInstancia) Esta variable no se ha creado pues se crea al mismo tiemo  que un objeto
#Desde un metodo estático no se puede acceder a la variables de instancia
    @classmethod
    def metodoClase(cls): #Tampoco puede recibir parametro self, sino uno que haga referencia a la clase
        print("Método de Clase, " + str(cls))
        print(cls.variableClase)
        #No podemos acceder a una variable de instancia desde un contexto estático
        #print(cls.variableInstancia)

    def metodoInstancia(self):
        self.metodoEstatico()
        self.metodoClase()
        print(self.variableClase)
        print(self.variableInstancia)


print("Método Estático".center(50,'-'))
MiClase.metodoEstatico()
print("Método De Clase".center(50,'-'))
MiClase.metodoClase()
print("Método De Instancia".center(50,'-'))
instancia1 = MiClase()
instancia1.metodoInstancia()