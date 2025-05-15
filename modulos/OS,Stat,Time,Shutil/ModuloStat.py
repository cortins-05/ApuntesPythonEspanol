"""
El módulo stat permite trabajar con los metadatos de los ficheros, como los permisos, la fecha de modificación y otros atributos.
Sus constantes principales están orientadas a obtener información detallada de un fichero.

FUNCIONES PRINCIPALES:
- stat(); obtiene información del fichero como un objeto stat que contiene varios atributos
- S_IRUSR, S_IWUSR, S_IXUSR; constantes que se usan para comprobar y cambiar permisos de ficheros

"""

#EJEMPLO PRÁCTICO:
import os
import stat

file_path = "ejemplo.txt"
stat_info = os.stat(file_path)

permissions = stat_info.st_mode
if permissions & stat.S_IRUSR:
    print("El fichero tiene permisos de lectura para el dueño")
else:
    print("El fichero no tiene permisos de lectura para el dueño")

"""
stat_info.st_mode -> proporciona información sobre permisos de un fichero
stat.S_IRUSR -> indica si el dueño tiene permisos de lectura
"""