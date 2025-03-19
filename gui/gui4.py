#Crear un programa que lea el la altura y el peso
# y determine el IMC

import tkinter as tk
from tkinter import messagebox 


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

################################
def calcularIMC2():
    peso = float ( entrada1.get() )
    altura = float( entrada2.get() )

    IMC = peso / (altura * altura)

    if IMC <18.5:
        mensaje = tk.Message(ventana, text="Peso insuficiente")
        mensaje.pack()
    elif IMC >= 25:
        mensaje = tk.Label(ventana, text="Tiene sobrepeso")
        mensaje.pack()
    else:
        tk.Label(ventana, text=("Peso normal")).pack()

############################################
def calcularIMC3():
    peso = float ( entrada1.get() )
    altura = float( entrada2.get() )

    IMC = peso / (altura * altura)

    if IMC <18.5:
        messagebox.showinfo("Peso insuficiente", f"El paciente tiene muy bajo peso con un IMC {IMC}")
    elif IMC >= 25:
       messagebox.showinfo("Sobrepeso", f"El paciente tiene sobrepeso con un IMC {IMC}")
    else:
       messagebox.showwarning("Peso normal", f"El pacien tiene un peso normal con IMC de: {IMC}")



######################################
#### INTEFAZ GRÁFICA #######

ventana = tk.Tk()
ventana.title("IMC")
ventana.geometry("400x180")

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
boton = tk.Button(ventana, text="Cálcular IMC", command=calcularIMC3)
boton.pack()

ventana.mainloop()