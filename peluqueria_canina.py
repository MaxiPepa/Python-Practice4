"""
Desarrollar un sistema que integre una base de datos con SQLite para una peluquería canina. 
Mediante un menú de opciones llevar a cabo las siguientes posibilidades. 
1- Cargar Perros. 
De cada perro almacenar nombre, nombre del dueño, domicilio, teléfono. Cada perro puede ir a la peluquería por baño, o por baño y corte. Por esto mismo almacenar estas dos variables enteras y medida que el perro vaya por estos motivos aumentarlas en 1. El nombre del perro declararlo como Único e irrepetible. Llevar también a cabo un id como primary key autoincremental. 
2- Modificar datos de un perro. 
Dado el nombre de un perro dar la posibilidad de modificar domicilio o teléfono. 
3- Borrar un perro. 
Dado un nombre de un perro eliminarlo de la base de datos. 
4- Cargar visita. 
Leer el motivo por el que vino el perro (Baño o baño y corte) y aumentar en uno la/s variable/s indicadas. 
5- Listado de Perros. 
Mostrar ordenadamente todos los perros cargados.
0- Salir del menú. 

Punto adicional: usar la estructura de manejo de errores de python para que los datos ingresados sean correctos.
"""
from class_menu import *

program = Menu()
program.menu()

"""
import sqlite3

connection = sqlite3.connect("peluqueria")

cursor = connection.cursor()

cursor.execute(
    '''CREATE TABLE PERROS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE_PERRO VARCHAR (50) UNIQUE,
        NOMBRE_DUEÑO VARCHAR (50),
        DOMICILIO VARCHAR (50),
        TELEFONO INTEGER,
        BAÑO INTEGER,
        CORTE INTEGER)
    '''
)


connection.commit()
connection.close()
"""