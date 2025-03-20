# Formulario que pida al usuario, su nombre, la edad
# el género, estado civil, número de cédula, 
# AGREGAR UN CHECKBOX, CON LENGUAJES DE PROGRAMACIÓN
# En base a la información  se crearán 2 botones
# 1. (Ver información) Mostrar la informacacion ingresada
# 2. (Calculo de impuestos)
#  Calculo de impuestos:  si edad está entre 20 y 60 años impuesto de $200 anuales
#  si la edad es mayor de 60 impuesto de $100
#  si  es menor de 20 no paga impuestos
#  Además si en el esta civil consta como soltero se agrega un impuesto $30

import tkinter as tk
from tkinter import ttk, messagebox

def verInformacion():
    cedula = entrada1.get()
    nombre = entrada2.get()
    edad =  entrada3.get()
    genrer = genero.get()
    civil = entrada4.get()

    lenguajes = []

    if python.get()== True:
        lenguajes.append("Python")
    
    if cpp.get() == True:
        lenguajes.append("C++")

    if go.get() == True :
        lenguajes.append("Go")



    messagebox.showinfo("Datos Ingresados",
                       "Cédula: "+ cedula+ "\nNombre: " + nombre + "\nedad: "+ str(edad)   +"\nGénero: " + genrer+ "\nEstado Civil: " + civil
                        +f"\nLenguajes:  { str(lenguajes ) }"
                         )


def calcularImpuesto():
    nombre = entrada2.get()
    edad = int ( entrada3.get() )
    civil = entrada4.get()
    impuesto=0

    if edad>=20 and edad < 60:
        impuesto = 200
    elif edad >= 60:
        impuesto = 100

    if civil == "Soltera/o":
        impuesto = impuesto + 30

    messagebox.showinfo("Valor impuesto", f"{nombre} debe pagar ${impuesto} por impuestos" )




ventana = tk.Tk()
ventana.title("CALCULADORA IMPUESTOS")
tk.Label(ventana, text="FORMULARIO DE IMPUESTOS", font="Arial 20").grid(row=0, column=1)
#### CÉDULA###
tk.Label(ventana, text="N° Cédula: ").grid(row= 1, column=0)
entrada1 = tk.Entry(ventana)
entrada1.grid(row=1, column=1)


### NOMBRE ####
tk.Label(ventana, text="Nombre y Apellido: ").grid(row=2, column=0)
entrada2 = tk.Entry(ventana)
entrada2.grid(row=2, column=1)

### EDAD ###
tk.Label(ventana, text="Edad: ").grid(row=3, column=0)
entrada3 = tk.Entry(ventana)
entrada3.grid(row=3, column=1)

### GÉNERO ###
tk.Label(ventana, text="Género: ").grid(row=4, column=0)
genero = tk.StringVar()
rb_femenino  = tk.Radiobutton(ventana, text="Femenino", value="Femenino", variable= genero)
rb_masculino = tk.Radiobutton(ventana, text="Masculino", value="Masculino", variable= genero)

rb_femenino.grid( row =4 , column=1)
rb_masculino.grid( row =4 , column=2)

### ESTADO CIVIL ###
tk.Label(ventana, text="Estado Civil: ").grid(row=5, column=0)
estado= ["Soltera/o", "Casada/o", "Divorciada/o", "Viuda/o"]
entrada4 = ttk.Combobox(ventana, values= estado, state='readonly')
entrada4.grid(row=5, column=1)

### LENGUAJES DE PROGRAMACIÓN ####
python = tk.BooleanVar()
cpp = tk.BooleanVar()
go= tk.BooleanVar()

tk.Label(ventana, text="Seleccionar lenguajes: ").grid(row=6, column=0)
cb_python = tk.Checkbutton(ventana, text="Python", variable=python)
cb_python.grid(row=6, column=1)

cb_cpp = tk.Checkbutton(ventana, text="C++", variable=cpp)
cb_cpp.grid(row=7, column=1)

cb_go = tk.Checkbutton(ventana, text="Go", variable= go)
cb_go.grid(row=8, column=1)

tk.Button(ventana, text="Ver información", command=verInformacion).grid(row=9, column=0)
tk.Button(ventana, text="Calcula impuestos", command=calcularImpuesto).grid(row=9, column=2)


ventana.mainloop()