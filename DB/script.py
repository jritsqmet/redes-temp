#CREAR DOCUMENTOS
arhivo = open("datos.xt", "w")

arhivo.write("Hola mundo \n")
arhivo.write("Esto es un mensaje \n")
arhivo.write("Otro mensaje\n")

texto1 = input("Ingresar un texto: ")
arhivo.write(texto1+ "\n")

texto2 = input("Ingresar segundo texto: ")
arhivo.write(texto2)

arhivo.close()

#LEER DOCUMENTOS
with open("datos.txt", "r") as datos:
    contenido = datos.read()

    print(contenido)