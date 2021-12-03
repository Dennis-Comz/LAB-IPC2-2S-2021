from tkinter import *
import xml.etree.cElementTree as ET
from Analizar import Analizador
from Models.LinkedLists import OperationList, GenerateList
from ColaSecuencia import Cola
from Reportes import Reporte
class EscribirArchivo:
    def __init__(self):
        self.Analizador = Analizador()
        self.reportes = Reporte()
        self.genListSm = GenerateList()
        self.genListInd = GenerateList()
        self.genSm = False
        self.genInd = False

        
    def movimientos(self, nombre, listaProductos, listaLineas):
        prMaquina = listaProductos
        cnLineas = listaLineas.getSize()
        self.tt = 0
        if prMaquina.search(nombre):
            self.listaOp = OperationList()
            i, tiempo = 1, 1
            self.Analizador.evaluarCadena(prMaquina.getPasos())
            pasos = self.Analizador.getLista()
            pasos = pasos.first
            while pasos:

                for j in range(1, cnLineas+1):
                        if j == pasos.noLinea:
                            valLinea = listaLineas.search(j)

                while i <= (pasos.noComponente + 1):

                    if i != pasos.noComponente + 1:
                        if self.listaOp.is_Empty() == False:
                            if self.listaOp.is_ensamblando(tiempo):
                                self.listaOp.append(tiempo, pasos.noLinea, i, False, False)
                                tiempo += valLinea.tiempo
                            else:
                                self.listaOp.append(tiempo, pasos.noLinea, i, False, True)
                                tiempo += valLinea.tiempo
                                i += 1
                        else:
                            self.listaOp.append(tiempo, pasos.noLinea, i, False, True)
                            tiempo += valLinea.tiempo
                            i += 1
                    else:
                        if self.listaOp.is_ensamblando(tiempo):
                            self.listaOp.append(tiempo, pasos.noLinea, i, False, False)
                            tiempo += valLinea.tiempo
                        else:
                            self.listaOp.append(tiempo, pasos.noLinea, pasos.noComponente, True, False)
                            tiempo += valLinea.tiempo
                            i += 1

                if self.tt < tiempo:
                    self.tt = tiempo -1               
                i, tiempo = 1,1
                pasos = pasos.next
            a = self.bubblesort(self.listaOp)
            sortedList = OperationList()
            while a:
                sortedList.append(a.segundo, a.linea, a.componente, a.ensamblar, a.mover)
                a = a.next

        return sortedList

    def escribirSimulacion(self, listaSimulacion, listaProductos, listaLineas):
        nomSimulacion = listaSimulacion.first.nombre
        prSimulacion = listaSimulacion.first.listaElaborar.first

        root = ET.Element('SalidaSimulacion')
        ET.SubElement(root, 'Nombre').text = nomSimulacion
        listado = ET.SubElement(root, 'ListadoProductos')
        producto = ET.SubElement(listado, 'Producto')
        while prSimulacion:
            listaOrdenada = self.movimientos(prSimulacion.nombre, listaProductos, listaLineas)
            listaOrdenada.delete_duplicates()
            listaOrdenada.delete_duplicates()
            # self.genListSm = GenerateList()
            self.genSm = True
            self.genInd = False
            self.genListSm.append(prSimulacion.nombre, listaOrdenada)

            ET.SubElement(producto, 'Nombre').text = prSimulacion.nombre
            ET.SubElement(producto, 'TiempoTotal').text = str(self.tt)
            optima = ET.SubElement(producto, 'ElaboracionOptima')
            temp = listaOrdenada.first
            prTiempo = temp.segundo
            tiempo = ET.SubElement(optima, 'Tiempo', NoSegundo=str(temp.segundo))
            while temp:
                if temp.next != None:
                    if temp.segundo != temp.next.segundo and temp.segundo != prTiempo:
                        tiempo = ET.SubElement(optima, 'Tiempo', NoSegundo=str(temp.segundo))
                    if temp.mover == True:
                        ET.SubElement(tiempo, 'LineaEnsamblaje', NoLinea=str(temp.linea)).text = 'Mover brazo - componente ' + str(temp.componente)
                    elif temp.ensamblar == True:
                        ET.SubElement(tiempo, 'LineaEnsamblaje', NoLinea=str(temp.linea)).text = 'Ensamblar - componente ' + str(temp.componente)
                    elif temp.mover == False and temp.ensamblar == False:
                        ET.SubElement(tiempo, 'LineaEnsamblaje', NoLinea=str(temp.linea)).text = 'No hacer nada'
                else:
                    tiempo = ET.SubElement(optima, 'Tiempo', NoSegundo=str(temp.segundo))
                    if temp.mover == True:
                        ET.SubElement(tiempo, 'LineaEnsamblaje', NoLinea=str(temp.linea)).text = 'Mover brazo - componente ' + str(temp.componente)
                    elif temp.ensamblar == True:
                        ET.SubElement(tiempo, 'LineaEnsamblaje', NoLinea=str(temp.linea)).text = 'Ensamblar - componente ' + str(temp.componente)
                    else:
                        ET.SubElement(tiempo, 'LineaEnsamblaje', NoLinea=str(temp.linea)).text = 'No hacer nada'
                temp = temp.next
            tree = ET.ElementTree(root)
            tree.write(nomSimulacion + '.xml')
            prSimulacion = prSimulacion.next
        # self.reportes.genReporte(genList)


    def escribirIndividual(self, nombre, listaProductos, listaLineas):
        #Obteniendo una lista con los pasos a realizar
        listaOrdenada = self.movimientos(nombre, listaProductos, listaLineas)
        listaOrdenada.delete_duplicates()
        listaOrdenada.delete_duplicates()
        listaOrdenada.printList()
        self.generateTable(listaOrdenada)

        #Guardando la lista ordenada con el producto para despues realizar html
        self.genSm = False
        self.genInd = True
        self.genListInd = GenerateList()
        self.genListInd.append(nombre, listaOrdenada)
        # self.reportes.genReporte(genList)
        
        #Generarando archivo xml del producto
        root = ET.Element('SalidaSimulacion')
        listado = ET.SubElement(root, 'ListadoProductos')
        producto = ET.SubElement(listado, 'Producto')
        ET.SubElement(producto, 'Nombre').text = nombre
        ET.SubElement(producto, 'TiempoTotal').text = str(self.tt)
        optima = ET.SubElement(producto, 'ElaboracionOptima')
        temp = listaOrdenada.first
        prTiempo = temp.segundo
        tiempo = ET.SubElement(optima, 'Tiempo', NoSegundo=str(temp.segundo))
        while temp:
            if temp.next != None:
                if temp.segundo == temp.next.segundo and temp.segundo != prTiempo:
                    tiempo = ET.SubElement(optima, 'Tiempo', NoSegundo=str(temp.segundo))
                if temp.mover == True:
                    ET.SubElement(tiempo, 'LineaEnsamblaje', NoLinea=str(temp.linea)).text = 'Mover brazo - componente ' + str(temp.componente)
                elif temp.ensamblar == True:
                    ET.SubElement(tiempo, 'LineaEnsamblaje', NoLinea=str(temp.linea)).text = 'Ensamblar - componente ' + str(temp.componente)
                elif temp.ensamblar == False and temp.mover == False:
                    ET.SubElement(tiempo, 'LineaEnsamblaje', NoLinea=str(temp.linea)).text = 'No hacer nada'
            else:
                tiempo = ET.SubElement(optima, 'Tiempo', NoSegundo=str(temp.segundo))
                if temp.mover == True:
                    ET.SubElement(tiempo, 'LineaEnsamblaje', NoLinea=str(temp.linea)).text = 'Mover brazo - componente ' + str(temp.componente)
                elif temp.ensamblar == True:
                    ET.SubElement(tiempo, 'LineaEnsamblaje', NoLinea=str(temp.linea)).text = 'Ensamblar - componente ' + str(temp.componente)
                else:
                    ET.SubElement(tiempo, 'LineaEnsamblaje', NoLinea=str(temp.linea)).text = 'No hacer nada'
            temp = temp.next
        tree = ET.ElementTree(root)
        tree.write(nombre + '.xml')
        
        #Obteniendo los pasos en forma de lista enlada
        if listaProductos.search(nombre):
            self.Analizador.evaluarCadena(listaProductos.getPasos())
            pasos = self.Analizador.getLista()
            cola = Cola()
            cola.setRoot(self.root)
            cola.graficar(pasos)

    def bubblesort(self, lista):
        sorted = None 
        current = lista.first
        while current != None:
            next = current.next  
            sorted = self.sortedInsert(sorted, current)
            current = next

        lista = sorted
        return lista

    def sortedInsert(self, nodoFirst, new_Node):
        current = None
        if nodoFirst == None or nodoFirst.segundo >= new_Node.segundo:
            new_Node.next = nodoFirst
            nodoFirst = new_Node
        else:
            current = nodoFirst
            while current.next != None and current.next.segundo < new_Node.segundo:
                current = current.next
            new_Node.next = current.next
            current.next = new_Node

        return nodoFirst
    
    def setRoot(self, root):
        self.root = root

    def generateTable(self, lista):
        first = lista.first

        y = 0
        for i in range(self.tt + 1):
            e = Entry(relief=GROOVE)
            e.grid(row=i, column=0, sticky=NSEW)
            if i == 0:
                e.insert(END, "Tiempo")
            else:
                e.insert(END, str(i) + " seg")
            e.place(x=550, y = 100 + y)
            e.config(state='disabled', width=7)
            y += 25

        x = 60
        for i in range(lista.getMayor()):
            e = Entry(relief=GROOVE)
            e.grid(row=i, column=0, sticky=NSEW)
            e.insert(END, "Linea " + str(i+1))
            e.place(x=550 + x, y = 100)
            e.config(state='disabled', width=10)
            x += 80
        