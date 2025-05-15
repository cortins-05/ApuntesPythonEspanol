import tkinter as tk

root = tk.Tk()
root.title("Mi aplicacion 3")
root.geometry("600x1000")


# Pack() -> Organiza los widgets y los coloca en la ventana


boton1 = tk.Button(root,text="Boton1")
boton1.pack(side=tk.LEFT,padx=10)

boton2 = tk.Button(root,text="Boton2")
boton2.pack(side=tk.RIGHT,padx=10)

boton3 = tk.Button(root,text="Boton3")
boton3.pack(side=tk.TOP,pady=10)

boton4 = tk.Button(root,text="Boton4")
boton4.pack(side=tk.BOTTOM,pady=10)

"""
Parámetros principales:
    - side -> posición (tk.TOP,tk.BOTTOM,tk.LEFT,tk.RIGHT)
    - fill -> como llenar el espacio (tk.X,tk.Y,tk.BOTH)
    - expand -> si se debe expandir para ocupar el espacio disponible (True/False)
    - padx/pady -> espacio externo horizontal/vertical
    - ipadx/ipady -> espacio interno horizontal/vertical
"""

root.mainloop()