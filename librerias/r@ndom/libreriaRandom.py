#La librería random en Python se utiliza para generar números pseudoaleatorios. Proporciona una variedad de funciones para diferentes casos de uso. Aquí tienes un desglose con ejemplos:
import random

#Generación básica de números aleatorios

print(random.random()) #Genera un num aleatorio entre 0.0 (incluido) a 1.0 (excluido)

print(random.uniform(10,20)) #Genera un numero float entre 10(incluido) a 20 (incluido)

print(random.randint(10,20)) #Genera un numero entero entre 10(incluido) a 20(incluido)

#RANDOM RANDRANGE
print(random.randrange(10)) #Genera un numero aleatorio entre 0 y 9
print(random.randrange(2,21,2)) #Genera un numero entero entre 2(incluido) a 21(excluido) con paso 2(en este caso)

#Con secuencias (listas)
lista_ejemplo = ["manzana", "platano", "pera"]
print(f"Elección aleatoria {random.choice(lista_ejemplo)}") #Devuelve un elemento aleatorio de la lista

print(random.choices(lista_ejemplo, k=5, weights=[1,2,1])) #Devuelve una lista de k elementos sobre la lista enviada donde se repiten algunos de forma aleatoria, tambien le puedes indicar un peso (opcional) donde indicas cual aparece con mayor frecuencia

random.shuffle(lista_ejemplo)#Modifica la lista original cambiando el orden de la misma
print(lista_ejemplo) 

print(random.sample(lista_ejemplo, 2)) #Devuelve una lista de k elementos UNICOS sobre la lista original


#SEMILLA (con los resultados te deberías hacer una idea de para que sirve)
random.seed(42)
print(random.random())
print(f"Numero aleatorio entre 0 y 9 con la semilla 42: {random.randint(1,10)}")

random.seed(42)
print(random.random())
print(f"Numero aleatorio entre 0 y 9 con la semilla 42: {random.randint(1,10)}")
