from Models.LinkedLists import instructionList

lexema = ''
estado = 0

class Analizador:
    def __init__(self) -> None:
        self.lexema = ''
        self.estado = 0
        
    def evaluarCadena(self, cadena):
        self.instructionList = instructionList()
        self.lexema = ''
        self.estado = 0
        cadena += '#'
        actual = ''
        noLinea = ''
        noComponente = ''
        longitud = len(cadena)
        i = 0

        while i < longitud:
            actual = cadena[i]

            if self.estado == 0:
                if actual == 'L':
                    self.estado = 1
                    self.lexema += actual
                    i +=1
                elif actual == 'C':
                    self.estado = 2
                    self.lexema += actual
                    i += 1
                elif actual == ' ':
                    self.estado = 0
                    self.saveFilasComponentes(int(noLinea), int(noComponente))
                    i += 1
                elif actual == '#':
                    self.saveFilasComponentes(int(noLinea), int(noComponente))
                    i += 1

            elif self.estado == 1:
                if actual.isdigit():
                    self.estado = 1
                    self.lexema += actual
                    noLinea = actual
                    i += 1
                else:
                    self.estado = 0

            elif self.estado == 2:
                if actual.isdigit():
                    self.estado = 2
                    self.lexema += actual
                    noComponente = actual
                    i += 1
                else:
                    self.estado = 0
        # self.instructionList.show() #Recordar borrar
    
    def saveFilasComponentes(self, linea, componente):
        self.instructionList.append(linea, componente)

    def getLista(self):
        return self.instructionList