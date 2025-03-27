import tkinter as tk
from tkinter import ttk, filedialog
import csv

def mostrar():
    with open ("cars2.csv", 'r') as archivo:
        data = csv.reader(archivo)

       # listbox.insert(tk.END, data)
        listbox.delete(0, tk.END)
        for item in data :
            listbox.insert(tk.END, item)
    
        archivo.close()

def cargar():
    datos=[]
    with open('cars2.csv', 'r') as archivo:
        data = csv.reader(archivo)

        for item in data:
            datos.append(item)
    archivo.close()

    return datos


def filtro():
    precio = float (entry_filtro_num.get())
    datos = cargar()
    datosFiltrados =[]

    for item in datos:
       # print(item[-1])
        try:
            if precio <= float( item[-1] ):
                #print(item)
                datosFiltrados.append(item)
        except ValueError :
            print("ERROR" )
            

    listbox.delete(0, tk.END)
    for item in datosFiltrados:
        listbox.insert(tk.END, item)
    
    return datosFiltrados

def filtro2():
    estado = combo_valores.get()
    datos = filtro()
    datosFiltrados = []

    for item in datos:
        if estado == item[3]:
            datosFiltrados.append(item)

    listbox.delete(0, tk.END)
    for item in datosFiltrados:
        try:
            listbox.insert(tk.END, f"{item[0] }   {item[1] }    {item[2] }   {item[3]}  {item[-1]}")
        except ValueError:
            print("error")



# Crear ventana principal
ventana = tk.Tk()
ventana.title("Visualizador CSV con ListBox")


# Variables
archivo_csv = None
df = None
df_filtrado = None

# Widgets
lbl_archivo = tk.Label(ventana, text="Archivo CSV:")
lbl_archivo.grid(row=0, column=0, padx=5, )


lbl_filtro_num = tk.Label(ventana, text="Filtro precio:")
lbl_filtro_num.grid(row=1, column=0,)

entry_filtro_num = tk.Entry(ventana)
entry_filtro_num.grid(row=1, column=1,)


lbl_valores_combo = tk.Label(ventana, text="Valor a filtrar:")
lbl_valores_combo.grid(row=3, column=0, )

combo_valores = ttk.Combobox(ventana, values=["New","Used", "Certified"], state="readonly")
combo_valores.grid(row=3, column=1, padx=5)

btn_aplicar = tk.Button(ventana, text="Aplicar Filtros", command=filtro2)
btn_aplicar.grid(row=4, column=0, columnspan=2)


frame_listbox = tk.Frame(ventana)
frame_listbox.grid(row=5, column=0, columnspan=2)

#ARREGLO
listbox = tk.Listbox(frame_listbox,  width=70)
listbox.pack(expand=True)


mostrar()
ventana.mainloop()