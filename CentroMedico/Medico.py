class Medico :

    #Declaración de atributos
    def __init__ (self):
        self.nombre=""
        self.especialidad=""

    def setMedico( self ):
        print("-----------")
        self.nombre = input("Ingresar nombre: ")
        self.especialidad = input("Ingresar especialidad: ")

    def imprimirMedico( self ):
        print("----------")
        print("MÉDICO: ", self.nombre)
        print("ESPECIALIDAD: ", self.especialidad)