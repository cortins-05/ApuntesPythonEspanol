import tkinter as tk
from tkinter import ttk,messagebox

class AplicacionTareas:
    def __init__(self,root):
        self.root = root
        self.root.title("Lista de tareas")
        self.root.geometry("500x400")
        
        #Variables
        self.tareas = []
        
        #Marco principal
        marco_principal = ttk.Frame(root,padding="10")
        marco_principal.pack(fill=tk.BOTH,expand=True)
        
        #Marco superior para la entrada y boton
        marco_superior = ttk.Frame(marco_principal)
        marco_superior.pack(fill=tk.X,pady=10)
        
        #Entrada de texto
        self.entrada_tarea = ttk.Entry(marco_superior,width=40)
        self.entrada_tarea.pack(side=tk.LEFT,padx=5)
        self.entrada_tarea.bind("<Return>",lambda e:self.añadir_tarea())
        
        #Boton de añadir
        boton_añadir = ttk.Button(marco_superior,text="Añadir",command=self.añadir_tarea)
        boton_añadir.pack(side=tk.LEFT,padx=5)
        
        #Marco para la lista y barra de desplazamiento
        marco_lista = ttk.Frame(marco_principal)
        marco_lista.pack(fill=tk.BOTH,expand=True)
        
        #Listbox para tareas
        self.listBox = tk.Listbox(marco_lista,height=15,selectmode=tk.SINGLE)
        self.listBox.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        
        #Barra de desplazamiento
        scrollbar = ttk.Scrollbar(marco_lista,orient=tk.VERTICAL,command=self.listBox.yview)
        scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
        self.listBox.configure(yscrollcommand=scrollbar.set)
        
        #Marco para botones inferiores
        marco_botones = ttk.Frame(marco_principal)
        marco_botones.pack(fill=tk.X,pady=10)
        
        #Botones
        boton_eliminar = ttk.Button(marco_botones,text="Eliminar",command=self.eliminar_tarea)
        boton_eliminar.pack(side=tk.LEFT,padx=5)
        
        boton_completar = ttk.Button(marco_botones,text="Marcar como completada",command=self.marcar_completada)
        boton_completar.pack(side=tk.LEFT,padx=5)
        
        boton_limpiar = ttk.Button(marco_botones,text="Limpiar todo",command=self.limpiar_todo)
        boton_limpiar.pack(side=tk.RIGHT,padx=5)
    
    def añadir_tarea(self):
        tarea = self.entrada_tarea.get().strip()
        if tarea:
            self.tareas.append({"texto":tarea,"completada":False})
            self.actualizar_lista()
            self.entrada_tarea.delete(0,tk.END)
        else:
            messagebox.showwarning("Aviso","Introduce una tarea valida")
        
    def eliminar_tarea(self):
        try:
            indice = self.listBox.curselection()[0]
            del self.tareas[indice]
            self.actualizar_lista()
        except IndexError:
            messagebox.showwarning("Aviso","Selecciona una tarea para eliminar")
    
    def marcar_completada(self):
        try:
            indice = self.listBox.curselection()[0]
            self.tareas[indice]["completada"] = not self.tareas[indice]["completada"]
            self.actualizar_lista()
        except IndexError:
            messagebox.showwarning("Aviso","Selecciona una tarea")
        
    def limpiar_todo(self):
        if messagebox.askyesno("Confirmar","Quieres eliminar todas las tareas?"):
            self.tareas = []
            self.actualizar_lista()
        
    def actualizar_lista(self):
        self.listBox.delete(0,tk.END)
        for tarea in self.tareas:
            texto = tarea["texto"]
            if tarea["completada"]:
                texto = "✓" + texto
            else:
                texto = "□" + texto
            self.listBox.insert(tk.END,texto)

#Crear la aplicacion
root = tk.Tk()
app = AplicacionTareas(root)
root.mainloop()