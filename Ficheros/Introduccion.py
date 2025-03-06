"""
    r -> lectura
    w -> escritura
    a -> anexado
    r+ -> Lectura y escritura
    w+ -> Lectura y escritura sin convervar el contenido
    a+ -> Lectura y escritura anexado
    x -> Abre el fichero para escritura SOLO si no existe, sino lanza ERROR
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

# 5. Funcion seek()
#   Sintaxis-> file.seek(offset, whence) Donde offset es la distancia a la posicion indicada por whence-> whence = 0 (defecto) inicio, whence = 1 desde la posicion actual del puntero, whence = 2 desde el final del fichero

# 6. Funcion tell() -> indica la posicion actual del puntero en el fichero
#   fichero.tell()

# 7. Funcion flush() -> fuerza el guardado de los datos en el fichero antes del close()
#   fichero.flush()

#EJEMPLO:

fichero = open("introduccion.txt", "w+")
fichero.write("hola\nadios\nhola de nuevo")
fichero.close()

with open("introduccion.txt", "r") as archivo:
    print(archivo.read())
    