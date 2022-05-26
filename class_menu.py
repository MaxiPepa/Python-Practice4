from class_connection import *
from class_perro import *

class Menu:

    def ingresar_perro(self):
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

    def ingresar_perro(self):
        nombre = input("Ingrese el nombre del perro: ")
        

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
                self.ingresar_perro()
            elif opcion == 2:
                pass
            elif opcion == 3:
                pass
            elif opcion == 4:
                pass
            elif opcion == 5:
                pass
            elif opcion == 0:
                print("Hasta Pronto")
                loop = False