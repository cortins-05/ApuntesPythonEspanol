"""

Clases: Unha clase é un molde ou plantilla que define propiedades (atributos) e comportamentos
(métodos) para os obxetos creados a partir dela. É un concepto fundamental na programación
orientada a obxetos (OOP).
Obxetos: Un obxeto é unha instancia dunha clase. Cando creamos un obxeto dunha clase,
asignamos valores reais aos atributos e podemos usar os métodos definidos na clase.

"""

#EJEMPLO

class Perro:
    #Constructor (inicializa el objeto)
    def __init__(self, nombre ,raza, edad):
        #Atributos del perro
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        
    #Método para ladrar
    def ladrar(self):
        print(f'{self.nombre} está ladrando: Au Au!')
        
    #Método para describir el perro
    def presentar(self):
        print(f'Hola, soy un {self.raza} llamado {self.nombre}. Tengo {self.edad} años.')
        

#Creando objetos (instancias de la clase perro)
rex = Perro("Rex", "Pastor Alemán", 5)
bob = Perro("Bob", "Cruzado", 3)

#Usando los métodos de los objetos
rex.ladrar()
bob.presentar()


"""

CONCEPTOS CLAVE:

1.Clase
    Se define usando la palabra class
    Funciona como modelo para crear objetos
    Define atributos (características) y métodos (comportamientos)

2.Metodo __init__
    Método especial llamado constructor
    Inicializa los atributos cuando se crea un objeto
    self se refiere a la propia instancia de un objeto

3.Atributos
    Características del objeto 
    En el ejemplo nombre, raza, edad son atributos
    Cada objeto puede tener valores diferentes para esos atributos

4.Métodos
    Funciones que definen los comportamientos de la clase
    En el ejemplo ladrar() y presentar() son métodos
    Pueden acceder y manipular los atributos del objeto
    
5.Creando objetos
    Cada objeto (rex y bob) es una instancia única de la clase Perro
    Tiene sus propios valores de atributos
    Puede llamar a los métodos definidos en la clase


BENEFICIOS DE LA POO:
    Organicación de código
    Reutilización de código
    Modelaje más óptima de la realidad
    Encapsulamiento de datos y comportamientos

"""