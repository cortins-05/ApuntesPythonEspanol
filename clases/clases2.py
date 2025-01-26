# Atributos de Instancia e de Clase en Python

# Atributos de Instancia: Os atributos de instancia son variables que pertencen a unha instancia
# específica dunha clase. Cada instancia da clase ten o seu propio conxunto de atributos de instancia,
# o que significa que poden ter valores diferentes en cada obxecto.

# Atributos de Clase: Os atributos de clase son variables que pertencen á clase en si e son
# compartidos por todas as instancias da clase. Isto significa que todas as instancias da clase teñen
# acceso ao mesmo valor do atributo de clase. Neste exemplo iva é un atributo de clase.

# EXEMPLO de atributos de clase
class Coche:
    total_coches = 0
    
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        Coche.total_coches += 1
    
coche1 = Coche("toyota", "corolla")
coche2 = Coche("honda", "civic")

print(Coche.total_coches)

# Métodos de Instancia
# Os métodos de instancia son os que teñen acceso ás variables de instancia e poden modificar o
# estado do obxecto. Para acceder ás variables de instancia dentro dos métodos, utilízase a palabra
# clave self.

#METODOS DE CLASE EJEMPLO

class Coche1:
    total_coches = 0
    
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        Coche1.total_coches += 1
    
    @classmethod
    def mostrar_total_coches(cls):
        print(f"El número total de coches es {cls.total_coches}")
    
coche1 = Coche1("toyota", "corolla")
coche2 = Coche1("honda", "civic")

Coche1.mostrar_total_coches()

# Visibilidad en Python

# 1. Publico (accesible desde cualquier parte del programa)

# 2. Protegido (se recomienda acceder solo desde la propia clase o subclases)

# 3. Privado (usa name manling para acceder)

class Ejemplo:
    
    def __init__(self, valor, valor_protegido, valor_privado):
        self.valor = valor
        self._valor1 = valor_protegido
        self.__valor2 = valor_privado
        
    def metodo_publico(self):
        print("Este método es público")
    
    def _metodo_protegido(self):
        print("Este es un método protegido")
        
    def __metodo_privado(self):
        print("Este es un metodo privado")
    
    def mostrar_valor(self):
        print(self.__valor2)
        
obx = Ejemplo(10, 10, 10)
print(obx.valor)
obx.metodo_publico()

print(obx._valor1)
obx._metodo_protegido()

# print(obx.__valor2) Error
# obx.__metodo_privado() Error
obx.mostrar_valor()