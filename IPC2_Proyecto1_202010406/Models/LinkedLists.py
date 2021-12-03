from Models.Nodos import NodoTerreno, NodoCamino

class ListaTerrenos:
    def __init__(self):
        self.primero = None
    
    def insertar(self, nombre, m, n, initX, initY, finX, finY, matriz):
        nuevo = NodoTerreno(nombre, m, n, initX, initY, finX, finY, matriz)
        if self.primero is None:
            self.primero = nuevo
        else:
            actual = self.primero
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo
    
    def buscar(self, name):
        if self.primero is None:
            print("LISTA VACIA")
        else:
            actual = self.primero
            encontrado = False
            while actual and encontrado is False:
                if actual.nombre == name:
                    encontrado = True
                else:
                    actual = actual.siguiente
            if actual is None:
                print('ERROR: El terreno no esta en la lista.')
            return actual
            
class ListaEncabezado:
    def __init__(self, primero=None):
        self.primero = primero

# Inserciones de nodos en la lista
    def setEncabezado(self, nuevo):
        if self.primero == None:
            self.primero = nuevo
        elif nuevo.id < self.primero.id:
            nuevo.siguiente = self.primero
            self.primero.anterior = nuevo
            self.primero = nuevo
        else:
            actual = self.primero
            while actual.siguiente != None:
                if nuevo.id < actual.siguiente.id:
                    nuevo.siguiente = actual.siguiente
                    actual.siguiente.anterior = nuevo
                    nuevo.anterior = actual
                    actual.siguiente = nuevo
                    break
                actual = actual.siguiente
            
            if actual.siguiente == None:
                actual.siguiente = nuevo
                nuevo.anterior = actual

# Busqueda
    def getEncabezado(self, id):
        actual = self.primero
        while actual != None:
            if actual.id == id:
                return actual
            actual = actual.siguiente
        return None

class LinkedList:
    def __init__(self):
        self.primero = None
    
    def insertar(self, fila, columna, gasto):
        newNode = NodoCamino(fila, columna, gasto)
        if self.primero is None:
            self.primero = newNode
        else:
            actual = self.primero
            while actual.next is not None:
                actual = actual.next
            actual.next = newNode

    def onList(self, gasto):
        if self.primero is None:
            return False
        else:
            actual = self.primero
            encontrado = False
            while encontrado is False:
                if actual.gasto == gasto:
                    encontrado = True
                    return True
                else:
                    actual = actual.next
                if actual is None:
                    return False
    
    def buscarNodo(self, fila, columna):
        if self.primero is None:
            return None
        else:
            actual = self.primero
            encontrado = False
            while actual:
                if actual is not None:
                    if actual.fila == fila and actual.columna == columna:
                        encontrado =  True
                        return encontrado
                    elif actual.fila != fila and actual.columna != columna:
                        encontrado = False
                    actual = actual.next
            if actual is None:
                return False
    
    def buscarGasto(self, fila, columna):
        if self.primero is None:
            return None
        else:
            actual = self.primero
            # encontrado = False
            while actual:
                if actual is not None:
                    if actual.fila == fila and actual.columna == columna:
                        # encontrado =  True
                        return actual
                    elif actual.fila != fila and actual.columna != columna:
                        encontrado = False
                    actual = actual.next
            if actual is None:
                return False

    def size(self):
        temp = self.primero
        contador = 0
        while temp:
            if temp is not None and temp!='':
                contador += 1
            temp = temp.next
        return contador

    def printList(self):
        temp = self.primero
        while temp:
            if temp is not None or temp != '':
                return temp
            temp = temp.next
        print('\n\n')

