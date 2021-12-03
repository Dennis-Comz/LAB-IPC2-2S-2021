from tkinter import *
from Models.Nodes import *

class LineList:
    def __init__(self):
        self.first = None
    
    def append(self, noLinea, componentes, tiempo):
        newNode = LineNode(noLinea, componentes, tiempo)
        if self.first == None:
            self.first = newNode
        else:
            actual = self.first
            while actual.next != None:
                actual = actual.next
            actual.next = newNode

    def search(self, linea):
        temp = self.first
        while temp:
            if temp.noLinea == linea:
                return temp
            else:
                temp = temp.next
            if temp == None:
                return False
    
    def getSize(self):
        temp = self.first
        tamano = 0
        while temp:
            tamano += 1
            temp = temp.next
        return tamano

    def show(self):
        temp = self.first
        while temp:
            if temp != None:
                print('Linea: ' + str(temp.noLinea) + '; Componentes: ' + str(temp.noComponentes) + '; Tiempo: ' + str(temp.tiempo))
            temp = temp.next

class ProductList:
    def __init__(self):
        self.first = None
    
    def append(self, nombre, instrucciones):
        newNode = ProductNode(nombre, instrucciones)
        if self.first == None:
            self.first = newNode
        else:
            actual = self.first
            while actual.next != None:
                actual = actual.next
            actual.next = newNode
    
    def getProducts(self):
        temp = self.first
        nombres = ''
        while temp:
            if temp != None:
                nombres += temp.nombre + '\n'
            temp = temp.next
        return nombres

    def search(self, name):
        temp = self.first
        self.nombre = name
        while temp:
            if temp.nombre == name:
                return True
            else:
                temp = temp.next
            if temp == None:
                return False

    def getPasos(self):
        temp = self.first
        while temp:
            if temp.nombre == self.nombre:
                return temp.pasos
            else:
                temp = temp.next
        
    def show(self):
        temp = self.first
        while temp:
            if temp != None:
                print('Nombre: ' + temp.nombre + '; Instrucciones: ' + temp.pasos)
            temp = temp.next

class SimulationList:
    def __init__(self):
        self.first = None

    def append(self, nombre, listaElaborar):
        newNode = SimulationNode(nombre, listaElaborar)
        if self.first == None:
            self.first = newNode
        else:
            actual = self.first
            while actual.next != None:
                actual = actual.next
            actual.next = newNode
    
    def show(self):
        temp = self.first
        while temp != None:
            if temp.listaElaborar.show() != None:
                print(' Simulacion: ' + temp.nombre + 'Productos a Elaborar: ' + temp.listaElaborar.show())
                temp = temp.next
            else:
                break

class DevelopList:
    def __init__(self):
        self.first = None
    
    def append(self, nombre):
        newNode = DevelopNode(nombre)
        if self.first == None:
            self.first = newNode
        else:
            actual = self.first
            while actual.next != None:
                actual = actual.next
            actual.next = newNode

    def show(self):
        temp = self.first
        while temp != None:
            print('\n Producto: ' + temp.nombre)
            temp = temp.next

class instructionList:

    def __init__(self):
        self.first = None

    def append(self, noLinea, noComponente):
        newNode = instNode(noLinea, noComponente)
        if self.first == None:
            self.first = newNode
        else:
            actual = self.first
            while actual.next != None:
                actual = actual.next
            actual.next = newNode
    
    def show(self):
        temp = self.first
        while temp != None:
            print('Linea: ' + temp.noLinea + '; Componente: ' + temp.noComponente)
            temp = temp.next

    def setLabel(self, root):
        temp = self.first
        self.var = '\nPasos Para Elaborar Producto:\n'
        while temp != None:
            self.var += 'Linea: ' + str(temp.noLinea) + '; Componente: ' + str(temp.noComponente) + '\n'
            temp = temp.next
        self.label = Label(root, text=self.var, font= ('Verdana', 12), height=10, bg='grey').place(x=70, y=170)

class OperationList:
    def __init__(self):
        self.first = None

    def append(self, segundo, linea, componente, ensamblar, mover):
        newNode = OperationNode(segundo, linea, componente, ensamblar, mover)
        if self.first == None:
            self.first = newNode
        else:
            actual = self.first
            while actual.next != None:
                actual = actual.next
            actual.next = newNode
    
    def is_ensamblando(self, segundo):
        temp = self.first
        while temp:
            if temp != None:
                if temp.segundo == segundo and temp.ensamblar == True:
                        return True
            temp = temp.next
        return False
    def alreadyMove(self, linea, segundo):
        temp = self.first
        while temp:
            if temp != None:
                if temp.linea == linea and temp.segundo == segundo and temp.mover == True:
                    return True
                else:
                    return False
            temp = temp.next

    def is_Empty(self):
        if self.first == None:
            return True
        else:
            return False

    def getSize(self):
        temp = self.first
        tamano = 0
        while temp:
            tamano += 1
            temp = temp.next
        return tamano

    def getMayor(self):
        temp = self.first 
        mayor = 0
        while temp:
            if temp.next != None:
                if temp.linea > temp.next.linea:
                    mayor = temp.linea
                    temp = temp.next
            temp = temp.next
        return mayor

    def getTiempoTotal(self):
        temp = self.first 
        mayor = 0
        while temp:
            if temp.next != None:
                if temp.segundo < temp.next.segundo:
                    mayor = temp.next.segundo
                    temp = temp.next
            temp = temp.next
        return mayor


    def delete_duplicates(self):        
        current = self.first
        while current:
            runner = current
            while runner.next:
                if current.linea == runner.next.linea and current.componente == runner.next.componente and current.segundo == runner.next.segundo:
                    runner.next = runner.next.next
                elif current.linea == runner.next.linea and current.segundo == runner.next.segundo:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next

    def printList(self):
        temp = self.first
        while temp:
            print('Segundo: ' + str(temp.segundo) + '; Linea: ' + str(temp.linea) + '; Componente: ' + str(temp.componente) + '; Ensamblar: ' + str(temp.ensamblar) + '; Mover: ' + str(temp.mover))
            temp = temp.next

class GenerateList:
    def __init__(self):
        self.first = None
    
    def append(self, nombre, listaPasos):
        newNode = GenerateNode(nombre, listaPasos)
        if self.first == None:
            self.first = newNode
        else:
            actual = self.first
            while actual.next != None:
                actual = actual.next
            actual.next = newNode