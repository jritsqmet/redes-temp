#Crear un programa que permita realizar un CRUD par la gestión
#de una tienda tecnológica

import tkinter as tk
import csv

#MUESTRA INFORMACIÓN EN LA LISTA
def mostrar():
    with open ("datos.csv", 'r') as archivo :
        data = csv.reader(archivo)

        lista.delete(0, tk.END)
        for item in data:
            lista.insert(tk.END, item)

        archivo.close()

# GUARDAR REGISTROS
def guardar():
    id = entradaID.get()
    producto = entradaProducto.get()
    cantidad = entradaCantidad.get()
    precio = entradaPrecio.get()

    with open("datos.csv", 'a') as archivo:
        
        archivo.write(f"{id},{producto},{cantidad},{precio}\n")

    archivo.close()
    mostrar()
#################################
def cargar():
    with open( "datos.csv", 'r') as archivo:
        data = csv.reader(archivo)

        datos=[]
        for item in data:
            datos.append(item)
       
    return datos


#ELIMINAR REGISTROS
def eliminar():
    datos = cargar()
    seleccionado = lista.curselection() # asigna el id del elemento seleccionado

    del datos[ seleccionado[0]]

    with open ("datos.csv", 'w') as archivo:
        data = csv.writer(archivo)
        data.writerows(datos)

    mostrar()

#EDITAR
def editar():
    datos= cargar()
    seleccionado = lista.curselection()

    id = entradaID.get()
    producto = entradaProducto.get()
    cantidad = entradaCantidad.get()
    precio = entradaPrecio.get()

    datos[seleccionado[0]] = [id, producto, cantidad, precio]

    with open("datos.csv", 'w') as archivo:
        data = csv.writer(archivo)
        data.writerows(datos)

    mostrar()




ventana = tk.Tk()
ventana.title("CRUD")

tk.Label(ventana, text= "CRUD CON CSV").grid(row=0, column=0, columnspan=2)

#ID
tk.Label(ventana, text= "ID. Producto: ").grid(row=1, column=0)
entradaID = tk.Entry(ventana)
entradaID.grid(row=1, column=1)

#Producto
tk.Label(ventana, text="Producto").grid(row=2, column=0)
entradaProducto = tk.Entry(ventana)
entradaProducto.grid(row=2, column=1)

#Cantidad
tk.Label(ventana, text="Cantidad").grid(row=3, column=0)
entradaCantidad = tk.Entry(ventana)
entradaCantidad.grid(row=3, column=1)

#Precio
tk.Label(ventana, text="Precio").grid(row=4, column=0)
entradaPrecio = tk.Entry()
entradaPrecio.grid(row=4, column=1) 

#BOTONES - CRUD
tk.Button(ventana, text="GUARDAR", command=guardar).grid( row=5, column=0)
tk.Button(ventana, text="ELIMINAR", command= eliminar).grid(row=5, column=1)
tk.Button(ventana, text="EDITAR", command=editar).grid(row=5, column=2)


#LISTA
lista = tk.Listbox(ventana, width=40)
lista.grid( row=6, column=0, columnspan=3)


mostrar()

ventana.mainloop()