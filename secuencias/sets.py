# Los conjuntos son colecciones desordenadas de elementos únicos. No permiten elementos duplicados y se definen con llaves {} o con la función set().

conjunto = {1,2,3,4,5}
conjunto2 = {6,7,8,9,10}
conjunto3 = {1,3,5}
lista = [1,1,2,3,4,4,5,6,7]

#Metodos comunes
conjunto.add(6)
print(conjunto)
conjunto.remove(6) #Arroja error si no existe
print(conjunto)
conjunto.discard(7) #Tambien elimina el elemento pero no arroja error si no existe
print(conjunto)
print(conjunto.union(conjunto2)) #Une dos conjuntos
print(conjunto.intersection(conjunto3)) #Devuelve la interseccion de dos conjuntos
print(conjunto.difference(conjunto2)) # Devuelve la diferencia de dos conjuntos

#Funciones comunes
print(len(conjunto))
print(set(lista)) #Convierte una lista u otra secuencia en un conjunto eliminando duplicados