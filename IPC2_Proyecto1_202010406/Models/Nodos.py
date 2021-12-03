# Nodos Matriz Ortogonal y Lista Simple

class NodoMatriz:
    def __init__(self, fila, columna, valor):
        self.valor = valor
        self.fila = fila
        self.columna = columna
        self.derecha = None
        self.izquierda = None
        self.arriba = None
        self.abajo = None
        self.visitado = False
        self.gasto = 0

class NodoEncabezado:
    def __init__(self, id):
        self.id = id
        self.siguiente = None
        self.anterior = None
        self.accesoNodo = None

class NodoTerreno:
    def __init__(self, nombre, m, n, initX, initY, finX, finY, matriz):
        self.nombre = nombre
        self.m = m
        self.n = n
        self.initX = initX
        self.initY = initY
        self.finX = finX
        self.finY = finY
        self.matriz = matriz
        self.siguiente = None

class NodoPrioridad:
    def __init__(self, fila, columna, valor, gasto):
        self.fila = fila
        self.columna = columna
        self.valor = valor
        self.gasto = gasto
        self.next = None
class NodoCamino:
    def __init__(self, fila, columna, gasto):
        self.fila = fila
        self.columna = columna
        self.gasto = gasto
        self.next = None