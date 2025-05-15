import tkinter as tk

root = tk.Tk()
root.title("Mi aplicacion 3")
root.geometry("600x1000")


# Place() -> permite colocar los widgets en coordenadas exactas
boton1 = tk.Button(root,text="Posicion absoluta")
boton1.place(x=50,y=50)

boton2 = tk.Button(root,text="Posicion relativa")
boton2.place(relx=0.5,rely=0.5,anchor=tk.CENTER)

"""
Parámetros principales:
    - x/y -> coordenadas en píxeles
    - relx/rely -> coordenadas relativas
    - width/height -> tamaño en píxeles
    - relwidth/relheight -> tamaño relativo
    - anchor -> punto de anclaje (tk.CENTER,tk.NW,tk.SE,etc)
"""


root.mainloop()