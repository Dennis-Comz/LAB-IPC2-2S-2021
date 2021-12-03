from os import system, startfile
from tkinter import *
import PIL.Image
import PIL.ImageTk
class Cola:
    def __init__(self):
        pass

    def graficar(self, pasos):
        paso = pasos.first
        nPaso = pasos.first.next
        graphviz = '''
        digraph L{
        node[shape=box fillcolor="skyblue" style= filled]
        subgraph cluster_p{
        label = "Cola de Secuencia"
        bgcolor = "#FFFFFF"\n'''

        graphviz += "\t\t raiz[label = \"L" + str(paso.noLinea) + "C" + str(paso.noComponente) + "\"]\n"
        graphviz += "\t\t edge[dir = \"Normal\"]\n"

        if paso.next != None:
            paso = paso.next
        
        i = 1
        while paso:
            graphviz += "\t\tnodo" + str(i) + "[label = \"L" + str(paso.noLinea) + "C" + str(paso.noComponente) + "\", group = " + str(i) + "];\n"
            i += 1
            paso = paso.next
        
        i = 1
        while nPaso:
            if i == 1:
                graphviz += "\t\traiz->nodo1\n"
                graphviz += "\t\t{rank = same; raiz; nodo1}\n"
            else:
                graphviz += "\t\tnodo" + str(i-1) + "->nodo" + str(i) + "\n"
                graphviz += "\t\t{rank = same; nodo" + str(i-1) + ";nodo" + str(i) + "}\n"
            i += 1
            nPaso = nPaso.next
        graphviz += "\t}\n}"

        archName = "cola.dot"
        archivo = open(archName, "w")
        archivo.write(graphviz)
        archivo.close()

        system('dot -Tpng ' +  archName + ' -o ' + 'cola' + '.png')
        img = PIL.Image.open('cola.png')
        img = PIL.ImageTk.PhotoImage(img)
        self.label = Label(image=img)
        self.label.image = img
        self.label.place(x=20, y=450)
            
    def setRoot(self, root):
        self.root = root
