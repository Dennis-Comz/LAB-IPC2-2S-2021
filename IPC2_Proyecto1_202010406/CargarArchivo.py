from Models.Matriz import *
from  Models.LinkedLists import *
import xml.etree.ElementTree as ET

# LISTA TERRENOS GLOBAL
listTerrenos = ListaTerrenos()
class Cargar:
    
    def leerArchivo(path):
        root = ET.parse(path).getroot()

        for tag in root.findall('terreno'):
            #Variables a modificar por iteracion
            mtOrtogonal = MatrizOrtogonal()
            cargado = False

            # Nombre de los terrenos
            nombre = tag.get('nombre')

            # Dimensiones de los terrenos
            dM = int(tag[0][0].text)
            dN = int(tag[0][1].text)

            # Posicion Inicial de los terrenos
            piX = int(tag[1][0].text)
            piY = int(tag[1][1].text)

            # Posicion Final de los terrenos
            pfX = int(tag[2][0].text)
            pfY = int(tag[2][1].text)

            # Posiciones y valor de combustible que posee el terreno
            for i in range(3, len(tag)):
                posX = int(tag[i].get('x'))
                posY = int(tag[i].get('y'))
                valor = int(tag[i].text)
                if posX > dM or posY > dN:
                    print("Dimension Invalida")
                else:
                    cargado = True
                    mtOrtogonal.insertar(posY, posX, valor)

            if cargado == True:
                listTerrenos.insertar(nombre, dM, dN, piX, piY, pfX, pfY, mtOrtogonal)
                print(nombre + " Cargado")
            else:
                print(nombre + ' No Cargado')