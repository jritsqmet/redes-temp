class Persona:

    #declarar atributos
    def __init__(self):
        self.cedula = ""
        self.nombre = ""

    #crear el método para ingresar información de persona
    def ingresarPersona ( self ):
        self.cedula = input ("Ingresar cédula: ")
        self.nombre = input ("Ingresar nombre: ")

    def imprimirPersona ( self ):
        print("----------------")
        print("CI: ", self.cedula)
        print("NOMBRE: ", self.nombre)