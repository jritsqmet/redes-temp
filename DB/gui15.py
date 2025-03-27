import tkinter as tk
from tkinter import ttk, filedialog
import csv





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

btn_aplicar = tk.Button(ventana, text="Aplicar Filtros")
btn_aplicar.grid(row=4, column=0, columnspan=2)


frame_listbox = tk.Frame(ventana)
frame_listbox.grid(row=5, column=0, columnspan=2)


listbox = tk.Listbox(frame_listbox,  width=70)
listbox.pack(expand=True)



# Configurar expansión
ventana.grid_rowconfigure(5, weight=1)
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)




ventana.mainloop()