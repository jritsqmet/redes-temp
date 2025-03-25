#Crear una aplicación que permita gestionar la información
# de un estudiante
# Ingresar cedula, nombre, calificaciones (3)
# El programa debe generar un CRUD
# Implementar un botón que determine si el
# estudiante aprobó el curso, mediante el promedio de las
# 3 calificaciones con un promedio mayor o igual de 7
import tkinter as tk
from tkinter import messagebox
import csv

def mostrar():
    with open ("estudiantes.csv", 'r') as archivo:
        data = csv.reader(archivo)
        
        lista.delete(0, tk.END)
        for item in data:
            lista.insert(tk.END, item)
    archivo.close()     


def agregar_estudiante():
    cedula = cedulaEntrada.get()
    nombre = nombreENtrada.get()
    calificacion1 = float( calificacion1Entrada.get())
    calificacion2 = float( calificacion2Entrada.get() )
    calificacion3 = float( calificacion3Entrada.get() )

    promedio = (calificacion1 +calificacion2 +calificacion3) /3

    with open( "estudiantes.csv", 'a') as archivo :
        archivo.write(f"{cedula},{nombre},{calificacion1},{calificacion2},{calificacion3},{promedio}\n")

    mostrar()



    
##### ELIMINAR - EDITAR #####
def cargar():
    with open( "estudiantes.csv", 'r') as archivo:
        data = csv.reader(archivo)
        datos = []

        for item in data:
            datos.append(item)
    archivo.close()
    return datos

#ELIMINAR
def eliminar_estudiante():
    seleccionado = lista.curselection()
    datos = cargar()

    del datos[seleccionado[0]]

    with open ("estudiantes.csv", 'w') as archivo:
        data = csv.writer(archivo)
        data.writerows(datos)

    archivo.close()
    mostrar()

#EDITAR

def editar():
    seleccionado = lista.curselection()
    datos = cargar()

    cedula = cedulaEntrada.get()
    nombre = nombreENtrada.get()
    calificacion1 = calificacion1Entrada.get()
    calificacion2 = calificacion2Entrada.get()
    calificacion3 = calificacion3Entrada.get()

    datos[seleccionado[0]]= [cedula, nombre, calificacion1, calificacion2, calificacion3]

    with open( "estudiantes.csv", 'w') as archivo:
        data = csv.writer(archivo)
        data.writerows(datos)
    archivo.close()
    mostrar()


def ver_aprobacion():
    seleccionado = lista.curselection()
    datos = cargar()

    promedio = float( datos[seleccionado[0]][-1] )
    
    if promedio >= 7:
        messagebox.showinfo("Felicitaciones", "Estudiante aprobado")
    else:
        messagebox.showerror("NO APORBADO", "El estudiante no aprobó")
    


def limpiar_campos():
    ""

# Configuración de la ventana principal
root = tk.Tk()
root.title("Gestión de Estudiantes")
root.geometry("500x400")


# Etiquetas y campos de entrada para los datos del estudiante
tk.Label(root, text="Cédula:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
cedulaEntrada= tk.Entry(root, width=30)
cedulaEntrada.grid(row=0, column=1)

tk.Label(root, text="Nombre:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
nombreENtrada= tk.Entry(root, width=30)
nombreENtrada.grid(row=1, column=1)

tk.Label(root, text="Calificaciones:").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)

tk.Label(root, text="1:").grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
calificacion1Entrada= tk.Entry(root, width=5)
calificacion1Entrada.grid(row=3, column=1)

tk.Label(root, text="2:").grid(row=4, column=0, sticky=tk.W, padx=10, pady=5)
calificacion2Entrada= tk.Entry(root, width=5)
calificacion2Entrada.grid(row=4, column=1)

tk.Label(root, text="3:").grid(row=5, column=0, sticky=tk.W, padx=10, pady=5)
calificacion3Entrada=tk.Entry(root, width=5)
calificacion3Entrada.grid(row=5, column=1)

# Botones
tk.Button(root, text="Agregar",  command=agregar_estudiante).grid(row=6, column=0)
tk.Button(root, text="Editar",  command=editar).grid(row=6, column=1)
tk.Button(root, text="Eliminar",  command=eliminar_estudiante).grid(row=6, column=2)
tk.Button(root, text="Aprobación", command=ver_aprobacion).grid(row=6, column=3)

# Listbox con scroll
list_frame = tk.LabelFrame(root, text="Lista de Estudiantes", padx=10, pady=10)
list_frame.grid(row=7, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")

lista = tk.Listbox(list_frame, width=60)
lista.grid(row=0, column=0, )




# Aseguramos que los elementos de la ventana se ajusten adecuadamente
root.grid_rowconfigure(7, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)
root.grid_columnconfigure(4, weight=1)

mostrar()
root.mainloop()
