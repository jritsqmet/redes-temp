class Paciente:
    
    def __init__(self):
        self.cedula=""
        self.nombre=""
        self.edad=0
        self.peso=0
        self.altura=0

    def setPaciente (self):
        print("------------")
        self.cedula = input("Ingresar cedula: ")
        self.nombre = input("Ingresar nombre: ")
        self.edad = int( input("Ingresar edad: "))
        self.peso = float (input("Ingresar peso: "))
        self.altura = float ( input ("Ingresar altura: "))

    def imprimirPaciente( self ):
        print("-----------------")
        print("CÉDULA: ", self.cedula)
        print("PACIENTE: ", self.nombre)
        print("EDAD: ", self.edad)
        print("PESO: ", self.peso)
        print("ALTURA: ", self.altura)


    def calculoIMC( self ):
        IMC = self.peso/( self.altura * self. altura)

        print("---------------------")

        if IMC >=25:
            print("El paciente ", self.nombre , " tiene sobrepeso")
        if IMC <18.5 :
            print("El paciente ", self.nombre, " tiene un peso insuficiente")
        else:
            print("El panciente ", self.nombre, " tiene un peso adecuado")