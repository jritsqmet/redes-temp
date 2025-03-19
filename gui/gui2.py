import tkinter as tk

def multiplo():
    try: 
        numero = int( entrada.get()  ) 
        if (numero % 3) == 0:
            print("Es múltiplo de 3")
        else:
            print("No es múltiplo de 3")
            
    except ValueError:
        print("Por favor ingresar solo números")


#########################################################
################# INTERFAZ GRÁFICA ######################
#DECLARACIÓN INICIAL
ventana = tk.Tk()
ventana.title("Múltiplos de 3")
ventana.geometry("400x120")

#ETIQUETA
etiqueta = tk.Label(ventana, text="Ingresar un número", font="Arial 25")
etiqueta.pack()

#ENTRADA
entrada = tk.Entry(ventana, font="Arial 20")
entrada.pack()

#BOTON
boton = tk.Button(ventana, text="CÁLCULAR", font=("Arial 12"), command=multiplo)
boton.pack()


#VISUALIZAR
ventana.mainloop()