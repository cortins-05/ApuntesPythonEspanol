"""
El modulo shutil proporciona varias funciones de alto nivel para copiar, mover y eliminar ficheros o directorios,
así como otras tareas relacionadas con la gestión de archivos

FUNCIONES PRINCIPALES:
- shutil.copy() -> copia un fichero de un directorio a otro
- shutil.move() -> mueve un fichero de un directorio a otro
- shutil.rmtree() -> elimina un directorio y todo su contenido de manera recursiva
- shutil.make_archive() -> crea un archivo comprimido
"""

#EJEMPLO PRÁCTICO
import shutil
import os

with open("ejemplo.txt", "w") as f:
    f.write("Este es un fichero de ejemplo")

shutil.copy("ejemplo.txt", "ejemplo_copy.txt")
print("Fichero copiado correctamente")

shutil.move("ejemplo_copy.txt", "ejemplo_moved.txt")
print("Fichero movido correctamente")

os.makedirs("ejemplo_dir",exist_ok=True)
shutil.move("ejemplo.txt", "ejemplo_dir/")
print("Fichero movido a ejemplo_dir")

"""
- shutil.copy() -> copia el fichero ejemplo.txt a ejemplo_copy.txt
- shutil.move() -> mueve el fichero original a otro nombre o directorio
- shutil.rmtree() -> elimina un directorio y todo su contenido
"""

#Tambien se puede crear comprimidos...
shutil.make_archive("ejemplo_dir_comprimido","zip", "ejemplo_dir")
print("Archivo comprimdo creado")

shutil.rmtree("ejemplo_dir")
print("Directorio ejemplo_dir eliminado")

