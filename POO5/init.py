# numero1 = float( input("Ingresar primer número: "))
# numero2 = float( input ("Ingresar segundo número: ") )

# resultado = numero1 +numero2
# print("La respuesta es: " , resultado)

# try :
#     resultado = numero1 / numero2
#     print("La respuesta es: ", resultado)

# except ZeroDivisionError:
#     print("NO existe la división para cero")

####################################
# crear una aplicación que use la clase operaciones
# la clase operaciones va a devolver las operaciones básicas
# implementar un try (excepciones) para evitar errores

import Operaciones as op

operacion = op.Operaciones()

print("La suma es: ", operacion.suma(20, "ocho") )
print("La resta es: ", operacion.resta( 40, 8))
print("La multiplicación es: ", operacion.multiplicacion(6, 8))
print("La división es: ", operacion.division("tres",0))


print("#############################")
operacion.setNumeros()