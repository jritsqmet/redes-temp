#Crear un programa que simule un sistema de login
#El programa debe pedir usuario y contraseña (admin/1234)
#Si las credenciales son correctas el programa pedirá ingresar
# un depósito al saldo base del usuario. 
#Posterior al deposito se debe mostrar el nuevo salario.
# El salario base es de $1530

import tkinter as tk

def login():
    usuario = entrada1.get()
    contrasenia = entrada2.get()

    if usuario== "admin" and contrasenia == "1234":
        print("Desplegar ventana")

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

boton = tk.Button(ventana, text="Calcular salario", command=login)
boton.pack()


ventana.mainloop()



