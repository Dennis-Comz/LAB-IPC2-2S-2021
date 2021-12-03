from CargarArchivo import *
from Models.ColaPrioridad import *
from Models.LinkedLists import LinkedList

ll = LinkedList()

class Procesar:
    def matrizRepre(self, lista, terreno):
        terrenoN2 = terreno
        filas = terrenoN2.matriz.filas.primero
        columnas = terrenoN2.matriz.columnas.primero

        while columnas is not None:
            actualColumnas = columnas.accesoNodo
            while actualColumnas is not None:
                while filas is not None:
                    actualFilas = filas.accesoNodo
                    while actualFilas is not None:
                        if lista.buscarNodo(actualFilas.fila, actualFilas.columna) == True:
                            # actualFilas.valor = self.colored(55, 168, 82, str(1))
                            print("| " + str(1), end='|')
                        else:
                            # actualFilas.valor = self.colored(255, 255, 255, str(0))
                            print("| " + str(0), end='|')
                        actualFilas = actualFilas.derecha
                    filas = filas.siguiente
                    print()
                actualColumnas = actualColumnas.abajo
            columnas = columnas.siguiente
        print('\n')
        
    def examinarNodos(self, nodo, terreno, cola):
        terrenoN = terreno

        if terrenoN.initY == nodo.fila and terrenoN.initX == nodo.columna:
            nodo.visitado = True
            nodo.gasto = nodo.valor
        if terrenoN.finY == nodo.fila and terrenoN.finX == nodo.columna:
            nodo.visitado = True

        if nodo.arriba is not None:
            cambio = False
            if nodo.arriba.visitado is not True:
                nodo.arriba.visitado = True
                if nodo.gasto != 0:
                    nodo.arriba.gasto += nodo.gasto + nodo.arriba.valor
                else:
                    nodo.arriba.gasto += nodo.valor + nodo.arriba.valor
            elif nodo.gasto < nodo.arriba.gasto:
                cambio = True
                nodo.arriba.gasto = nodo.gasto + nodo.arriba.valor

        if nodo.abajo is not None:
            if nodo.abajo.visitado is not True:
                nodo.abajo.visitado = True
                if nodo.gasto != 0:
                    nodo.abajo.gasto += nodo.gasto + nodo.abajo.valor
                else:
                    nodo.abajo.gasto += nodo.valor + nodo.abajo.valor
            elif nodo.abajo.gasto > nodo.gasto:
                nodo.abajo.gasto = nodo.gasto + nodo.abajo.valor

        if nodo.izquierda is not None:
            if nodo.izquierda.visitado is not True:
                nodo.izquierda.visitado = True
                if nodo.gasto != 0:
                    nodo.izquierda.gasto += nodo.gasto + nodo.izquierda.valor
                else:
                    nodo.izquierda.gasto += nodo.valor + nodo.izquierda.valor
            elif nodo.izquierda.gasto > nodo.gasto:
                nodo.izquierda.gasto = nodo.gasto + nodo.izquierda.valor

        if nodo.derecha is not None:
            if nodo.derecha.visitado is not True:
                nodo.derecha.visitado = True
                if nodo.gasto != 0:
                    nodo.derecha.gasto += nodo.gasto + nodo.derecha.valor
                else:
                    nodo.derecha.gasto += nodo.valor + nodo.derecha.valor
            elif nodo.derecha.gasto > nodo.gasto:
                nodo.derecha.gasto = nodo.gasto + nodo.derecha.valor

        if nodo.columna == terrenoN.finX:
            if nodo.columna == terrenoN.finX and nodo.fila == terrenoN.finX:
                nodo.gasto = nodo.gasto
                cola.push(nodo)
        
        cola.push(nodo)

    def procesarLista(self, name):
        pq = PriorityQueue()
        terreno = listTerrenos.buscar(name)
        if terreno is not None:
            filas = terreno.matriz.filas.primero
            columnas = terreno.matriz.columnas.primero
            contador = 0
            # CICLO PARA RECORRER LA MATRIZ Y ENVIAR CADA DATO A SER ANALIZADO
            while filas is not None:
                actualF = filas.accesoNodo
                while actualF is not None:
                    while columnas is not None:
                        actualC = columnas.accesoNodo
                        while actualC is not None:
                            self.examinarNodos(actualC, terreno, pq)
                            contador += 1
                            actualC = actualC.abajo
                        columnas = columnas.siguiente
                    actualF = actualF.derecha
                filas = filas.siguiente
            print('\nRecorriendo puntos del terreno...')
            print("Verficando puntos adyacentes...")
            print("Obteniendo gasto optimo...")
            print("Ruta encontrada.")

            print("\n\nREPRESENTACION GRAFICA DEL " + name.upper())
            
            # LISTA Y CICLO PARA OBTENER LOS DATOS EN LA COLA
            tempPQ = pq
            for i in range(0,contador):
                first = tempPQ.peek()
                if first is not None:
                    if ll.onList(first.gasto) == False:
                        ll.insertar(first.fila, first.columna, first.gasto)
                    else:
                        second = tempPQ.pop()
                        if second is not None:
                            if ll.onList(second.gasto) == True:
                                continue
                            else:
                                if second.fila == terreno.finY and second.columna == terreno.finX:
                                    print("*Consumo total de Combustile: " + str(second.gasto) + " Unidades\n")
                                    ll.insertar(second.fila, second.columna, second.gasto)
                                    break
                                else:
                                    ll.insertar(second.fila, second.columna, second.gasto)
            self.matrizRepre(ll, terreno)