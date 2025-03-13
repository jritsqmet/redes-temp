#Crear un programa que calcule el promedio de notas
# un estudiante. Si promedio >=7, aprueba
# si promedio está entre 5.45 y 6.99, supletorio
# si promedio es menor a 5.45, reprueba
# Crear una función que reciba un arreglo de notas

#[4,8,6,8]
def calcularPromedio( calificaciones ): 
    suma = 0
    for nota in calificaciones:
        suma = suma + nota
    
    promedio = suma / len( calificaciones )

    print("El promedio del alumno es: ", promedio)

    if promedio >= 7:
        print("Aprueba")
    
    elif promedio < 5.45:
        print("REPRUEBA")

    else:
        print("SUPLETORIOS")


calcularPromedio( [6, 9, 8, 4.5] )

nota=[4,8,9,6,7,6,7,1,5]
calcularPromedio( nota )