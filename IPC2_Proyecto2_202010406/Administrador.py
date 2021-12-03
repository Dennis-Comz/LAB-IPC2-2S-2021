import os
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from LeerArchivos import Reader
from Analizar import Analizador
from Escribir import EscribirArchivo
from Reportes import Reporte
from tkinter.filedialog import askopenfilename

class Administrador:
    def __init__(self):
        self.scanner = Reader()
        self.Analizador = Analizador()
        self.Escribir = EscribirArchivo()
        self.reportes = Reporte()
    
    def setRoot(self, root):
        self.root = root

    def configMaquina(self):
        filename = askopenfilename()
        if os.path.exists(filename) == True:
            self.scanner.setMaquina(filename)
            messagebox.showinfo('Exito', 'Maquina Configurada')
        else:
            messagebox.showerror('Error', 'El archivo no existe')

    
    def genSimulacion(self):
        filename = askopenfilename()
        if os.path.exists(filename) == True:
            self.scanner.setSimulacion(filename)
            self.Escribir.escribirSimulacion(self.scanner.listaSimulacion, self.scanner.listaProductos, self.scanner.listaLineas)
            messagebox.showinfo('Exito', 'Generando simulacion.')
        else:
            messagebox.showerror('Error', 'El archivo no existe')

    def datos(self):
        datos = '''Nombre: Dennis Mauricio Corado Muñóz\nCarne: 202010406\nIntroduccion a la Programacion y Computacion 2 seccion A\nIngenieria en Ciencias y Sistemas\n4to Semestre'''
        messagebox.showinfo('Datos del Estudiante', datos)
    
    def showValues(self):
        self.nombres = self.scanner.listaProductos.getProducts()
        messagebox.showinfo('Productos', self.nombres)

    def ensamblarPr(self, nombre):
        existe = self.scanner.listaProductos.search(nombre)
        if existe == True:
            pasos = self.scanner.listaProductos.getPasos()
            self.Analizador.evaluarCadena(pasos)
            self.Analizador.instructionList.setLabel(self.root)
            self.Escribir.setRoot(self.root)
            self.Escribir.escribirIndividual(nombre,self.scanner.listaProductos, self.scanner.listaLineas)
        else:
            messagebox.showerror('Error', 'El producto no se encuentra en la maquina')

    def reporte(self):
        if self.Escribir.genSm != False:
            self.reportes.genReporte(self.Escribir.genListSm)
        elif self.Escribir.genInd != False:
            self.reportes.genReporte(self.Escribir.genListInd)
