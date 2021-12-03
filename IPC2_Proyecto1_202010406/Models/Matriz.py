from Models.Nodos import NodoMatriz, NodoEncabezado
from Models.LinkedLists import ListaEncabezado

class MatrizOrtogonal:

    def __init__(self):
        self.filas = ListaEncabezado()
        self.columnas = ListaEncabezado()

    def insertar(self, fila, columna, valor):
        nuevo = NodoMatriz(fila, columna, valor)

        # Insercion de encabezado por filas 
        eFila = self.filas.getEncabezado(fila)
        if eFila == None:
            eFila = NodoEncabezado(fila)
            eFila.accesoNodo = nuevo
            self.filas.setEncabezado(eFila)
        else:
            if nuevo.columna < eFila.accesoNodo.columna:
                nuevo.derecha = eFila.accesoNodo
                eFila.accesoNodo.izquierda = nuevo
                eFila.accesoNodo = nuevo
            else:
                actual = eFila.accesoNodo
                while actual.derecha is not None:
                    if nuevo.columna < actual.derecha.columna:
                        nuevo.derecha = actual.derecha
                        actual.derecha.izquierda = nuevo
                        nuevo.izquierda = actual
                        actual.derecha = nuevo
                        break
                    actual = actual.derecha
                if actual.derecha is None:
                    actual.derecha = nuevo
                    nuevo.izquierda = actual

        # Insercion de encabezado por columnas
        eColumna = self.columnas.getEncabezado(columna)
        if eColumna is None:
            eColumna = NodoEncabezado(columna)
            eColumna.accesoNodo = nuevo
            self.columnas.setEncabezado(eColumna)
        else:
            if nuevo.fila < eColumna.accesoNodo.fila:
                nuevo.abajo = eColumna.accesoNodo
                eColumna.accesoNodo.arriba = nuevo
                eColumna.accesoNodo = nuevo
            else:
                actual = eColumna.accesoNodo
                while actual.abajo is not None:
                    if nuevo.fila < actual.abajo.fila:
                        nuevo.abajo = actual.abajo
                        actual.abajo.arriba = nuevo
                        nuevo.arriba = actual
                        actual.abajo = nuevo
                        break
                    actual = actual.abajo

                if actual.abajo is None:
                    actual.abajo = nuevo
                    nuevo.arriba = actual

    def mostrarFilas(self):
        eFila = self.filas.primero
        print('----------- FILAS ------------')
        while eFila is not None:
            actual = eFila.accesoNodo
            print('\n Fila ', actual.fila)
            print('Columna      Valor')
            while actual is not None:
                print(actual.columna, '         ', actual.valor)
                actual = actual.derecha

            eFila = eFila.siguiente
        print('------------ FIN --------------')

    def mostrarColumnas(self):
        eColumna = self.columnas.primero

        print('----------- COLUMNAS ------------')
        while eColumna is not None:
            actual = eColumna.accesoNodo
            print('\n Columna ', actual.columna)
            print('Fila     Valor')
            while actual is not None:
                print(actual.fila, '        ', actual.valor)
                actual = actual.abajo
                
            eColumna = eColumna.siguiente
        print('--------------- FIN --------------')