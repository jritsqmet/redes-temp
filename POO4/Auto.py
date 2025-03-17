class Auto:

    #definir los atributos
    def __init__(self):
        self.placa=""
        self.marca=""
        self.precio=0
        self.anio=0

    #crear un función para guardar datos
    def guardarAuto( self ):
        print("------------------")
        self.placa = input("Ingresar placa: ")
        self.marca = input("Ingresar marca: ")
        self.precio = float(  input("Ingresar precio: ")  ) 
        self.anio  = int( input ("Ingresar año: "))

    #crear un método para imprimir los datos de un auto
    def imprimirAuto (self):
        print("-------------------------------")
        print("PLACA: " , self.placa)
        print("MARCA: ", self.marca)
        print("PRECIO: ", self.precio)
        print("AÑO: ", self.anio)

    #Método que calcula el costo de la matrícula
    def calculoMatricula ( self ):
        if( self.anio >= 2020 ):
            print("El auto con placa ",self.placa ," debe pagar de matrícula es: 800" )
        
        elif ( self.anio >2010 and self.anio < 2020 ):
            print("El auto con placa ", self.placa ," debe pagar de matrícula es: 300")

        else:
            print("El auto con placa ", self.placa, " debe pagar de matrícula es: 120")
