"""
ODBC es una especificación desarrollada por Microsoft en los años 90 para que diferentes aplicaciones puedan acceder a datos almacenados en distintos sistemas de gestión de bases
de datos sin tener que escribir código específico en distintos sistemas de gestión de datos (SGBD)

ODBC actúa como intermediario entre las aplicaciones y los SGBD. Usando un conector ODBC, una aplicación puede realizar consultas SQL y recibir los resultados sin preocuparse
de cual es el sistema de base de datos subyacente

CÓMO FUNCIONA UN CONECTOR ODBC?
Funciona en varias capas:
1. Aplicación; hace llamadas al ODBC para interactuar con los datos
2. Driver ODBC; este driver es el responsable de traducir las llamadas ODBC en comandos específicos para el sistema de base de datos de destino
3. Gestor de ODBC; es un programa que gestiona conexiones ODBC
4. Base de datos; el driver ODBC traducirá las solicitudes SQL de aplicación para que el sistema de base de datos pueda procesarlas

ESTRUCTURA DE UNA CONEXIÓN ODBC:
Para conectarse a una BD usandolo, normalmente se define una cadena de conexión que especifica todos los detalles necesarios para que el conector ODBC pueda establecer la conexión.
Esta cadena incluye parámetros como:
 - Driver; el controlador que se usará
 - Server; la dirección del servidor donde estará alojada la bd
 - Database; el nombre de la BD que se desea acceder
 - User ID y Password; el usuario y contraseña para efectuar la conexión

INSTALAR ODBC DRIVER PARA SQL SERVER:
1. Descargar ODBC Driver 17 para SQL Server
2. Instalar el driver
"""

#MANEJO:
#Conexión a SQL Server y creación de una tabla:
import pyodbc

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'
    'DATABASE=nombre_base_de_datos;'
    'UID=usuario;'
    'PWD=contraseña')

cursor = conn.cursor()

cursor.execute('''
Create table if not exits usuarios(
    id int primary key,
    nom varchar(50),
    edad int
)               
''')

conn.commit()

cursor.execute('select * from usuarios')
for row in cursor:
    print(f"ID:{row.id}\nNombre:{row.nom}\nEdad:{row.edad}")

conn.close()
