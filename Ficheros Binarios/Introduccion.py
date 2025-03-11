#Los ficheros binarios son aquellos que cuentan con un formato de datos que no se puede leer directamente como texto
 
 
# 1.Leer un fichero binario
with open('ejemplo.bin', 'rb') as f:
    datos = f.read()
    print(datos)

# 2.Escribir en un fichero binario
with open('salida.bin', 'wb') as f:
    datos = bytearray([65,66,67,68])
    f.write(datos)

"""
Que es un bytearray?
Es una lista mutable de bytes.
Un byte es una unidad de información que puede almacenar valores entre 0 y 255.
Permite modificar los datos y manipularlos directamente, es muy útil ya que nos permite trabajar los bytes como si fuesen elementos de una lista.
"""

# 3.Leer y escribir datos binarios a partir de posiciones específicas
"""
Se puede manipular la posición de lectura y escritura usando seek() para movernos a una posición específica del fichero
"""
with open('secuencias.bin', 'wb') as f:
    datos = bytearray([10,20,30,40,50])
    f.write(datos)

with open('secuencias.bin', 'rb') as f:
    f.seek(2)
    datos = f.read(2)
    print(datos)
    
# 4.Trabajar con ficheros binarios grandes
with open('grande_fichero', 'rb') as f:
    while True:
        bloque = f.read(1024)
        if not bloque:
            break
        print(bloque)
