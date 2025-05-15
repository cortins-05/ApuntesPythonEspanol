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
Menu (Menú):
Para crear barras de menu:
"""
barra_menu = tk.Menu(root)
root.config(menu=barra_menu)

#Menú archivo
menu_archivo = tk.Menu(barra_menu,tearoff=0)
barra_menu.add_cascade(label="Archivo",menu=menu_archivo)
menu_archivo.add_command(label="Nuevo",command=lambda:print("Nuevo archivo"))
menu_archivo.add_command(label="Abrir",command=lambda:print("Abrir archivo"))
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir",command=root.quit)

#Menu editar
menu_editar = tk.Menu(barra_menu,tearoff=0)
barra_menu.add_cascade(label="Editar",menu=menu_editar)
menu_editar.add_command(label="Cortar",command=lambda:print("Cortar"))
menu_editar.add_command(label="Copiar",command=lambda:print("Copiar"))
menu_editar.add_command(label="Pegar",command=lambda:print("Pegar"))

"""
Eventos y vinculaciones:
Los eventos permiten que la aplicación responda a acciones del usuario:
"""

def click_izquierdo(event):
    print(f"Click en la posicion ({event.x},{event.y})")

def click_derecho(event):
    print("Click derecho")

def tecla_presionada(event):
    print(f"Tecla presionada: {event.char}, codigo: {event.keysym}")

#Vinculacion de eventos
root.bind("<Button-1>",click_izquierdo)
root.bind("<Button-3>",click_derecho)
root.bind("<Key>",tecla_presionada)
root.bind("<Return>",lambda e: print("Enter presionado"))
root.bind("<B1-Motion>",lambda e:print(f"Arrastre: ({e.x},{e.y})"))

"""
Otros eventos comunes:
    - "<Enter>": El cursor entra en un widget
    - "<Leave>" : El cursor sale de un widget
    - "<FocusIn>" : El widget recibe el foco
    - "<FocusOut>" : El widget pierde el foco
    - "<Configure>" : El widget cambia de tamaño o posicion
    - "<Double-Button-1>" : Doble click con el botón izquierdo
"""

"""
Diálogos:
Tkinter proporciona diálogos predefinidos para tareas comunes:
"""
from tkinter import messagebox,filedialog,colorchooser,simpledialog

#Diálogo de mensaje 
def mostrar_mensaje():
    messagebox.showinfo("Información","Esta és un mensaje informativo")
    messagebox.showwarning("Aviso","Este es un mensaje de aviso")
    messagebox.showerror("Error","Esta es una mensaje de error")
    
    #Dialogo de pregunta
    respuesta = messagebox.askquestion("Pregunta","Quieres continuar?")
    if respuesta=="yes":
        print("Respondio Si")
    else:
        print("Respondio No")
    
    #Otras variantes
    messagebox.askokcancel("Confirmación","Quieres proceder?")
    messagebox.askyesno("Pregunta Si/No","Estas seguro?")
    messagebox.askyesnocancel("Pregunta con cancelación","Quieres guardar antes de salir?")

#Diálogo de selección de archivo
def seleccionar_archivo():
    ruta_archivo = filedialog.askopenfilename(
        title="Selecciona un archivo",
        filetypes=[("Archivos de texto","*.txt"),("Todos los archivos","*.*")]
    )
    
#Diálogo de guardar archivo
def guardar_archivo():
    ruta_guardar = filedialog.asksaveasfilename(
        title="Guardar archivo como:",
        defaultextension=".txt",
        filetypes=[("Archivos de texto","*.txt"),("Todos los archivos","*.*")]
    )
    print(f"Guardar en: {ruta_guardar}")

#Diálogo de selección de directorio
def seleccionar_directorio():
    directorio=filedialog.askdirectory(title="Seleccionar directorio")
    print(f"Directorio seleccionado: {directorio}")

#Diálogo de selección de color
def seleccionar_color():
    color_tupla = colorchooser.askcolor(title="Selecciona un color")
    #Devuelve una tupla con codigo RGB, codigo hexadecimal
    print(f"Color seleccionada: {color_tupla[1]}")

#Diálogo de entrada
def obtener_entrada():
    nombre = simpledialog.askstring("Nombre","Como te llamas?")
    edad = simpledialog.askinteger("Edad","Cuantos años tienes?",minvalue=0,maxvalue=120)
    peso = simpledialog.askfloat("Peso","Cual es tu peso en kg?",minvalue=0)
    print(f"Nombre: {nombre}, Edad: {edad}, Peso: {peso}")

mostrar_mensaje()
seleccionar_archivo()
guardar_archivo()
seleccionar_directorio()
seleccionar_color()
obtener_entrada()

root.mainloop()