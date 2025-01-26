# Los diccionarios son colecciones desordenadas de pares clave-valor. Son mutables y se definen con llaves {}, donde cada elemento tiene la forma clave: valor.

estudiante = {
    'nombre': 'Juan',
    'edad': 21,
    'carrera': 'ingenieria'
}

estudiante_añadido = {
    'coche': 'toyota'
}

# Acceso a su valor por clave
print(estudiante['edad'])

#Modificar un valor
estudiante['edad'] = 22
print(estudiante)

#Añadir un nuevo par-valor
estudiante['promedio']=8.9
print(estudiante)

#Eliminar un par clave-valor
del estudiante['carrera']
print(estudiante)

#Metodos comunes
print(estudiante.get('promedio')) #Es como acceso a un valor por clave
print(estudiante.keys()) #Devuelve todas las claves de un diccionario
print(estudiante.values()) #Devuelve todos los valores de un diccionario
print(estudiante.items()) #Devuelve una LISTA de pares clave-valor
print(estudiante.pop('edad')) #Elimina la clave y devuelve su valor
estudiante.update(estudiante_añadido) #Fusiona diccionarios
print(estudiante)

#Funciones comunes
print(len(estudiante)) #Devuelve la cantidad de pares clave-valor
