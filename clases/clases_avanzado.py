#1. Clase -> Es un objeto o molde que define las propiedades de atributos y metodos de un objeto
#EJEMPLO
class Coche:
    #Atributos o propiedades (caracteristicas del coche)
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
    
    #Metodo (accion)
    def enseñar_informacion(self):
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nColor: {self.color}")

#2. Subclase y herencia -> La herencia permite que una clase (subclase) herede los atributos y metodos de otra clase (superclase). La subclase puede modificar los atributos y metodos de la superclase
#EJEMPLO subclase que hereda de coche
class CocheElectrico(Coche):
    def __init__(self, marca, modelo, color, autonomia):
        super().__init__(marca, modelo, color)
        self.autonomia = autonomia
    
    def enseñar_informacion(self):
        super().enseñar_informacion()
        print(f"Autonomia: {self.autonomia}")


"""
Super() en Python:
El uso de super() permite llamar a métodos o constructores de la clase padre (la clase donde hereda la subclase). Esto es útil para que el código sea más flexible y menos susceptible a errores.

Como funciona super():
1. Llamar a un método de la clase padre -> super().metodo()
2. Uso de constructores -> super().__init__()        
"""



#3.E Encapsulamiento -> Se refiere a ocultar la implementación interna de un objeto y ofrecer una interfaz pública para interactuar con él. Se consigue con métodos privados.
#EJEMPLO
class Coche1:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.__modelo = modelo #Atributo privado
    
    def obtener_modelo(self):
        return self.__modelo  #Método público
    



#4. Polimorfismo -> Permite que una clase tenga métodos con el mismo nombre pero con diferente implementación	
#Se puede lograr de dos formas: A través de herencia o a través de polimorfismo de sobrecarga
#EJEMPLO
class Coche3:
    def sonido(self):
        print("Biim Biim")

class Moto:
    def sonido(self):
        print("Brrr Brrr")

def haz_sonar(vehiculo):
    vehiculo.sonido()

coche = Coche3()
moto = Moto()

haz_sonar(coche)
haz_sonar(moto)



#5. Clases abstractas -> Son clases que no se pueden instanciar y que se utilizan como base para otras clases. Se pueden crear con el módulo abc
"""
Para que sirven las clases abstractas:
Son útiles cuando queremos asegurarnos de que ciertas clases tienen una interfaz común, sin preocuparnos por la implementación de los métodos.

Como se usan:
Usamos ABC para definir la clase abstracta y @abstractmethod para definir los métodos abstractos.
"""
#EJEMPLO
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def hablar(self):
        pass
    
    @abstractmethod
    def moverse(self):
        pass

class Perro(Animal):
    def hablar(self):
        print("El perro ladra")
    
    def moverse(self):
        print("El perro corre")

class Gato(Animal):
    def hablar(self):
        print("El gato maulla")
    
    def moverse(self):
        print("El gato salta")
        
#Esto fallara al crear instancias de clases abstractas
#animal = Animal()

#Pero las subsclases si se pueden instanciar
perro = Perro()
gato = Gato()

perro.hablar()
perro.moverse()

gato.hablar()
gato.moverse()