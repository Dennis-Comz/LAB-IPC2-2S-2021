from Queue import Queue

q = Queue()

class Admin:

    def ingresar():
        ingrediente = input("Ingrese el ingrediente: ")
        q.push(ingrediente)
        if q.isEmpty() is not None:
            print("Orden Ingresada\n")
        else:
            print("Error: No se pudo Ingresar\n")
    def entregar():
        if q.isEmpty() == True:
            print("Cola vacia - Totalidad de Ordenes Entregadas\n")
        else:
            print("Entregando Orden de Pizza de " + q.pop() + "...\n")

    def mostrarOrdenes():
        if q.isEmpty() == True:
            print("Cola vacia - Totalidad de Ordenes Entregadas\n")
        else:
            print("Ordenes en Cola: ")
            q.printQueue()

    def datos():
        datos = '''\n\n* Nombre: Dennis Mauririco Corado Muñóz\n* Carné: 202010406\n* Curso: Introduccion a la Programacion y Computacion 2 seccion A\n* Carrera: Ingeniería en Ciencias y Sistemas\n* Semestre: 4to Semestre\n'''
        print(datos)