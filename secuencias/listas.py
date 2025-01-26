#Las listas son colecciones ordenadas y modificables (mutables), lo que significa que puedes cambiar sus elementos. Se definen con corchetes [].

lista_vacia = []
numeros = [1,2,3,4,5]
str = ['pepe', 'caballo', 'cola']

# Acceso a elementos
print(numeros[0])
# Modificar un elemento
numeros[2] = 10
print(numeros)



# Metodos comunes:
numeros.append(6) #Añadir un elemento
print(numeros)

numeros.remove(10) #Eliminar un elemento
print(numeros)

print(numeros.pop()) #Elimnina el ultimo elemento y lo devuelve/ Tambien puedes ponerle la posicion
print(numeros)

numeros.insert(0, 10) #Inserta el 10 en la posicion 0
print(numeros)

print(numeros.index(4)) #Devuelve la primera posicion donde aparece el 4

numeros.sort() #Ordena la lista
print(numeros)

numeros.reverse() #Invierte el orden de la lista
print(numeros)

# Funciones comunes:
print(len(numeros)) #Devuelve la longitud de la lista
print(sum(numeros)) #Devuelve la suma de los elementos de la lista (si es numerica)
print(max(numeros)) #Devuelve el numero maximo de la lista
print(min(numeros)) #Devuelve el valor minimo


#Enumerar la lista
print(enumerate(str))
