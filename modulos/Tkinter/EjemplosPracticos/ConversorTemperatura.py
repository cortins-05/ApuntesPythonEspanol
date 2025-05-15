import tkinter as tk
from tkinter import ttk

def conversor():
    try:
        celsius = float(entrada_celsius.get())
        fahrenheit = (celsius * 9.5) + 32
        resultado_var.set(f"{fahrenheit: .2f}ºF")
    except ValueError:
        resultado_var.set("Error: Introduce un numero válido")

#Crear la ventana principal
root = tk.Tk()
root.title("Conversor de Temperatura")
root.geometry("350x200")
root.resizable(False,False)

#Crear un marco con padding
marco = ttk.Frame(root,padding="20")
marco.pack(fill=tk.BOTH,expand=True)

#Variables
resultado_var = tk.StringVar()
ttk.Label(marco,text="Temperatura en Celsius:").grid(row=0,column=0,sticky=tk.W,pady=5)
entrada_celsius = ttk.Entry(marco,width=10)
entrada_celsius.grid(row=0,column=1,pady=5)
ttk.Label(marco,text="ºC").grid(row=0,column=2,sticky=tk.W,pady=5)

ttk.Button(marco,text="Convertir",command=conversor).grid(row=1,column=0,columnspan=3,pady=10)

ttk.Label(marco,text="Resultado:").grid(row=2,column=0,sticky=tk.W,pady=5)
ttk.Label(marco,textvariable=resultado_var).grid(row=2,column=1,columnspan=2,sticky=tk.W,pady=5)

#Iniciar el bucle principal
root.mainloop()
        