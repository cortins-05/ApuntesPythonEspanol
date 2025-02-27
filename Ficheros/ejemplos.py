#1. Fichero separados por espacios
with open("numeros.txt", "r") as archivo:
    for linea in archivo:
        numeros = linea.split()
        numeros = [int(num) for num in numeros]
        print(numeros)

print("\n\n")

#2. Leer un fichero separado por comas (CSV)
with open("numeros.csv", "r") as fichero:
    for linea in fichero:
        numeros = linea.split(",")
        numeros = [int(x) for x in numeros]
        print(numeros)
        
print("\n\n")

#3. Leer un fichero con numeros flotantes
with open("numeros_flotantes.txt", "r") as archivo:
    for linea in archivo:
        numeros = linea.split()
        numeros = [float(num) for num in numeros]
        print(numeros)
