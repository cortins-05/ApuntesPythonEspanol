#Atributos státicos en python
#Se define usando el decorador: @staticmethod

#  Características dun método estático:
#  1. Non recibe self nin cls: A diferenza dos métodos de instancia (def
#   metodo(self):) e dos métodos de clase (@classmethod def metodo(cls):),
#   un método estático non precisa ter nin a instancia (self) nin a clase (cls) como primeiro
#   argumento.
#  2. Accede só aos parámetros proporcionados: Un método estático só pode acceder a aquilo
#     que se lle pase como argumento. Non ten acceso directo aos atributos da clase ou das
#     instancias.
#  3. Pódese chamar desde a clase ou desde unha instancia: Un método estático pódese invocar
#     tanto desde a propia clase como desde unha instancia.

# Cando NON usar un método estático?
#  1. Cando precisas acceder ou modificar atributos da clase ou da instancia: Se o método
#     necesita interactuar cos atributos da clase ou cos da instancia, non debe ser estático. Neste
#     caso, un método de instancia ou de clase sería máis apropiado.
#  2. Cando a operación depende do estado da instancia ou da clase: Se a operación realiza
#     cambios ou consultas aos datos da clase ou da instancia, entón debe ser un método de
#     instancia ou de clase.

#EJEMPLO
import math

class Circulo:
    @staticmethod
    def calcular_area(radio):
        return math.pi * radio**2
    
    @staticmethod
    def calcular_perimetro(radio):
        return math.pi * 2 * radio

area = Circulo.calcular_area(5)
perimetro = Circulo.calcular_perimetro(5)
print(f"El area de un circulo de 5 de radio es {round(area,2)} y el perimetro de {round(perimetro,2)}")
