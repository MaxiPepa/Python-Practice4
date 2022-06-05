from tracemalloc import start
from class_connection import *
from class_perro import *

class Menu:

    def insert_perro(self):
        nombre = input("Ingrese nombre del perro: ")
        dueno = input("Ingrese nombre del dueño: ")
        domicilio = input("Ingrese domicilio: ")

        telefono = int(input("ingrese teléfono: "))
        while type(telefono) != int:
            telefono = int(input("El teléfono debe ser un número, ingrese de nuevo: "))

        opcion_visita = int(input("Ingrese 1 si vino por baño, 2 si vino por corte o 3 si vino por ambos: "))
        while opcion_visita < 1 or opcion_visita > 3:
            opcion_visita = int(input("Ingrese una opción válida: "))

        if opcion_visita == 1:
            bano = 1
            corte = 0
        elif opcion_visita == 2:
            corte = 1
            bano = 0
        else:
            bano = 1
            corte = 1

        nuevo_perro = Perro(nombre, dueno, domicilio, telefono, bano, corte)
        nuevo_perro.add_perro()

    def modify_perro(self):
        nombre = input("Ingrese el nompre del perro: ")
        opcion = int(input("Ingrese 1 si quiere cambioar el domicilio o 2 si quiere cambiar el teléfono: "))
        while opcion < 1 or opcion > 2:
            opcion = int(input("Ingrese una opción válida: "))

        if opcion == 1:
            domicilio = input("Ingrese el nuevo domicilio: ")
            Perro.modify_domicilio(domicilio, nombre)
        else:
            telefono = int(input("ingrese el nuevo teléfono: "))
            while type(telefono) != int:
                telefono = int(input("El teléfono debe ser un número, ingrese de nuevo: "))
            Perro.modify_telefono(telefono, nombre)

    def delete_perro(self):
        nombre = input("Ingrese el nompre del perro: ")
        chequeo = int(input("Ingrese 1 si esta seguro que quiere borrar, de lo contrario ingrese 2: "))
        while chequeo < 1 or chequeo > 2:
            chequeo = int(input("Ingrese una opción válida: "))
        
        if chequeo == 1:
            Perro.delete_perro(nombre)
        else:
            return
    
    def add_visit(self):
        nombre = input("Ingrese el nompre del perro: ")
        opcion_visita = int(input("Ingrese 1 si vino por baño, 2 si vino por corte o 3 si vino por ambos: "))
        while opcion_visita < 1 or opcion_visita > 3:
            opcion_visita = int(input("Ingrese una opción válida: "))

        if opcion_visita == 1:
            bano = 1
            corte = 0
        elif opcion_visita == 2:
            corte = 1
            bano = 0
        else:
            bano = 1
            corte = 1

        Perro.add_visit(nombre, bano, corte)
    def show_table(self):
        table = Perro.return_table()
        print("ID ------ NOMBRE ------ DUEÑO ------ DOMICILIO ------ TELÉFONO ------ BAÑOS ------ CORTES")
        for datos in table:
            print(str(datos[0]) + " ------ " + str(datos[1]) + " ------ " + str(datos[2]) + " ------ " + str(datos[3]) + " ------ " + str(datos[4]) + " ------ " + str(datos[5]) + " ------ " + str(datos[6]))

    def menu(self):
        loop = True
        while loop:
            opcion = int()
            print("<-- Menú de opciones de la peluquería -->")
            print("1- Añadir perro")
            print("2- Modificar perro")
            print("3- Eliminar perro")
            print("4- Cargar visita")
            print("5- Listado de perros")
            print("0- Salir del menú")
            opcion = int(input("Elija la opción: "))
            if opcion == 1:
                self.insert_perro()
            elif opcion == 2:
                self.modify_perro()
            elif opcion == 3:
                self.delete_perro()
            elif opcion == 4:
                self.add_visit()
            elif opcion == 5:
                self.show_table()
            elif opcion == 0:
                print("Hasta Pronto")
                loop = False