from os import system,startfile
from CargarArchivo import *

class Grafica:
    def __init__(self, name):
        terreno = listTerrenos.buscar(name)
        if terreno is not None:
            filas = terreno.matriz.filas.primero
            columnas = terreno.matriz.columnas.primero

            graphviz = '''
            digraph L{\n
            node[shape=box fillcolor="#FFFFFF" style = filled]\n
            subgraph cluster_p{\n'''
            graphviz += "\t\t label = \"" + name + "\"\n"
            graphviz += "\t\t bgcolor = \"#C8FD88\"\n"
            graphviz += "\t\t raiz[label = \"0,0\"]\n"
            graphviz += "\t\t edge[dir = \"none\"]\n\n"

            n = terreno.n
            for i in range(1, n+1):
                graphviz += "\t\t Fila" + str(i)+ "[label = \"" + str(i) + "\", group = 1, fillcolor=\"#E67E37\"];\n"
            for i in range(1, n+1):
                if i+1 > n:
                    break
                else:
                    graphviz += "\t\t Fila" + str(i) + "->Fila" + str(i+1) + ";\n"
            
            m = terreno.m
            cm = ""
            it = 2
            for i in range(1, m+1):
                graphviz += "\t\t Columna" + str(i)+ "[label = \"" + str(i) + "\", group = " + str(it) + ", fillcolor=yellow];\n"
                it += 1
                if i != m:
                    cm += "Columna" + str(i) + ";"
                else:
                    cm += "Columna" + str(i) + "}"

            for i in range(1, m+1):
                if i+1 > m:
                    break
                else:
                    graphviz += "\t\t Columna" + str(i) + "->Columna" + str(i+1) + ";\n"

            graphviz += "\t\t raiz->Fila1;\n"
            graphviz += "\t\t raiz->Columna1;\n"

            graphviz += "\t\t {rank = same raiz;" + cm + "\n"

            contador = 2
            while filas is not None:
                actualFilas = filas.accesoNodo
                while actualFilas is not None:
                    while columnas is not None:
                        actualColumnas = columnas.accesoNodo
                        while actualColumnas is not None:
                            graphviz += "\t\t nodo"+str(actualColumnas.fila) + "_" + str(actualColumnas.columna)
                            graphviz += "[label = \""+str(actualColumnas.valor) + "\","
                            graphviz += "group=" + str(contador) + ", fillcolor=\"#FE493D\"]\n"
                            actualColumnas = actualColumnas.abajo
                        contador += 1
                        columnas = columnas.siguiente
                    actualFilas = actualFilas.derecha
                filas = filas.siguiente
            
            filas = terreno.matriz.filas.primero
            columnas = terreno.matriz.columnas.primero
            contadorF = 1
            while columnas is not None:
                actualColumnas = columnas.accesoNodo
                while actualColumnas is not None:
                    while filas is not None:
                        contadorC = 1
                        nodo = ""
                        graphviz += "\t\t Fila" + str(contadorF) + "->nodo" + str(contadorF) + "_" + str(contadorC) + ";\n"
                        actualFilas = filas.accesoNodo
                        while actualFilas is not None:
                            if contadorC != m:
                                nodo += "nodo" + str(contadorF) + "_" + str(contadorC) + ";"
                            else:
                                nodo += "nodo" + str(contadorF) + "_" + str(contadorC) + "}"
                            if contadorC + 1 > m:
                                break
                            else:
                                graphviz += "\t\t nodo" + str(contadorF) + "_" + str(contadorC) + "->nodo" + str(contadorF) + "_" + str(contadorC+1) + ";\n"
                            contadorC += 1
                            actualFilas = actualFilas.derecha
                        graphviz += "\t\t {rank = same;Fila" + str(contadorF) + ";" + nodo + "\n"
                        contadorF += 1
                        filas = filas.siguiente
                    actualColumnas = actualColumnas.abajo
                columnas = columnas.siguiente

            filas = terreno.matriz.filas.primero
            columnas = terreno.matriz.columnas.primero
            contadorC = 1
            while filas is not None:
                actualFilas = filas.accesoNodo
                while actualFilas is not None:
                    while columnas is not None:
                        contadorF = 1
                        graphviz += "\t\t Columna" + str(contadorC) + "->nodo" + str(contadorF) + "_" + str(contadorC) + ";\n"
                        actualColumnas = columnas.accesoNodo
                        while actualColumnas is not None:
                            if contadorF + 1 > n:
                                break
                            else:
                                graphviz += "\t\t nodo" + str(contadorF) + "_" + str(contadorC) + "->nodo" + str(contadorF+1) + "_" + str(contadorC) + ";\n"
                            contadorF += 1
                            actualColumnas = actualColumnas.abajo
                        contadorC += 1
                        columnas = columnas.siguiente  
                    actualFilas = actualFilas.derecha
                filas = filas.siguiente

            graphviz += "\t}\n}"

            archName = name + ".dot"     
            archivo = open(archName, "w")
            archivo.write(graphviz)
            archivo.close()

            system('dot -Tpng ' +  archName + ' -o ' + name + '.png')
            startfile(name + '.png')
            # print(graphviz)