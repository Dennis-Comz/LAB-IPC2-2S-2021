from Admin import Admin


def main():
    option = 0
    while option != 5:
        print("Seleccione una opcion: ")
        print("\t 1. Ingresar Orden")
        print("\t 2. Entregar Orden")
        print("\t 3. Mostrar Ordenes")
        print("\t 4. Mostrar Datos del Estudiante")
        print("\t 5. Salir")
        option = selectOp()

        if option == 1:
            Admin.ingresar()
        elif option == 2:
            Admin.entregar()
        elif option == 3:
            Admin.mostrarOrdenes()
        elif option == 4:
            Admin.datos()

def selectOp():
    option = input("Opcion: ")
    while option < '1' or option > '5':
        print("Ingrese una opcion valida.")
        option = input()
    else:
        return int(option)

if __name__ == "__main__":
    main()