import os
from CargarArchivo import Cargar
from ProcesarTerreno import Procesar
from EscribirArchivo import *
from Grafica import *

def menu():
    opcion = 0

    while opcion != 6:
        print("========== MENU PRINCIPAL ==========")
        print("| 1. Cargar Archivo                |")
        print("| 2. Procesar Archivo              |")
        print("| 3. Escribir Archivo Salida       |")
        print("| 4. Mostrar Datos del Estudiantes |")
        print("| 5. Generar Grafica               |")
        print("| 6. Salida                        |")
        print("====================================")
        print("Seleccione una opcion: ")
        opcion = elegirOpcion()

        if opcion == 1:
            print("Ingrese la ruta del archivo: ")
            ruta = input()
            cargarArchivo(ruta)
        elif opcion == 2:
            print("Ingrese el nombre del terreno: ")
            nombre = input()
            procesarArchivo(nombre)
        elif opcion == 3:
            print("Escribir una ruta especifica: ")
            path = input()
            escribirArchivo(path, nombre)
        elif opcion == 4:
            mostrarDatos()
        elif opcion == 5:
            print("Seleccione un terreno a realizar grafica: ")
            name = input()
            grafica(name)

def elegirOpcion():
    op = input()
    while op < '1' or op > '6':
        print("Ingrese una opcion valida")
        op = input()
    return int(op)

def cargarArchivo(path):
    if os.path.exists(path) == True:
        Cargar.leerArchivo(path)
    else:
        print("El archivo no existe")

def procesarArchivo(name):
    pr = Procesar()
    pr.procesarLista(name)
    # Procesar(name).procesarLista

def escribirArchivo(path, name):
    EscribirArchivo.escribir(path, name)

def grafica(name):
    Grafica(name)

def mostrarDatos():
    print("*****************************************************************")
    print("***************** === Datos Estudiante === **********************")
    print(" * Nombre: Dennis Mauricio Corado Muñóz")
    print(" * Carne: 202010406")
    print(" * Introduccion a la Programacion y Computacion 2 seccion A")
    print(" * Ingenieria en Ciencias y Sistemas")
    print(" * 4to Semeste")
    print("*****************************************************************\n")
    
if __name__ == "__main__":
    menu()