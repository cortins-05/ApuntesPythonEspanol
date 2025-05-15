"""
INTRODUCCIÓN A TKINTER:
Que es Tkinter?
Es una biblioteca estándar de python para crear interfaces gráficas de usuario (GUI). Es una capa de Python sobre el kit de herramientas Tk,
que fué originalmente desarrollada para el lenguaje Tcl.

Para que se usa?
    - Crear aplicaciones de escritorio
    - Desarrollar prototipos rápidos de interfaces
    - Crear herramientas visuales simples
    - Implementar aplicaciones que necesitan interacción por el usuario

Ventajas de Tkinter:
    - Viene preinstalado con la mayoría de distribuciones Python
    - Es multiplataforma
    - Es simple y sencillo de usar
    - Ofrece un buen equilibrio entre simplicidad y funcionalidad

Elementos principales:
    1. Tk(); la clase principal para crear una app gráfica. Este objeto gestiona la ventana principal de la aplicación
    2. Widgets; son los componentes gráficos que añadimos a la ventana
    3. Event loop; un ciclo que mantiene en ejecución para que la ventana permanezca abierta y podamos interactuar con ella
"""

#Toda aplicación sigue una estructura similar:
import tkinter as tk

#Crear la ventana principal
root = tk.Tk()
root.title("Mi aplicación")
root.geometry("600x1000") #Ancho x alto

#Añadir widgets
label = tk.Label(root,text="Hola Mundo!")
label.pack()

boton = tk.Button(root,text="Pulsa aquí",command=lambda:print("Boton presionado!"))
boton.pack()

#El método mainloop() inicia el bucle de eventos de la aplicación que espera por las interacciones del usuario y responde a ellas

"""
WIDGETS PRINCIPALES:
Label (Etiqueta):
Se usa para mostrar textos o imágenes:
"""
label = tk.Label(root,text="Esto es una etiqueta",font=("Arial",14),fg="blue")
label.pack()

#Con imagen
imagen = tk.PhotoImage(file="imagen.png",width="100",height="100")
label_con_imagen=tk.Label(root,image=imagen)
label_con_imagen.pack()

"""
Button (Botón):
Permite al usuario ejecutar una accion cuando se presiona:
"""
def accion_boton():
    print("Boton presionado")
boton = tk.Button(root,text="Presione aqui",command=accion_boton,bg="lightblue",fg="black",padx=10,pady=5)
boton.pack()

"""
Entry (Campo de texto):
Permite al usuario introducir texto en una sola línea:
"""
entrada = tk.Entry(root,width=30)
entrada.pack()
#Para obtener el texto introducido
def obtener_texto():
    texto = entrada.get()
    print(f"Texto introducido = {texto}")
boton_obtener = tk.Button(root,text="Obtener texto",command=obtener_texto)
boton_obtener.pack()

"""
Text (Area de texto):
Para texto multilínea:
"""
area_texto = tk.Text(root,width=40,height=10)
area_texto.pack()
#Para obtener texto
def obtener_texto_area():
    texto = area_texto.get("1.0",tk.END) #Desde la linea uno caracter 0
    print(texto)
boton_texto_area = tk.Button(root,text="Obtener texto 2",command=obtener_texto_area)
boton_texto_area.pack()

"""
CheckButton (Caja de verificación):
Para opciones que pueden estar activadas o desactivadas:
"""
#Variable para almacenar el estado
estado_var = tk.BooleanVar()
check = tk.Checkbutton(root,text="Activar opcion",variable=estado_var)
check.pack()

def comprobar_estado():
    print(f"Estado:{"activado" if estado_var.get() else "desactivado"}")

boton_check = tk.Button(root,text="Verificar el estado",command=comprobar_estado)
boton_check.pack()

"""
Radiobutton (Botón de radio):
Para seleccionar una opción entre varias:
"""
opcion_var = tk.StringVar(value="opcion1") #Valor por defecto
radio1 = tk.Radiobutton(root,text="Opcion 1",variable=opcion_var,value="opcion1")
radio2 = tk.Radiobutton(root,text="Opcion 2",variable=opcion_var,value="opcion2")
radio3 = tk.Radiobutton(root,text="Opcion 3",variable=opcion_var,value="opcion3")

radio1.pack()
radio2.pack()
radio3.pack()

def obtener_opcion():
    print(f"Opcion seleccionada: {opcion_var.get()}")

opcion_var_boton = tk.Button(root,text="Obtener opcion",command=obtener_opcion)
opcion_var_boton.pack()

"""
List box (Lista de selección):
Para seleccionar uno o varios elementos de una lista:
"""
lista = tk.Listbox(root,height=5)
elementos = ["Elemento1","Elemento2","Elemento3","Elemento4","Elemento5"]
for elemento in elementos:
    lista.insert(tk.END,elemento)
lista.pack()

#Para obtener el elemento seleccionado
def obtener_seleccion():
    seleccion = lista.curselection()
    if seleccion:
        print(f"Seleccionado: {lista.get(seleccion[0])}")

boton_seleccion = tk.Button(root,text="Obtener seleccion",command=obtener_seleccion)
boton_seleccion.pack()

"""
Combobox (Lista desplegable):
Para seleccionar un elemento de una lista desplegable:
"""
from tkinter import ttk #Contiene widgets más modernos

combo = ttk.Combobox(root,values=["Opcion1","Opcion2","Opcion3"])
combo.current(0)
combo.pack()

def obtener_combo():
    print(f"Seleccionado: {combo.get()}")

boton_combo = tk.Button(root,text="Obtener combo",command=obtener_combo)
boton_combo.pack()

"""
Scale (Control deslizante):
Para seleccionar un valor dentro de un rango:
"""
valor_var = tk.DoubleVar()
escala = tk.Scale(root,from_=0,to=100,orient=tk.HORIZONTAL,variable=valor_var,length=200)
escala.pack()

def obtener_escala():
    print(f"Valor: {valor_var.get()}")

boton_escala = tk.Button(root,text="Obtener escala",command=obtener_escala)
boton_escala.pack()

"""
Frame (Marco):
Para agrupar y reorganizar otros widgets:
"""
marco = tk.Frame(root,bd=2,relief=tk.SUNKEN,padx=10,pady=10)
marco.pack(fill=tk.BOTH,expand=True)

#Ahora podemos añadir widgets a dicho marco
label_marco = tk.Label(marco,text="Esto está dentro de un marco")
label_marco.pack()

#Iniciar el bucle principal de la aplicacion
root.mainloop()