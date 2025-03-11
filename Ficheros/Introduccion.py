"""
    r -> lectura
    w -> escritura
    a -> anexado
    r+ -> Lectura y escritura
    w+ -> Lectura y escritura sin convervar el contenido
    a+ -> Lectura y escritura anexado
    x -> Abre el fichero para escritura SOLO si no existe, sino lanza ERROR
"""

# 1. Lectura de un fichero
# Para abrir un fichero en modo lectura, usamos 'r'

# Métodos de lectura:
#   - read(): Lee todo el contenido del fichero como una única cadena de texto.
#   - readline(): Lee una línea del fichero.
#   - readlines(): Lee todas las líneas del fichero y devuelve una lista de cadenas de texto.

# 2. Escritura de un fichero
# Para abrir un fichero en modo escritura, usamos 'w' (sobrescribe) o 'a' (anexar).

# Métodos de escritura:
#   - write(): Escribe una cadena de texto en el fichero.
#   - writelines(): Escribe una lista de cadenas en el fichero.

# 3. Cerrar un fichero
# Es importante cerrar el fichero después de usarlo para liberar recursos del sistema.
# Se usa el método close():
#   fichero.close()

# 4. Usar with para el manejo de ficheros
# La estructura 'with' gestiona automáticamente la apertura y cierre del fichero.
# Ejemplo:
#   with open("archivo.txt", "r") as fichero:
#       contenido = fichero.read()

# 5. Función seek()
# Permite mover el puntero del fichero a una posición específica.
# Sintaxis:
#   file.seek(offset, whence)
# Donde:
#   - offset: número de bytes a desplazar.
#   - whence:
#       0 -> Inicio del fichero (por defecto).
#       1 -> Posición actual del puntero.
#       2 -> Final del fichero.

# 6. Función tell()
# Indica la posición actual del puntero dentro del fichero.
# Ejemplo:
#   posicion = fichero.tell()

# 7. Función flush()
# Fuerza el guardado de los datos en el fichero antes de cerrarlo.
# Ejemplo:
#   fichero.flush()


#EJEMPLO:

fichero = open("introduccion.txt", "w+")
fichero.write("hola\nadios\nhola de nuevo")
fichero.close()

with open("introduccion.txt", "r") as archivo:
    print(archivo.read())
    