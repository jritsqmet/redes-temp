#creación de un función
def saludo ():
    print("Hola mundo")
    print("Esto es un texto de prueba")
    print("Se está llamando una función")
    print("----------------------------")

#llamar a la función
saludo()

#creación de una función que recibe un parámetro
def saludo2 ( nombre ):
    print("Hola tu nombre es: ", nombre)

saludo2( "Juan Paz")
saludo2( "Ana Guerra")

########################
print("####################################")
#Creación de función
def calculadora (numero1, numero2):
    print("------------------------------")
    respuesta = numero1 + numero2
    print("La suma es: ", respuesta)

    respuesta = numero1- numero2
    print("La resta es: ", respuesta)

    respuesta = numero1 * numero2
    print("La multiplicación es: ", respuesta)

    respuesta = numero1/numero2
    print("La división es: ", respuesta)

#llamar a la función
calculadora(7,9)
calculadora(8,6)

#USO DE return
#crear una función
print("#########################")
print("#########################")
def promedio (nota1, nota2, nota3):
    resultado = (nota1 + nota2 + nota3)/3

    return resultado

#llamar función


print("El promedio es: ", promedio( 6, 9, 7) )