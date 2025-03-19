#Crear un programa que simule un sistema de login
#El programa debe pedir usuario y contraseña (admin/1234)
#Si las credenciales son correctas el programa pedirá ingresar
# un depósito al saldo base del usuario. 
#Posterior al deposito se debe mostrar el nuevo salario.
# El salario base es de $1530

import tkinter as tk
from tkinter import messagebox

def login():
    usuario = entrada1.get()
    contrasenia = entrada2.get()

    ventana2 = tk.Tk()
    ventana2.geometry("200x150")

    def deposito():
        monto = float ( entrada.get() )
        salarioFinal = monto+ 1530

        messagebox.showinfo("Salario", f"Salario total es: {salarioFinal}")
        

    if usuario== "admin" and contrasenia == "1234":
        tk.Label(ventana2, text="Ingresar depósito").pack()
        entrada = tk.Entry(ventana2)
        entrada.pack()

        

        boton = tk.Button(ventana2, text="Depositar", command=deposito )
        boton.pack()

        ventana2.mainloop()





ventana = tk.Tk()
ventana.title("CÁLCULO SALARIO")
ventana.geometry("400x150")


etiqueta1 = tk.Label(ventana, text="Ingresar usuario")
etiqueta1.pack()

entrada1 = tk.Entry(ventana)
entrada1.pack()

etiqueta2 = tk.Label(ventana, text="Ingresar contraseña")
etiqueta2.pack()

entrada2 = tk.Entry(ventana)
entrada2.pack()

boton = tk.Button(ventana, text="Login", command=login)
boton.pack()


ventana.mainloop()



