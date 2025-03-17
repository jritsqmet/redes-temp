
def imprimir( nombre, especie, peso ):
    print( nombre, " tiene un peso de: ", peso)

def calcularPeso( peso, especie ):
    #### PERRO
    # Si peso mayor 20kg sobrepeso
    # si tiene entre 12kg y 20kg peso ideal
    # si tiene menos 12kg peso insuficiente

    #### GATO
    # Si peso mayor 12kg sobrepeso
    # si tiene entre 7kg y 12kg peso ideal
    # si tiene menos 7kg peso insuficiente

    if especie == 'perro':
        if peso > 20:
            print("Tiene sobrepeso")
        elif peso <12:
            print("Tiene un peso insuficiente")
        else :
            print("Tiene peso ideal")
    
    if especie == 'gato':
        if peso > 12:
            print("Tiene sobrepeso")
        elif peso < 7:
            print("Tiene un peso insuficiente")
        else:
            print("Tiene un peso ideal")

