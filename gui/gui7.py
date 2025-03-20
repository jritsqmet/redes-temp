#Crear un programa que simule una reserva de un hotel
# el programa debe recibir el numéro de días y el tipo de habitación
# habitacion simple ($10), doble (15), premium (25)
# calcular el costo de la estadía
# Agregar radioButon  que permita seleccionar la cantidad de huéspedes (1, 2, 3)

import tkinter as tk
from tkinter import ttk, messagebox

def calculoReserva():
    dias = int ( entrada.get() )
    tipoHabitacion = entrada2.get()
    numeroHuespedes = int ( huespedes.get() )

    costoHabitacion=0

    if tipoHabitacion == 'Simple':
        costoHabitacion = 10

    elif tipoHabitacion == 'Doble':
        costoHabitacion = 15

    else:
        costoHabitacion =25

    messagebox.showinfo("Costo de reserva",
        f"El valor de la reserva es: {dias*costoHabitacion} para {numeroHuespedes} personas")



##############################
#### INTERFAZ #########

ventana = tk.Tk()
ventana.title("RESERVAS DE HOTEL")
ventana.geometry("450x150")

#NÚMERO DE DÍAS
tk.Label(ventana, text="Ingresar días: ").grid(row=0, column=0)
entrada = tk.Entry(ventana)
entrada.grid(row= 0, column=1)


#TIPO DE HABITACIÓN
tk.Label(ventana, text="Ingresar tipo de habitación").grid(row=1, column=0)
entrada2 = ttk.Combobox(ventana, values=["Simple", "Doble", "Premium"], state='readonly')
entrada2.grid(row= 1 , column=1)

#CANTIDAD DE HUÉSPEDES
huespedes = tk.StringVar()
tk.Label(ventana, text="Seleccionar cantidad de huespedes: ").grid(row=2, column=0)

rb_uno = tk.Radiobutton(ventana, text="1 Huesped  ", value=1, variable= huespedes)
rb_uno.grid(row=2, column=1)

rb_dos = tk.Radiobutton(ventana, text="2 Huéspedes", value=2, variable= huespedes)
rb_dos.grid(row=3, column=1)

rb_tres = tk.Radiobutton( ventana, text="3 Huéspedes", value= 3, variable= huespedes)
rb_tres.grid( row=4, column=1)


tk.Button(ventana, text="Reservar", command=calculoReserva).grid(row=5, column=1)


ventana.mainloop()