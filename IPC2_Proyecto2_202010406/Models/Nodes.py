class LineNode:
    def __init__(self, noLinea, noComponentes, tiempo):
        self.noLinea = noLinea
        self.noComponentes = noComponentes
        self.tiempo = tiempo
        self.next = None

class ProductNode:
    def __init__(self, nombre, pasos):
        self.nombre = nombre
        self.pasos = pasos
        self.next = None

class SimulationNode:
    def __init__(self, nombre, listaElaborar):
        self.nombre = nombre
        self.listaElaborar = listaElaborar
        self.next = None

class DevelopNode:
    def __init__(self, nombre):
        self.nombre = nombre
        self.next = None

class instNode:
    def __init__(self, noLinea, noComponente):
        self.noLinea = noLinea
        self.noComponente = noComponente
        self.next = None

class OperationNode:
    def __init__(self, segundo, linea, componente, ensamblar, mover):
        self.segundo = segundo
        self.linea = linea
        self.componente = componente
        self.ensamblar = ensamblar
        self.mover = mover
        self.next = None

class GenerateNode:
    def __init__(self, nombre, listaPasos):
        self.nombre = nombre
        self.listaPasos = listaPasos
        self.next = None