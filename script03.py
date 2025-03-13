# Crear un programa que va recibir una lista de productos
# Determinar si se aplica IVA o no
# Los productos lacteos no tiene IVA
# La lista tendrá el nombre, tipo, y el precio sin IVA
# Mostrar el precio final de cada producto

productos = [ {
        "nombre": "Leche",
        "tipo": "Lácteo",
        "precio": 0.89
    } ,
    {
        "nombre": "Arroz",
        "tipo": "Cereal",
        "precio": 2.5
    } ,
    {
        "nombre": "Queso",
        "tipo": "Lácteo",
        "precio": 4.50
    }
]


productos2 = [ {
        "nombre": "Champú",
        "tipo": "Aseo",
        "precio": 2.6
    } ,
    {
        "nombre": "Manzanas",
        "tipo": "fruta",
        "precio": 1.5
    } ,
    {
        "nombre": "Mantequilla",
        "tipo": "Lácteo",
        "precio": 3.50
    },
    {
        "nombre": "Azúcar",
        "tipo": "básico",
        "precio": 4.5
    }
]

def calculoIVA ( productos ):
    for producto in productos:
        #print(producto['nombre'])
        if producto['tipo'] == "Lácteo":
            print("El precio de: ", 
                  producto['nombre'], "es: ",  producto['precio'])
        else:
            precioFinal = producto['precio'] * 1.15
            print("El precio de: ", 
                  producto['nombre'], "es", precioFinal   )

#####
#Llamar a la función

calculoIVA( productos)
calculoIVA( productos2 )