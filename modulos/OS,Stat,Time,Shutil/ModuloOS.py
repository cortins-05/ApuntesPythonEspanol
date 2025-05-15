"""
QUÉ ES EL MÓDULO OS?
El módulo OS en Python es un módulo de la biblioteca estándar que permite interactuar con el sistema operativo en el que se está ejecutando código.
A través de este módulo, puedes realizar varias operaciones relacionadas con el sistema, como manipulación de archivos y directorios, o mismo interactuar
con variables de entorno y recursos del sistema 

Por ejemplo con el módulo OS puedes:
- Acceder y modificar archivos y directorios
- Ejecutar comandos del sistema operativo
- Trabajar con variables de entorno
- Obtener información sobre el sistema, como el nombre del sistema operativo o el camino absoluto a un archivo

"""

#Como importarlo:
import os

#EJEMPLO BÁSICO
#Ver el directorio de trabajo actual
directorio_actual = os.getcwd()
print(f"El directorio actual es {directorio_actual}")

#Cambiar el directorio de trabajo
os.chdir("../.")
print(f"El nuevo directorio es {os.getcwd()}")

#Listar archivos de un directorio
archivos = os.listdir()
print(f"El contenido del directorio actual es:\n{archivos}")

"""
VENTAJAS DEL MÓDULO OS:
- Portabilidad; El módulo OS permite escribir código que puede ejecutarse sin problemas tanto en sistemas Linux/Unix como en Windows
- Integración con el sistema

Elementos:
os.getcwd() -> Obtiene el directorio de trabajo actual
os.chdir(path) -> Cambia al directorio de trabajo
os.listdir(path) -> Lista los archivos dentro de un directorio de trabajo especificado
os.mkdir(path) -> Crea un directorio en el camino especificado
os.makedirs(path) -> Crea directorios de forma recursiva (si no existen)
os.rmdir(path) -> Elimina un directorio, pero solo si está vacío
os.remove(path) -> Elimina un archivo
os.remane(src, dst) -> Renombra un archivo en el directorio src a dst
os.path.exists(path) -> Verifica si el archivo o directorio existe
os.path.abspath(path) -> Obtiene el camino absoluto de un archivo o directorio
os.path.join(a, b) -> Une dos caminos de forma segura para formar un camino completo
os.path.isfile(path) -> Verifica si el camino especificado es un archivo
os.path.isdir(path) -> Verifica si un camino especificado es un directorio
os.path.split(path) -> Separa un camino en dos: la parte del directorio y el nombre del archivo
os.system(comand) -> Ejecuta un comando en el sistema operativo
os.environ -> Accede o modifica las variables de entorno del sistema operativo
os.sep -> Obtiene el separador de directorios adecuado del sistema operativo
os.name -> Obtiene el nombre del sistema operativo

NOTAS ADICIONALES:
1. Buenas prácticas:
    - Usa os.path.join() para construir rutas en lugar de concatenar cadenas manualmente ya que maneja correctamente los separadores / o \ según el SO
    - Comprueba siempre si un fichero o directorio existe con os.path.exists() antes de realizar operaciones para evitar errores
    - Para operaciones más complejas con ficheros y directorios considera usar el módulo pathlib, que es una alternativa moderna más intuitiva

"""