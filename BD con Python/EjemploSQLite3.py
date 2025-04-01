import sqlite3

#Conectar o crear la base de datos
conn = sqlite3.connect("ejemplo.db")
cursor = conn.cursor()

#Crear una tabla si no existe
cursor.execute('''
CREATE TABLE IF NOT EXISTS personas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    edad INTEGER NOT NULL
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
conn.commit()
conn.close()