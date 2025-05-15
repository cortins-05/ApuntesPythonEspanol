"""
El módulo time proporciona varias funciones para trabajar con tiempo y fechas
Permite obtener el tiempo actual, convertir entre diferentes formatos de tiempo y medir la duracion de procesos

FUNCIONES PRINCIPALES:
- time.time(); devuelve el tiempo actual en segundos desde la época Unix
- time.ctime(); convierte el tiempo en segundos desde la época Unix en una representación legible
- time.sleep(); pausa la ejecución de un programa durante un número determinado de segundos
"""

#EJEMPLO PRÁCTICO:
import time

current_time = time.time()
print(f"El tiempo actual (en segundos desde la época Unix) es {current_time}")

human_readable_time = time.ctime(current_time)
print(f"Tiempo en formato legible: {human_readable_time}")

print("Esperando 2 segundos")
time.sleep(2)
print("Reanudando después de 2 segundos")

"""
- time.time() -> obtiene el tiempo en segundos de la época Unix
- time.ctime() -> convierte el tiempo en un formato legible
- time.sleep() -> pausa la ejecución de un programa
"""