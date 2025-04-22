"""
SQL Alchemy es una herramienta que permite trabajar con bases de datos sin escribir SQL directamente, si no usando clases de Python, que representan tablas de bases de datos.

VOCABULARIO FUNDAMENTAL:
- Engine -> La conexión con la base de datos.
- Base -> La clase base de la que heredan tus modelos (tablas).
- Modelo -> Una clase python que representa una tabla de base de datos.
- Session -> Una conversación con la base de datos. Aquí añades consultas, actualizas o eliminas datos.
- Commit -> Confirma los cambios hechos en la sesión y los añade en la BD.
- Query -> Una consulta para obtener datos.

TECNOLOGÍAS USADAS:
- Python
- SQLAlchemy ORM
- SQLite (no requiere instalación externa)

"""

#Ejemplo Practico Detallado Paso a Paso

"""
INSTALACIÓN:
pip install sqlalchemy

CREAR UN MODELO Y LA CONEXIÓN CON LA BASE DE DATOS:
"""
###########################################################################
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

#Declaramos una base para los modelos
Base = declarative_base()

#Creamos una conexión para la base de datos SQLite
engine = create_engine('sqlite:///libros.db', echo=False) #Crea libros.db, el argumento echo=True indica que SQLAlchemy debe imprimir toda la actividad del motor

#Creamos el canal para trabajar con la DB
Session = sessionmaker(bind=engine)
session = Session()

#Definimos el modelo Libro -> será una tabla de la BD
class Libro(Base):
    __tablename__ = 'Libros' #Nombre de la tabla de la base de datos
    
    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    autor = Column(String)
    año = Column(Integer)
    
    def __repr__(self):
        return f"<Libro(titulo='{self.titulo}',autor='{self.autor}',año='{self.año}')>"
###########################################################################
"""
ENTENDIENDO LA CLASE LIBRO(BASE):
Es un modelo ORM, es decir, una clase especial que representa una tabla en la base de datos, NO ES una clase cualquiera como se usan normalmente para guardar datos en memoria
Posee caracteristicas como:
- No vive solo en la memoria
- Tiene relacion con la base de datos
- Hereda de Base 
- Se usa para trabajar con SQLAlchemy
"""
###########################################################################
#Paso 3: Crear las tablas en la base de datos
Base.metadata.create_all(engine)

#Paso 4: Añadir libros a la base de datos
libro1 = Libro(titulo="El Principito", autor="Anton Super", año=1943)
libro2 = Libro(titulo="Memorias dun neno labrego", autor="Xose Neira Vilas", año=1961)

#Añadir varios Libros
session.add_all([libro1,libro2]) 

#Guardar los cambios
session.commit()

#Paso 5: Consultar libros
libros = session.query(Libro).all()
for l in libros:
    print(l)

#Tambien puedes buscar por autor
libros_gallegos = session.query(Libro).filter_by(autor="Xose Neira Vilas").all()

#Paso 6: Modificar un libro
libro = session.query(Libro).filter_by(titulo="El Principito").first()
libro.año = 1945 #Cambiamos el año
session.commit()

#Paso 7: Eliminar un libro
libro = session.query(Libro).filter_by(titulo="Memorias dun neno labrego").first()
session.delete(libro)
session.commit()
###########################################################################

#ELIMINACION DE DATOS

#1.Si quieres borrar todos los libros pero mantener la tabla libros:
session.query(Libro).delete()
session.commit()

#2. Si quieres borrar completamente la base de datos (tablas incluídas), puedes hacer:
Base.metadata.drop_all(engine)

#3. Si quieres borrar todo y crear una nueva estructura desde cero:
Base.metadata.drop_all(engine) 
Base.metadata.create_all(engine)

#4. Eliminar el fichero SQLite directamente:
import os
os.remove("libros.db")


