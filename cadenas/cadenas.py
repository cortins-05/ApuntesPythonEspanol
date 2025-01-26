#Las cadenas se pueden crear con comillas simples (' ') o dobles (" "), y también con comillas triples
#(''' ''' o """ """) para cadenas multilínea.

cadena1= 'hola'
cadena2 = "mundo"

cadena_multilinea = '''Este es 
un ejemplo de
cadena multilinea'''

#Acceso a los elementos de la cadena
cadena = "Hola Mundo"
print(cadena[0])
print(cadena[4])
print(cadena[-1])

print(cadena[1:4])
print(cadena[:4])
print(cadena[5:])
print(cadena[-5:])

#Metodos comunes en cadenas
print("Hola".lower())
print("Mundo".upper())

print("hola".capitalize())
print("el hombre y la mujer".title())

texto = " Hola Mundo "
print(texto.strip()) #Elimina ambos espacios de los extremos
print(texto.lstrip()) #Elimina el ultimo espacio
print(texto.rstrip()) #Elimina el primer espacio

print(texto.replace("Mundo", "Python")) #Reemplaza una cadena por otra

texto = "Hola Mundo Python"
lista_palabras = texto.split()
print(lista_palabras)

nuevo_texto = "-".join(lista_palabras)
print(nuevo_texto)

cadena = "Hola Mundo"
print(cadena.find("Mundo"))
print(cadena.find("Python")) #Devuelve -1 porque no existe

print(cadena.index("Mundo"))
try:
    print(cadena.index("Python")) #Lo mismo pero devuelve ValueError
except:
    print("Mira el codigo")

cadena="hola hola hola"
print(cadena.count("hola"))

cadena="Python es genial"
print(cadena.startswith("Python"))
print(cadena.endswith("genial"))

#Formateo de cadenas

nombre="Juan"
edad=25
print(f"Mi nombre es {nombre} y tengo {edad} años")
print("Mi nombre es {} y tengo {} años".format(nombre, edad))
print("Mi nombre es %s y tengo %d años"%(nombre, edad))

#Comprobacion de propiedades de la cadena
cadena="Hola123"
print(cadena.isalnum()) #Verifica si todos los caracteres son alfanumericos
print(cadena.isalpha()) #Verifica si todos los letras
print(cadena.isdigit()) #Verifica si son digitos
print(cadena.isspace()) #Verifica si son espacios

#Concatenacion y repeticion
cadena1 = "Hola"
cadena2 = "Mundo"

print(cadena1 + " " + cadena2)
print("Hola " * 3)

#Longitud de la cadena
cadena = "Hola Mundo"
print(len(cadena))

#Comprobacion de subcadenas
cadena = "Hola Mundo"
print("Hola" in cadena)
print("Python" in cadena)

#Cadenas son inmutables