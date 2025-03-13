#Crear un programa que determine si un estudiante aprobó (>=7)
#Implementar una función que reciba el nombre del estudiante
# y el promedio del estudiante.

#Creación de la función
def calculoNotas (nombre, promedio):
    if promedio >= 7:
        print(nombre, " aprobó la materia con: ", promedio)
    else:
        print(nombre, "no aprobó")

def calculoBeca( beca ):
    if beca == True:
        print("Tiene beca")
    else:
        print("No tiene beca")


nombre="*"
while nombre != "":
    print("----------------------------------")
    nombre = input("Ingresar nombre: ")
    if nombre != "":
        promedio = float( input("ingresar promedio: ") )
        beca = bool( input ("Tiene beca (True/False): ") )

        calculoNotas( nombre, promedio )
        calculoBeca(beca)
