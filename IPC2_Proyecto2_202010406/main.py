from tkinter import *
from Administrador import Administrador



class main:
    def __init__(self):
        self.root = Tk()
        self.root.config(bg='skyblue')
        self.root.title('Digital Intelligence, S. A.')
        self.root.geometry("1000x800")
        self.admin = Administrador()
        self.admin.setRoot(self.root)
        self.gui()

    def gui(self):

        self.btnConfigMaquina = Button(self.root, text='Configurar', height=2, width=12, command=self.admin.configMaquina)
        self.btnConfigMaquina.place(x=20, y=20)

        self.btnSimular = Button(self.root, text='Simulacion', height=2, width=12, command=self.admin.genSimulacion)
        self.btnSimular.place(x=150, y=20)

        self.btnReportes = Button(self.root, text='Reportes', height=2, width=12, command=self.admin.reporte)
        self.btnReportes.place(x=280, y=20)
        
        self.btnAyuda = Button(self.root, text='Ayuda', height=2, width=12, command=self.admin.datos)
        self.btnAyuda.place(x=410, y=20)

        self.txtProducto = Entry(self.root, font='Verdana 14', justify='center', width=17)
        self.txtProducto.place(x=20, y=120)

        self.btnEnsamblar = Button(self.root, text='Ensamblar', height=1, width=12, command=self.ensamblar)
        self.btnEnsamblar.place(x=300,y=120)
        
        self.btnVer = Button(self.root, text='Ver Productos', height=1, width=12, command=self.admin.showValues)
        self.btnVer.place(x=410,y=120)

        self.root.mainloop()
    
    def ensamblar(self):
        value = self.txtProducto.get()
        self.admin.ensamblarPr(value)

if __name__ == '__main__':
    main()