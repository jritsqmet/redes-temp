import tkinter as tk
from tkinter import ttk, messagebox
import csv


def guardar():
    nombre = entrada1.get()
    edad = entradaEdad.get()
    profesion = entradaProfesion.get()

    if not nombre or not edad or not profesion:
        messagebox.showwarning("Error", "Todos los campos son obligatorios")
        return

    with open("datos.csv", 'a', newline='') as archivo:
        writer = csv.writer(archivo)
        if archivo.tell() == 0: 
            writer.writerow(["Nombre", "Edad", "Profesión"])
        writer.writerow([nombre, edad, profesion])

    entrada1.delete(0, tk.END)
    entradaEdad.delete(0, tk.END)
    entradaProfesion.delete(0, tk.END)
    messagebox.showinfo("Éxito", "Datos guardados correctamente")
    leer_datos()  

def leer_datos():
    try:
        with open("datos.csv", 'r') as archivo:
            reader = csv.reader(archivo)
            datos = list(reader)
        
        for row in tabla.get_children():
            tabla.delete(row)
        
        for fila in datos:
            tabla.insert("", "end", values=fila)
    
    except FileNotFoundError:
        messagebox.showwarning("Error", "No hay datos guardados")

def eliminar_registro():
    seleccionado = tabla.selection()
    if not seleccionado:
        messagebox.showwarning("Error", "Seleccione un registro para eliminar")
        return


    item = tabla.item(seleccionado)
    valores = item['values']
    
    with open("datos.csv", 'r') as archivo:
        datos = list(csv.reader(archivo))
    

    datos = [fila for fila in datos if fila != valores]
    

    with open("datos.csv", 'w', newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerows(datos)
    
    messagebox.showinfo("Éxito", "Registro eliminado correctamente")
    leer_datos()  


def editar_registro():
    seleccionado = tabla.selection()
    if not seleccionado:
        messagebox.showwarning("Error", "Seleccione un registro para editar")
        return


    item = tabla.item(seleccionado)
    valores = item['values']
    

    entrada1.delete(0, tk.END)
    entrada1.insert(0, valores[0])
    entradaEdad.delete(0, tk.END)
    entradaEdad.insert(0, valores[1])
    entradaProfesion.delete(0, tk.END)
    entradaProfesion.insert(0, valores[2])


    eliminar_registro()


def ventana1():
    global entrada1, entradaEdad, entradaProfesion, tabla

    ventana = tk.Tk()
    ventana.title("Gestión de Datos")


    tk.Label(ventana, text="Ingresar Nombre").grid(row=0, column=0)
    entrada1 = tk.Entry(ventana)
    entrada1.grid(row=0, column=1)

    tk.Label(ventana, text="Ingresar Edad").grid(row=1, column=0)
    entradaEdad = tk.Entry(ventana)
    entradaEdad.grid(row=1, column=1)

    tk.Label(ventana, text="Ingresar Profesión").grid(row=2, column=0)
    entradaProfesion = tk.Entry(ventana)
    entradaProfesion.grid(row=2, column=1)


    tk.Button(ventana, text="GUARDAR", command=guardar, background='#7c75fa').grid(row=3, column=1)
    tk.Button(ventana, text="EDITAR", command=editar_registro, background='#fad775').grid(row=4, column=1)
    tk.Button(ventana, text="ELIMINAR", command=eliminar_registro, background='#fa7575').grid(row=5, column=1)


    tabla = ttk.Treeview(ventana, columns=("Nombre", "Edad", "Profesión"), show="headings")
    tabla.heading("Nombre", text="Nombre")
    tabla.heading("Edad", text="Edad")
    tabla.heading("Profesión", text="Profesión")
    tabla.grid(row=6, column=0, columnspan=2)


    leer_datos()

    ventana.mainloop()


ventana1()