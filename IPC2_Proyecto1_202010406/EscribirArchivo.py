import os
from ProcesarTerreno import *
from CargarArchivo import *
import xml.etree.cElementTree as ET

class EscribirArchivo:
    def escribir(ruta, nombreT):
        terreno = listTerrenos.buscar(nombreT)

        root = ET.Element('terreno', nombre = nombreT)

        posinicio = ET.SubElement(root, "posicionInicio")
        ET.SubElement(posinicio, "x").text = str(terreno.initX)
        ET.SubElement(posinicio, "y").text = str(terreno.initY)

        posFin = ET.SubElement(root, "posicionfin")
        ET.SubElement(posFin, "x").text = str(terreno.finX)
        ET.SubElement(posFin, "y").text = str(terreno.finY)

        nodoFin = ll.buscarGasto(terreno.finY, terreno.finX)
        if nodoFin == False:
            ET.SubElement(root, "combustible").text = '0'
        else:
            ET.SubElement(root, "combustible").text = str(nodoFin.gasto)

        temp = ll.printList()
        while temp:
            if temp is not None:
                ET.SubElement(root, "posicion", y = str(temp.fila), x = str(temp.columna)).text = str(temp.gasto)
            temp = temp.next
        
        tree = ET.ElementTree(root)
        tree.write(ruta)
        os.startfile(ruta)
        print("\nARCHIVO GENERADO\n")