class Node:
    def __init__(self, order):
        self.order = order
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
    
    def isEmpty(self):
        return True if self.front == None else False

    def push(self, orden):
        newNode = Node(orden)
        if self.isEmpty() == True:
            self.front = newNode
        else:
            actual = self.front
            while actual.next is not None:
                actual = actual.next
            actual.next = newNode
    
    def pop(self):
        if self.isEmpty() == True:
            return True
        else:
            temp = self.front
            self.front = temp.next
            return temp.order

    def printQueue(self):
        if self.isEmpty() == True:
            return True
        else:
            temp = self.front
            contador = 1
            while temp:
                if temp is None:
                    break
                elif temp.next is not None:
                    print(str(contador) + ". " + temp.order)
                    contador += 1
                else:
                    print(str(contador) + ". " + temp.order)
                    contador += 1
                temp = temp.next
            print("\n")