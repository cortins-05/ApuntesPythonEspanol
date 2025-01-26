# Las tuplas son similares a las listas, pero son inmutables, es decir, una vez creadas, no puedes modificar sus elementos. Se definen con paréntesis ().

punto = (0,10)
ejemplo_tupla_1_elemento = (40,) #Se necesita de coma

# Acceso a elementos
print(punto[1])

#Metodos comunes
print(punto.count(0)) #Devuelve el numero de veces que el valor 0 aparece en la tupla
print(punto.index(10)) #Devuelve el indice del primer elemento cuyo valor sea 10

#Funciones comunes
print(len(punto))
print(max(punto))
print(min(punto))
print(sum(punto))

