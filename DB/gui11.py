import tkinter as tk
from tkinter import filedialog

def cargarDocumento():
    archivo = filedialog.askopenfilename( filetypes= [ ("Archivos de texto", "*.csv"), ("Todos", "*.*") ] )

    with open( archivo , 'r', ) as documento:
        contenido = documento.read()
        texto.config(state='normal')
        texto.delete(1.0, tk.END)
        texto.insert(tk.END, contenido)
        texto.config(state='disabled')





def leerVentana():
    global texto
    ventana = tk.Tk()
    ventana.title("LEER INFORMACIÓN")

    tk.Button(ventana, text="Cargar documento", command= cargarDocumento ).grid(row=0)
    texto = tk.Text(ventana, state='disabled')
    texto.grid(row=1)


    ventana.mainloop()

leerVentana()