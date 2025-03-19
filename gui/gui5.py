#Crear un programa que pida el salario de una persona, 
# el total de horas trabajadas (al mes), si las horas son mayores de 40
# se pagarán horas extra.
# El valor por cada hora extra es de $7.25

import tkinter as tk

def calcularSalario():
    salario = float ( entrada1.get()  )
    horas = int( entrada2.get() )

    ventana2 = tk.Tk()
    ventana2.geometry("200x100")

    if horas > 40:
        horasExtra = horas - 40

        salarioFinal = salario + ( horasExtra* 7.25 )
        etiqueta3 = tk.Label(ventana2,
            text= f"El salario final es {salarioFinal}")
        etiqueta3.pack()

        ventana2.mainloop()



######################################################
ventana = tk.Tk()
ventana.title("CÁLCULO SALARIO")
ventana.geometry("400x150")

etiqueta1 = tk.Label(ventana, text="Ingresar salario")
etiqueta1.pack()

entrada1 = tk.Entry(ventana)
entrada1.pack()

etiqueta2 = tk.Label(ventana, text="Ingresar total de horas")
etiqueta2.pack()

entrada2 = tk.Entry(ventana)
entrada2.pack()

boton = tk.Button(ventana, text="Calcular salario", command=calcularSalario)
boton.pack()

ventana.mainloop()
