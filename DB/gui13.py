#Crear un programa que permita realizar un CRUD par la gestión
#de una tienda tecnológica

import tkinter as tk
from tkinter import messagebox 
import csv
import os

#MUESTRA INFORMACIÓN EN LA LISTA
def mostrar():
    if ( os.path.exists("datos.csv") == False):
        with open ("datos.csv", 'w') as archivo:
            archivo.write(f"{'ID':<0},{'PRODUCTO':<30},{'CANTIDAD':<30},{'PRECIO':<30}\n")

    with open ("datos.csv", 'r') as archivo :
        data = csv.reader(archivo)

        lista.delete(0, tk.END)
        for item in data:
            lista.insert(tk.END, f"{item[0]:<10} {item[1]:<30} {item[2]:<30} {item[3]:<30}")

        archivo.close()

# GUARDAR REGISTROS
def guardar():
    id = entradaID.get()
    producto = entradaProducto.get()
    cantidad = entradaCantidad.get()
    precio = entradaPrecio.get()

    if id.strip() != "" and producto.strip()!= "" and cantidad.strip() != "" and precio.strip() != "" :
        with open("datos.csv", 'a') as archivo:
                
                archivo.write(f"{id},{producto},{cantidad},{precio}\n")
        archivo.close()

        entradaID.delete(0, tk.END)
        entradaProducto.delete(0, tk.END)
        entradaCantidad.delete(0, tk.END)
        entradaPrecio.delete(0, tk.END)
    else:
        messagebox.showerror("ERROR", "No se permiten campos en blanco")

    


    mostrar()
#################################
def cargar():
    with open( "datos.csv", 'r') as archivo:
        data = csv.reader(archivo)

        datos=[]
        for item in data:
            datos.append(item)

    archivo.close()
    return datos


#ELIMINAR REGISTROS
def eliminar():
    datos = cargar()
    seleccionado = lista.curselection() # asigna el id del elemento seleccionado


    try:
        if seleccionado[0] != 0 :
            del datos[ seleccionado[0]]
        else:
            messagebox.showerror("ERROR", "No se pueden eliminar las cabeceras")

        with open ("datos.csv", 'w') as archivo:
            data = csv.writer(archivo)
            data.writerows(datos)

        archivo.close()
    except IndexError:
        messagebox.showerror("ERROR", "No se ha seleccionado ningún elemento")
    mostrar()

#EDITAR
def editar():
    datos= cargar()
    seleccionado = lista.curselection()

    id = entradaID.get()
    producto = entradaProducto.get()
    cantidad = entradaCantidad.get()
    precio = entradaPrecio.get()
    try:
        if seleccionado[0] != 0  and id.strip()!="" and producto.strip() != "" and cantidad.strip() != "" and precio.strip() != "":
            datos[seleccionado[0]] = [id, producto, cantidad, precio]

            with open("datos.csv", 'w') as archivo:
                data = csv.writer(archivo)
                data.writerows(datos)

            archivo.close()

            entradaID.delete(0, tk.END)
            entradaProducto.delete(0, tk.END)
            entradaCantidad.delete(0, tk.END)
            entradaPrecio.delete(0, tk.END)
        else:
            messagebox.showerror("ERROR", "No se permiten campos en blanco y tampoco seleccionar las cabeceras")
    except IndexError:
        messagebox.showerror("ERROR", "Debe seleccionar un elemento a editar")
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
lista = tk.Listbox(ventana, width=60)
lista.grid( row=6, column=0, columnspan=3)


mostrar()

ventana.mainloop()