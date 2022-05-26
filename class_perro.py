from class_connection import *

class Perro:
    def __init__(self, nombre, dueno, domicilio, telefono, bano, corte):
        self.nombre = str(nombre)
        self.dueno = str(dueno)
        self.domicilio = str(domicilio)
        self.telefono = int(telefono)
        self.bano = int(bano)
        self.corte = int(corte)

    def add_perro(self):
        conexion = Connection()
        conexion.open_connection()
        conexion.cursor.execute("INSERT INTO PERROS VALUES(NULL, '{}', '{}', '{}', '{}', '{}', '{}')".format(self.nombre, self.dueno, self.domicilio, self.telefono, self.bano, self.corte))
        conexion.connection.commit()
        conexion.close_connection()