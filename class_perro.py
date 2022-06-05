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

    @classmethod
    def modify_domicilio(self,new_domicilio, nombre):
        conexion = Connection()
        conexion.open_connection()
        conexion.cursor.execute("UPDATE PERROS SET DOMICILIO='{}' WHERE NOMBRE_PERRO='{}'".format(new_domicilio, nombre))
        conexion.connection.commit()
        conexion.close_connection()

    @classmethod
    def modify_telefono(self,new_telefono, nombre):
        conexion = Connection()
        conexion.open_connection()
        conexion.cursor.execute("UPDATE PERROS SET TELEFONO='{}' WHERE NOMBRE_PERRO='{}'".format(new_telefono, nombre))
        conexion.connection.commit()
        conexion.close_connection()

    @classmethod
    def delete_perro(self, nombre):
        conexion = Connection()
        conexion.open_connection()
        conexion.cursor.execute("DELETE FROM PERROS WHERE NOMBRE_PERRO='{}'".format(nombre))
        conexion.connection.commit()
        conexion.close_connection()

    @classmethod
    def add_visit(self, nombre, bano, corte):
        conexion = Connection()
        conexion.open_connection()
        conexion.cursor.execute("UPDATE PERROS SET BAÑO = BAÑO + {} WHERE NOMBRE_PERRO='{}'".format(bano, nombre))
        conexion.cursor.execute("UPDATE PERROS SET CORTE = CORTE + {} WHERE NOMBRE_PERRO='{}'".format(corte, nombre))
        conexion.connection.commit()
        conexion.close_connection()

    @classmethod
    def return_table(self):
        conexion = Connection()
        conexion.open_connection()
        conexion.cursor.execute("SELECT * FROM PERROS")
        table = conexion.cursor.fetchall()
        conexion.close_connection()
        return table