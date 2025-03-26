"""
Que es el módulo Picke???
Es una herramienta que permite serializar y deserializar objetos, pero que significa:
    - Serializar: Convertir un objeto de Python en un flujo de bytes que se puede guardar en un fichero o se puede enviar por red
    - Deserializar: Convertir ese flujo de bytes de vuelta en un objeto de Python
Es como "congelar" un objeto en python y "descongelarlo" para usarlo de nuevo

Se usa para:
    - Guardar datos complejos en ficheros
    - Pasar objetos entre programas o sesiones de Python

Cómo funciona???
Pickle tiene las siguientes funciones principales para trabajar con ficheros:
    - pickle.dump(objeto, fichero) Guarda(serializa) un objeto en un fichero
    - pickle.load(fichero) Recupera (deserializa) un objeto de un fichero
    - pickle.dumps(objeto) Serializa un objeto a una cadena de bytes (útil para otras cosas como redes)
    - pickle.loads(objeto) Deserializa una cadena de bytes en un objeto
"""

#Ejemplo básico con pickle
import pickle
datos = ["Jose", 30, "Galicia"]
with open("datos.dat", "wb") as fichero:
    pickle.dump(datos, fichero)

with open("datos.dat", "rb") as fichero:
    datos_recuperados = pickle.load(fichero)

print(datos_recuperados)

"""
Por que usar pickle con objetos???
Cuando trabajas con objetos, pickle es muy util porque:
    - Guarda toda la estructura de un objeto, incluyendo sus atributos y métodos
    - No tienes que preocuparte por convertir los datos manualmente
"""

#Ejemplo con fichero de objetos

class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
        
    def __str__(self):
        return f"{self.nombre}-{self.edad} años-{self.profesion}"

def guardar_con_pickle(objetos, fichero):
    with open(fichero, "wb") as f:
        pickle.dump(objetos, f)

def cargar_de_pickle(fichero):
    with open(fichero, "rb") as f:
        return pickle.load(f)
    
def demo_manejo_ficheros():
    personas = [
        Persona("Maria", 28, "Desarrolladora"),
        Persona("Pedro", 35, "Diseñador"),
        Persona("Ana", 42, "Gestora de Proyectos")
    ]
    
    guardar_con_pickle(personas, "personas.pickle")
    personas_cargadas = cargar_de_pickle("personas.pickle")
    for persona in personas_cargadas:
        print(persona)

demo_manejo_ficheros()
        
    
