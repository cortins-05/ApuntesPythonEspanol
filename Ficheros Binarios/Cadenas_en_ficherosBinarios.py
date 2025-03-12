"""
1. Por que ficheros binarios para cadenas?
Ya que guardan los datos de manera más eficiente que los ficheros de texto. También ocupan menos espacio.

2. Cómo se guardan las cadenas de texto en ficheros binarios?
Las cadenas de texto son en realidad sequencias de caracteres. Cuando guardamos una cadena en un fichero binario, tenemos que codificar esa cadena en una secuencia de bytes
Posteriormente, cuando leemos la cadena, descodificamos los bytes en el nuevo texto

3. Usar el módulo struct para guardar los strings:
Usaremos el módulo struct. Struct permite empaquetar los datos en Python en formato binario y al contrario desenpaquetarlos. En este caso, para guardar cadenas
tenemos que tener en cuenta que necesitamos especificar la longitud fija para que struct sepa cuantos bytes debe reservar para cada cadena.
"""
#Ejemplo Práctico

import struct

nomes = ["Pedro", "María", "Xoán", "Ana"]

with open("nomes.bin", "wb") as f:
    for nome in nomes:
        datos = struct.pack("50s", nome.encode('utf-8'))
        f.write(datos)

with open("nomes.bin", "rb") as f:
    while True:
        datos = f.read(struct.calcsize("50s"))
        if not datos:
            break
        nome_bytes = struct.unpack("50s", datos)[0]
        nome = nome_bytes.decode('utf-8').strip('\x00')
        print(nome)