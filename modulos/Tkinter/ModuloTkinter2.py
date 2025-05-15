import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Mi aplicacion 2")
root.geometry("600x1000")

"""
Canvas (Lienzo):
Para dibujar gráficos y crear widgets personalizados:
"""
lienzo = tk.Canvas(root,width=300,height=200,bg="white")
lienzo.pack()

#Dibujar una linea
lienzo.create_line(0,0,300,200,fill="red",width=3)

#Dibujar un rectangulo
lienzo.create_rectangle(50,50,150,100,fill="blue")

#Dibujar un óvalo
lienzo.create_oval(200,50,280,120,fill="green")

#Dibujar texto
lienzo.create_text(150,150,text="Texto en el lienzo",font=("Arial",12))

"""

"""


root.mainloop()