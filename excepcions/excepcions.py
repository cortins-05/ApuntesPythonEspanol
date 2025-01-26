""" 
try: Intentamos ejecutar el bloque de código dentro de try.
except: Si ocurre una excepción (error), el flujo del programa pasa al bloque except. En este caso, si se produce una ZeroDivisionError, mostramos un mensaje de error.
else: Si no ocurre ningún error en el bloque try, se ejecuta el bloque else.
finally: Este bloque se ejecuta siempre, haya ocurrido un error o no, y es útil para liberar recursos, cerrar archivos, etc.
"""

#EJEMPLO con un except especifico

def dividir(a,b):
    try:
        resultado = a/b
    except ZeroDivisionError:
        print("Error: No se puede dividir entre 0")
    else:
        print(f"El resultado de la division es {resultado}")
    finally:
        print("La operacion de división ha terminado")

dividir(10,0)
dividir(10,2)


#EJEMPLO con un except genérico

try:
    x= int(input("Ingresa un numero: "))
    result= 10/x
except Exception as e:
    print(f"Ocurrio el error {e}")