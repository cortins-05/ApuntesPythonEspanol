"""
Métodos get e set en POO:

- Método get: Su propósito es "obtener" o acceder al valor de un atributo privado
- Método set: Su propósito es "establecer" o modificar el valor de un atributo privado


ATRIBUTOS PRIVADOS:
ejemplo -> self.__nombre

"""

#Ejemplos Prácticos

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre #Atributo privado
        self.__edad = edad #Atributo privado
    
    #Método set para cambiar el nombre
    def set_nombre(self, nuevo_nombre):
        if (len(nuevo_nombre)>2):#Validación del nombre
            self.__nombre == nuevo_nombre
    
    def set_edad(self, nueva_edad):
        if nueva_edad >= 0:#Validación de la edad
            self.__edad = nueva_edad
    
    #Método get para acceder al nombre
    def get_nombre(self):
        return self.__nombre
    
    #Método get para acceder a la edad
    def get_edad(self):
        return self.__edad
    
persona1 = Persona("Ana", 30)
print(persona1.get_nombre())
print(persona1.get_edad())

persona1.set_nombre("Pepe")
persona1.set_edad(25)
print(persona1.get_nombre())
print(persona1.get_edad())

"""
Ventajas de usar get y set:
-Encapsulamiento: Permite ocultar los detalles de implementación de los atributos de la clase, haciendo que la manipulación de los datos sea más segura
-Validación: Puedes asegurarte de que los datos que se almacenan en los atributos cumplen ciertas condiciones o reglas de negocio
-Mejor control: Permiten mayor control sobre el acceso o modificación de los datos, evitando cambios inesperados o incorrectos en los atributos

"""

#Usando property() en para gestionar getters y setters

class Persona1:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if len(nuevo_nombre)>2:
            self.__nombre = nuevo_nombre
        else:
            print("Error de longitud")
        
    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad > 0:
            self.__edad = nueva_edad
        else:
            print("La edad no puede ser inferior o igual a 0")

persona2 = Persona1("Ana", 30)

print(persona2.nombre)
persona2.nombre = "Maria"
print(persona2.nombre)

persona2.edad = 40
print(persona2.edad)



"""
Métodos Mágicos:
Son los métodos que tienen un nombre especial, rodeados por dos guiones bajos.

EJEMPLOS:

1. __init__: El método constructor que se llama automáticamente al inializar una clase
2. __str__: Éste método es usado cuando intentas imprimir un objeto o cuando usas una función str(). Permite definir como se debe representar el objeto como una cadena de texto. Si imprimer el objeto saldra el método __str__.
3. __repr__: Destinado a dar una representación más formal o técnica del objeto.
4.__add__: Es llamado cuando usas el operador + para sumar 2 objetos. Lo puedes personalizar.
5.__eq__: Es usado cuando usas el operador == para comparar dos objetos.
6.__del__: Este método es llamado cuando el objeto está a punto de ser destruido o eliminado. Se puede usar para hacer limpiezas.
7.__len__: Suele usarse en clases que tengan colecciones de elementos para que pueda devolver el operador len()
"""
    
#1. Ya sabemos de sobra

#2.
class Coche:
    def __init__(self, marca, matricula):
        self.marca = marca
        self.matricula = matricula
    
    def __str__(self):
        return f'{self.marca} con matricula {self.matricula}'
    
    def __repr__(self):
        return f'Marca: {self.marca}, Matricula:{self.matricula} '

coche = Coche("Toyota", "12345B")
print(coche)

#3.Reutilizamos la clase anterior
print(repr(coche))

#4.
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, outro):
        return Punto(self.x + outro.x, self.y + outro.y)
    
punto1 = Punto(1,2)
punto2 = Punto(3,4)
punto3 = punto1 + punto2
print(punto3.x, punto3.y)

#5.
class Persona2:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __eq__(self, otro):
        return self.nombre == otro.nombre and self.edad == otro.edad
    
    def __del__(self):
        print(f"El objeto {self.nombre} esta a punto de borrarse")
    
    def __len__(self):
        return 2
    
persona1 = Persona2("Juan", 30)
persona2 = Persona2("Juan", 30)
print(persona1 == persona2)

#6.Reutalizamos la clase anterior
del persona1


#7.Reutilizamos la clase anterior
print(len(persona2))