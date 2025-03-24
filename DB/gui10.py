import tkinter as tk
from tkinter import messagebox

datos=""

def guardar():

    nombre = entrada1.get()
    edad = entradaEdad.get()
    profesion = entradaProfesion.get()
   # archivo = open("datos.csv", 'w')
    ##PENDIENTE

   # datos= datos + archivo.read()


    with open ("datos.csv", 'a') as archivo:

        if  archivo.tell()== 0:
            archivo.write("Nombre,edad,profesión\n")

        archivo.write(f"{nombre},{edad},{profesion}\n")
        
        archivo.close()
    
    entrada1.delete(0, tk.END)
    entradaEdad.delete(0, tk.END)
    entradaProfesion.delete(0, tk.END)

    


def ventana1():
    #Se crea variables globales
    global entrada1, entradaEdad, entradaProfesion


    ventana = tk.Tk()
    ventana.title("Guardar datos")

    tk.Label(ventana, text="Ingresar Nombre").grid(row=0, column=0)
    entrada1 = tk.Entry(ventana)
    entrada1.grid(row=0, column=1)

    tk.Label(ventana, text="Ingresar edad").grid(row=1, column=0)
    entradaEdad = tk.Entry(ventana)
    entradaEdad.grid(row=1, column=1 )

    tk.Label(ventana, text="Ingresar profesion").grid(row=2)
    entradaProfesion = tk.Entry(ventana)
    entradaProfesion.grid(row= 2,column=1)

    tk.Button(ventana, text="GUARDAR", command=guardar, background='#7c75fa'). grid(row=3, column=1)


    ventana.mainloop()


ventana1()