#Crear un programa que reciba dos clases ( Medico, Paciente)
#Clase medico tendrá los atributos : "Nombre", "Especialidad",
#Clase Paciente tendra los atributos: 
# "CC", "Nombre", "Edad" y "Peso"
#El programa va a mencionar si una persona IMC>25 => sobrepeso
# IMC está entre 18.5 y 24.9  => Peso apropiado
# IMC está bajo 18.5 => Peso insuficiente

# Calcular indice de creciemiento de un niño y mostrar los datos
# IC= edad / altura 
# IC > 1 => normal
# IC entre 1 y 0.85 =>bajo crecimiento
# IC <0.85 => Muy bajo crecimiento

#notas = [ 2, 8, 71, 6,8,2,]

import Paciente

pacientes = []
cantidad = 0


while cantidad < 3:
    ##SE CREA EL OBJETO PACIENTE
    paciente = Paciente.Paciente() 
    paciente.setPaciente()

    #Agregar información al arreglo
    pacientes.append(paciente)

    cantidad = cantidad + 1
    

#Trae todos los elementos del arreglo
for item in pacientes:
    item.imprimirPaciente() 

for item in pacientes:
    item.calculoIMC()

#############################
try:
    print(10/1)

except ZeroDivisionError :
    print("No existe la división para cero")