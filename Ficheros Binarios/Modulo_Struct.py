"""
El modulo struct sirve para trabajar con datos binarios de manera eficiente, permitiendo empaquetar(convertir datos en formato binario) y desempaquetar
(convertir datos en formatos legibles) diferentes tipos de datos.
Su función principal es realizar conversiones entre tipos de datos(como enteros, flotantes, caracteres, etc) a su formato binario correspondiente


PRINCIPALES FUNCIONES DEL MODULO STRUCT:
    1. struct.pack()
    2. struct.unpack()
    
ESPECIFICACIONES DE FORMATO:
    1. 'i' -> Un numero entero (4 bytes)
    2. 'f' -> Un nummero flotante (4 bytes)
    3. 'd' -> Un numero flotante de doble precisión (8 bytes)
    4. 's' -> Un string
    5. 'b' -> Un entero de 1 byte (signed char)
    6. 'B' -> Un entero de 1 byte (unsigned char)
"""

#Como guardar un INT en un fichero binario
import struct

edades = [25, 30, 22, 40, 35]
with open('edades.bin', 'wb') as f:
    for edad in edades:
        f.write(struct.pack('i', edad))

edades_recuperadas = []
with open('edades.bin', 'rb') as f:
    while True:
        datos = f.read(4)
        if not datos:
            break
        edad = struct.unpack('i', datos)[0]
        edades_recuperadas.append(edad)
print(edades_recuperadas)

#Como guardar un FLOAT en un fichero binario
numero_float = 3.14159

with open('numeros.bin', 'wb') as f:
    f.write(struct.pack('f', numero_float))

with open('numeros.bin', 'rb') as f:
    print(struct.unpack('f', f.read())[0])

#Guardar varios tipos de datos
valores=[42, 3.14159, -7.89, 100]
with open('valores.bin', 'wb') as f:
    f.write(struct.pack('i', valores[0]))
    f.write(struct.pack('f', valores[1]))
    f.write(struct.pack('f', valores[2]))
    f.write(struct.pack('i', valores[3]))
print("Valores guardados correctamente")
"""
Opcion abreviada:
f.write(struct.pack("iffi", valores[0], valores[1], valores[2], valores[3]))
"""

#Leer datos de un fichero binario y reconstruir valores

with open('valores.bin', 'rb') as f:
    valor_int1 = struct.unpack('i', f.read(4))[0]
    valor_float1 = struct.unpack('f', f.read(4))[0]
    valor_float2 = struct.unpack('f', f.read(4))[0]
    valor_int2 = struct.unpack('i', f.read(4))[0]

print(f"Valor int 1: {valor_int1}")
print(f"Valor float 1: {valor_float1}")
print(f"Valor float 2: {valor_float2}")
print(f"Valor int 2: {valor_int2}")

"""
Opción abreviada:
datos = f.read(struct.calcsize("iffi"))
valor_int1,valor_float1,valor_float2,valor_int2=struct.unpack("iffi", datos)
"""
