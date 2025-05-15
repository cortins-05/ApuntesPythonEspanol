import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import os

class EditorTexto:
    def __init__(self,root):
        self.root = root
        self.root.title("Editor de Texto")
        self.root.geometry("800x600")
        
        #Variables
        self.archivo_actual = None
        self.texto_modificado = False

        #Crear barra de menu
        self.crear_menu()
        
        #Crear área de texto
        self.crear_area_texto()
        
        #Crear la barra de estado
        self.crear_barra_de_estado()
        
        #Vincular eventos
        self.area_texto.bind("<<Modified>>",self.texto_cambiado)
        self.root.protocol("WM_DELETE_WINDOW",self.al_cerrar)
        
    def crear_menu(self):
        #Barra de menu principal
        menu_bar = tk.Menu(self.root)
        
        #Menu Archivo
        menu_archivo = tk.Menu(menu_bar,tearoff=0)
        menu_archivo.add_command(label="Nuevo",command=self.nuevo_archivo,accelerator="Ctrl+N")
        menu_archivo.add_command(label="Abrir",command=self.abrir_archivo,accelerator="Ctrl+O")
        menu_archivo.add_command(label="Guardar",command=self.guardar_archivo,accelerator="Ctrl+S")
        menu_archivo.add_command(label="Guardar Como",command=self.guardar_como)
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Salir",command=self.al_cerrar)
        menu_bar.add_cascade(label="Archivo",menu=menu_archivo)
        
        #Menú editar
        menu_editar = tk.Menu(menu_bar,tearoff=0)
        menu_editar.add_command(label="Deshacer",command=lambda:self.area_texto.event_generate("<<Undo>>"),accelerator="Ctrl+Z")
        menu_editar.add_command(label="Rehacer",command=lambda:self.area_texto.event_generate("<<Redo>>"),accelerator="Ctrl+Y")
        menu_editar.add_separator()
        menu_editar.add_command(label="Cortar",command=lambda:self.area_texto.event_generate("<<Cut>>"),accelerator="Ctrl+X")
        menu_editar.add_command(label="Copiar",command=lambda:self.area_texto.event_generate("<<Copy>>"),accelerator="Ctrl+C")
        menu_editar.add_command(label="Pegar",command=lambda:self.area_texto.event_generate("<<Paste>>"),accelerator="Ctrl+V")
        menu_editar.add_separator()
        menu_editar.add_command(label="Seleccionar todo",command=self.seleccionar_todo,accelerator="Ctrl+A")
        menu_bar.add_cascade(label="Editar",menu=menu_editar)
        
        #Menú formato
        menu_formato = tk.Menu(menu_bar,tearoff=0)
        submenu_fuente = tk.Menu(menu_formato,tearoff=0)
        submenu_fuente.add_command(label="Aumentar",command=self.aumentar_fuente)
        submenu_fuente.add_command(label="Disminuir",command=self.disminuir_fuente)
        menu_formato.add_cascade(label="Tamaño de fuente",menu=submenu_fuente)
        menu_bar.add_cascade(label="Formato",menu=menu_formato)
        
        #Menú ayuda
        menu_ayuda = tk.Menu(menu_bar,tearoff=0)
        menu_ayuda.add_command(label="Acerca de",command=self.mostrar_acerca_de)
        menu_bar.add_cascade(label="Ayuda",menu=menu_ayuda)
        
        #Configurar la barra de menu
        self.root.config(menu=menu_bar)
        
        #Atajos de teclado
        self.root.bind("<Control-n>",lambda e: self.nuevo_archivo())
        self.root.bind("<Control-o>",lambda e: self.abrir_archivo())
        self.root.bind("<Control-s>",lambda e: self.guardar_archivo())
        self.root.bind("<Control-a>",lambda e: self.seleccionar_todo())
        
    def crear_area_texto(self):
        #Marco para el area de texto
        marco_texto = ttk.Frame(self.root)
        marco_texto.pack(fill=tk.BOTH,expand=True)
        
        #Area de texto
        self.area_texto = tk.Text(marco_texto,wrap=tk.WORD,undo=True,font=("Consolas",11))
        self.area_texto.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        
        #Barra de desplazamiento vertical
        scrollbar_v = ttk.Scrollbar(marco_texto,orient=tk.VERTICAL,command=self.area_texto.yview)
        scrollbar_v.pack(side=tk.RIGHT,fill=tk.Y)
        self.area_texto.config(yscrollcommand=scrollbar_v.set)
        
        #Barra de desplazamiento horizontal
        scrollbar_h = ttk.Scrollbar(self.root, orient=tk.HORIZONTAL,command=self.area_texto.xview)
        scrollbar_h.pack(side=tk.BOTTOM,fill=tk.X)
        self.area_texto.config(xscrollcommand=scrollbar_h.set)
    
    def crear_barra_estado(self):
        #Barra de estado
        self.barra_estado = ttk.Label(self.root,text="Listo",anchor=tk.W)
        self.barra_estado.pack(side=tk.BOTTOM,fill=tk.X)
        
    def texto_cambiado(self,event=None):
        if self.area_texto.edit_modified():
            self.texto_modificado = True
            titulo = self.root.title()
            if not titulo.startswith("*"):
                self.root.title("*"+titulo)
            self.area_texto.edit

#Crear la aplicacion
root = tk.Tk()
app = EditorTexto(root)
root.mainloop()