"""
Primero necesitarás instalar la librería:

pip install mysql-connector-python

"""

#Conectar a MySQL
import mysql.connector
cnx = mysql.connector.connect(
    host='localhost',       # El servidor MySQL en XAMPP
    user='root',            # El usuario de MySQL
    password='',           # La contraseña del usuario (por defecto está vacía)
    database='ejemplo'     # El nombre de la base de datos
)
cursor = cnx.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS ejemplo")

#Crear una tabla en MySQL
cursor.execute('''
CREATE TABLE IF NOT EXISTS personas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    edad INT NOT NULL
)
''')

#Insertar datos en la tabla
cursor.execute("INSERT INTO personas (nombre, edad) VALUES ('Ana', 30)")
cursor.execute("INSERT INTO personas (nombre, edad) VALUES ('Carlos', 25)")
cursor.execute("INSERT INTO personas (nombre, edad) VALUES ('Marta', 28)")

#Consultar datos
cursor.execute("SELECT * FROM personas")
resultados = cursor.fetchall()

for registro in resultados:
    print(f"ID: {registro[0]}, Nombre: {registro[1]}, Edad: {registro[2]}")
    
#Actualizar datos
cursor.execute("UPDATE personas SET edad = 26 WHERE nombre = 'Carlos'")

#Eliminar datos
cursor.execute("DELETE FROM personas WHERE nombre = 'Marta'")

#Cerrar la conexion
cnx.commit()
cnx.close()
