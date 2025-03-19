#Crear una interfaz gráfica que reciba dos números
#La aplicación realizará las operaciones básicas
#Determinar cual de los número es mayor  o si son iguales

import tkinter as tk

def mayor():
    numero1 = int( entrada1.get() )
    numero2 = int( entrada2.get() )

    if( numero1 > numero2 ):
        print("El primer número es mayor")
    elif( numero2 > numero1 ):
        print("El segundo número es mayor")
    else:
        print("Los números son iguales")

#########################################################
################# INTERFAZ GRÁFICA ######################
#DECLARACIÓN INICIAL
ventana = tk.Tk()
ventana.title("Múltiplos de 3")
ventana.geometry("400x200")

tk.Label(ventana, text="Ingresar primer número").pack()
entrada1 = tk.Entry(ventana)
entrada1.pack()

tk.Label(ventana, text="Ingresar segundo número").pack()
entrada2 = tk.Entry(ventana)
entrada2.pack()

tk.Button(ventana, text="Cual es mayor", command=mayor).pack()

ventana.mainloop()