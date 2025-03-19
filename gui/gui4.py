#Crear un programa que lea el la altura y el peso
# y determine el IMC

import tkinter as tk
def calcularIMC():
    peso = float ( entrada1.get() )
    altura = float( entrada2.get() )

    IMC = peso / (altura * altura)

    if IMC <18.5:
        print("Peso insuficiente")
    elif IMC >= 25:
        print("Sobrepeso")
    else:
        print("Peso normal")

######################################
#### INTEFAZ GRÁFICA #######

ventana = tk.Tk()
ventana.title("IMC")
ventana.geometry("400x150")

####### PESO ########
etiqueta1 = tk.Label(ventana, text="Ingresar peso (kg)")
etiqueta1.pack()

entrada1 = tk.Entry(ventana)
entrada1.pack()

####### ALTURA #####
etiqueta2 = tk.Label(ventana, text="Ingresar altura (m)")
etiqueta2.pack()

entrada2 = tk.Entry(ventana)
entrada2.pack()

tk.Label(ventana, text=" ").pack() #Da un espacio en blanco en la interfaz
boton = tk.Button(ventana, text="Cálcular IMC", command=calcularIMC)
boton.pack()

ventana.mainloop()