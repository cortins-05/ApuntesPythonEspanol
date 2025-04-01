"""
Primero necesitarás instalar la librería:

pip install mysql-connector-python

"""

#Conectar a MySQL

import mysql.connector

try:
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "ejemplo"
    )
except:
    print("Conexion fallida con la DB")