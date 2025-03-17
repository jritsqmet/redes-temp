propietario= "Juan Paz"

marca=""
anio=""
color=""

def agregar(marca, anio, color):
    marca = input("Ingresar marca del auto: ")
    anio =  int( input("Ingresar año de fabricación: ")  )  
    color = input("Ingresar color de auto: ")

    imprimir(color, anio)


def imprimir( color, anio):
    print("El auto de color ", color, " se fabricó en ", anio)