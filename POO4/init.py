#Crear un sistema de gestión de matriculas vehículares
#Va a tener como atributos: marca, placa, precio, año
#Crear la clase Auto y la clase Persona
#Persona tiene los atributos de CC, nombre
#Dependiendo del año del costo de la matrícula cambiará
#  >2020 => $800
#  entres 2010 y 2020  => $300
# menores del 2010 => $120

import Auto
import Persona

#creación de objetos
auto1 = Auto.Auto() # creación de objetos
auto2 = Auto.Auto()

#Métodos para ingresar autos
auto1.guardarAuto()
auto2.guardarAuto()

#Métodos para imprimir autos
auto1.imprimirAuto()
auto2.imprimirAuto()

#Calcular precio de matricula
auto1.calculoMatricula()
auto2.calculoMatricula()


persona1 = Persona.Persona()
persona1.ingresarPersona()
persona1.imprimirPersona()

print("El auto de placa: ", auto1.placa, " le pertenece a ", persona1.nombre)

