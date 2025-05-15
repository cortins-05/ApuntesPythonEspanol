import tkinter as tk

root = tk.Tk()
root.title("Mi aplicacion 3")
root.geometry("600x1000")

#GRID() -> organiza los widgets en filas y columnas

# Etiquetas
tk.Label(root,text="Nombre: ").grid(row=0,column=0,sticky=tk.W,padx=5,pady=5)
tk.Label(root,text="Email: ").grid(row=1,column=0,sticky=tk.W,padx=5,pady=5)

# Campos de entrada
entrada_nombre = tk.Entry(root)
entrada_nombre.grid(row=0,column=1,padx=5,pady=5)

entrada_email = tk.Entry(root)
entrada_email.grid(row=1,column=1,padx=5,pady=5)

#Boton que ocupa dos columnas
boton = tk.Button(root,text="Enviar")
boton.grid(row=2,column=0,columnspan=2,padx=5,pady=5)


"""
Parámetros principales:
    - row/column -> posición en la cuadrícula
    - rowspan/colspan -> número de filas/columnas que ocupa
    - sticky -> a qué borde adherirse (tk.N,tk.S,tk.E,tk.W o combinaciones)
    - pax/pady -> espacio externo
"""


root.mainloop()