"""
    r -> lectura
    w -> escritura
    a -> anexado
    rb, wb, ab -> modos binarios para trabajar con ficheros de texto    
"""

# 1.Lectura de un fichero
#Lo abrimos en modo lectura 'r'

#Métodos de lectura:
#   read(): Leer todo el contenido del fichero como una cadena de texto
#   readline():Leer una linea del fichero
#   readlines():Leer una línea del fichero y devuelve una lista de cadenas de texto


# 2.Escritura de un fichero
#Lo abrimos en modo escritura 'w' o anexado 'a'

#Métodos de escritura:
#   read(): Leer todo el contenido del fichero como una cadena de texto
#   readline():Leer una linea del fichero
#   readlines():Leer una línea del fichero y devuelve una lista de cadenas de texto

# 3. Cerrar un fichero
#   Se usa close(), lo que libera los recursos que se estaban usando del sistema

# 4. Usar with para el manejo de ficheros
#   Lo que hace es gestionar de forma automática la apertura y cierre de ficheros

#EJEMPLO:

fichero = open("introduccion.txt", "w+")
fichero.write("hola\nadios\nhola de nuevo")
fichero.close()

with open("introduccion.txt", "r") as archivo:
    print(archivo.read())
    