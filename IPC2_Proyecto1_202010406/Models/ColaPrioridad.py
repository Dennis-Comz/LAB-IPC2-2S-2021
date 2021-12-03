from Models.Nodos import NodoPrioridad

class PriorityQueue:
    def __init__(self):
        self.front = None
    
    def isEmpty(self):
        return True if self.front == None else False

    def push(self, nodo):
        if self.isEmpty() == True:
            self.front = NodoPrioridad(nodo.fila, nodo.columna, nodo.valor, nodo.gasto)
            return 1
        else:
            if self.front.gasto > nodo.gasto:
                newNode = NodoPrioridad(nodo.fila, nodo.columna, nodo.valor, nodo.gasto)
                newNode.next = self.front

                self.front = newNode
                return 1
            else:
                temp = self.front
                while temp.next:
                    if nodo.gasto <= temp.next.gasto:
                        break
                    temp = temp.next
                newNode = NodoPrioridad(nodo.fila, nodo.columna, nodo.valor, nodo.gasto)
                newNode.next = temp.next
                temp.next = newNode
                return 1
        
    def pop(self):
        if self.isEmpty() == True:
            return False
        else:
                self.front = self.front.next
                return self.front
                
    def peek(self):
        if self.isEmpty() == True:
            return
        else:
            return self.front

    def traverse(self):
        if self.isEmpty() == True:
            return "Cola vacia"
        else:
            temp = self.front
            print('\n\n VALORES DE LA COLA DE PRIORIDAD')
            while temp:
                if temp.next is not None:
                    print("fila: " + str(temp.fila) + ";  columna: " + str(temp.columna) + "; gasto: " + str(temp.gasto))   
                temp = temp.next
            print('\n')

