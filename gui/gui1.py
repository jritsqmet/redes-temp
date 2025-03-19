import tkinter as tk
from tkinter import messagebox 

def saludo():
    nombre = entrada.get()
    print("Hola, bienvenido ", nombre)


def saludo2():
    mensaje = tk.Message( ventana, text="Hola mundo")
    mensaje.pack()




#DECLARIÓN INICIAL
ventana = tk.Tk()
ventana.title("Aplicación 1")
ventana.geometry("400x300")

#ETIQUETAS
etiqueta1 = tk.Label(ventana, text="Ingresar Texto", font=("Arial 20"))
etiqueta1.pack()

#INGRESAR TEXTO - INPUT
entrada = tk.Entry(ventana, font="Arial 15")
entrada.pack()

#CREAR BOTÓN 
boton = tk.Button(ventana, text="ACEPTAR", command = saludo2)
boton.pack()




ventana.mainloop()