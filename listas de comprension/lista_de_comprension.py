""" Las list comprehensions son una forma concisa y eficiente de crear listas en Python. Permiten crear nuevas listas aplicando una expresión a
cada elemento de una secuencia (como un rango, lista o tupla). """
#Ejemplo basico
cuadrados_1_al_10=[x**2 for x in range(1,11)]
print(cuadrados_1_al_10)
#La sintaxis general es: [expresión for elemento in iterable].


#Ejemplo con condicion
cuadrados_pares=[x**2 for x in range(1,11) if x % 2 == 0]
print(cuadrados_pares)
#Agregamos un if dentro de la lista de comprension para filtrar los elementos del rango y quedarnos solo con numeros pares