from Models.LinkedLists import *
import xml.etree.ElementTree as ET

class Reader:
    def __init__(self):
        self.listaProductos = ProductList()
        self.listaLineas = LineList()
    
    def setMaquina(self, path):
        root = ET.parse(path).getroot()
        
        lineasPd = int(root[0].text)
        
        for i in range(lineasPd):
        
            noLinea = int(root[1][i][0].text)
            cantComponentes = int(root[1][i][1].text)
            tiempo = int(root[1][i][2].text)
        
            self.listaLineas.append(noLinea, cantComponentes, tiempo)

        for productos in root[2].findall('Producto'):
            nombre = productos[0].text
            instrucciones = productos[1].text
            
            self.listaProductos.append(nombre, instrucciones)
    
    def setSimulacion(self, path):
        self.listaSimulacion = SimulationList()
        self.ListaElaborar = DevelopList()

        root = ET.parse(path).getroot()

        nombreSimulacion = root[0].text

        for productos in root[1].findall('Producto'):
            nombreProducto = productos.text
            self.ListaElaborar.append(nombreProducto)
        
        self.listaSimulacion.append(nombreSimulacion, self.ListaElaborar)