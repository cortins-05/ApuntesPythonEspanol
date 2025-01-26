# Una función es un bloque de código reutilizable que realiza una tarea específica. Piensa en ella como una "mini-programa".

# Puntos importantes sobre las funciones:
#     1.Se definen con la palabra def
#     2.El nombre de la funcion debe ser descriptivo
#     3.Pueden tener 0 o más parámetros
#     4.Pueden retornar valores usando return
#     5.Si no hay un return retornan None

# Función básica sin parámetros
def saludar():
    print('Hola mundo')
saludar()

# Función con parámetros
def saludar1(nombre):
    print(f'Hola {nombre}')
saludar1('Lucas')

# Función que retorna un valor
def sumar(a,b):
    resultado = a+b
    return resultado
sumar(4,5)

# Función con múltiples parámetros y valor por defecto
def crear_perfil(nombre, edad, ciudad='No especificada'):
    return f'Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}'
perfil1 = crear_perfil('Ana', 25, 'Madrid')
perfil2 = crear_perfil('Pedro', 30)
print(perfil1)
print(perfil2)


"""TIPOS DE PARÁMETROS"""
# POSICIONALES (obligatorios)
def multiplicar(a,b):
    return a*b
print(multiplicar(5,8))

# Con valores por defecto
def saludar2(nombre, saludo='Aloha'):
    print(f'{saludo}, {nombre}')
saludar2('María')
saludar2('Pedro', 'Hola')

# Nombrados
def crear_usuario(nombre, edad, ciudad):
    print(f'Usuario: {nombre}, Edad: {edad} años, de {ciudad}')
crear_usuario(edad=25, ciudad='Madrid', nombre='Ana')

"""ALCANCE (SCOPE) DE LAS VARIABLES"""
# Variables locales
# Variables globales
mensaje = "Global"

def mi_funcion():
    mensaje_local = 'Local'
    print(mensaje_local)
    print(mensaje)
mi_funcion()
print(mensaje)
print(mensaje_local) #Error no existe fuera de la función