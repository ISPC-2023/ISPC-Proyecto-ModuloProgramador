import CRUD as crud
import ui
ley = crud.Ley()


def mostrarMenuModificar(nro_normativa):
    print(ui.header)
    print("\n¿Cómo desea modificar la Normativa?:\n 1- Modificar campos específicos.\n 2- Modificar toda la norma.\n 0- Salir\n")
    while True:
        opcion = int(input(ui.opcion))
        if (opcion >= 0 and opcion <= 2) or opcion == 9:
            modificar = opcion
            break
        else:
            print(ui.erroneo)

    if modificar == 1:
        mostrarMenuModificarCampos(nro_normativa)

    elif modificar == 2:
        modificarNorma(nro_normativa)

    elif modificar == 0:
        print(ui.closer)
        print(ui.decorador)


def mostrarMenuModificarCampos(nro_normativa):
    print(ui.header)
    print("\nElija el campo a modificar:\n 1- Fecha de la Normativa\n 2- Descripción\n 3- Enlace a la Norma\n 4- Categoría\n 5- Jurisdicción/Órgano Legislativo\n 6- Tipo de Normativa\n 7- Palabras Clave\n 0- Salir\n")
    while True:
        opcion = int(input(ui.opcion))
        if opcion >= 0 and opcion <= 9:
            modificarCampos(opcion, nro_normativa)
            break
        else:
            print(ui.erroneo)


def modificarCampos(opcion, nro_normativa):
    if opcion == 1:
        campo = "Fecha"
        nuevo_valor = input("Ingrese la nueva Fecha (dd-mm-aaaa): ")
        crud.Ley.modificarLey(nro_normativa, campo, nuevo_valor)
        print(ui.correcto)

    elif opcion == 2:
        campo = "Descripcion"
        nuevo_valor = input("Ingrese ingrese la nueva Descripción: ")
        crud.Ley.modificarLey(nro_normativa, campo, nuevo_valor)
        print(ui.correcto)

    elif opcion == 3:
        campo = "Link"
        nuevo_valor = input("Ingrese ingrese el nuevo Enlace: ")
        crud.Ley.modificarLey(nro_normativa, campo, nuevo_valor)
        print(ui.correcto)

    elif opcion == 4:
        campo = "id_categoria"
        while True:
            print("\nElija la nueva Categoría:\n 1- Laboral\n 2- Penal\n 3- Civil\n 4- Comercial\n 5- Familia y Sucesiones\n 6- Agrario y Ambiental\n 7- Minería\n 8- Derecho informático\n")
            opcion = int(input(ui.opcion))
            if opcion >= 1 and opcion <= 8:
                nuevo_valor = opcion
                break
            else:
                print(ui.erroneo)
        crud.Ley.modificarLey(nro_normativa, campo, nuevo_valor)
        print(ui.correcto)

    elif opcion == 5:
        campo = "id_jurisdiccion"
        while True:
            print(
                "\nElija la nueva Jurisdicción:\n 1- Nacional\n 2- Provincial\n")
            opcion = int(input(ui.opcion))
            if opcion == 1 or opcion == 2:
                nuevo_valor = opcion
                break
            else:
                print(ui.erroneo)
        crud.Ley.modificarLey(nro_normativa, campo, nuevo_valor)
        campo = "id_organo_legislativo"
        crud.Ley.modificarLey(nro_normativa, campo, nuevo_valor)
        print(ui.correcto)

    elif opcion == 6:
        campo = "id_tipo_normativa"
        while True:
            print(
                "\nElija el nuevo tipo de normativa:\n 1- Ley\n 2- Decreto\n 3- Resolución\n")
            opcion = int(input(ui.opcion))
            if opcion >= 1 and opcion <= 3:
                nuevo_valor = opcion
                break
            else:
                print(ui.erroneo)
        crud.Ley.modificarLey(nro_normativa, campo, nuevo_valor)
        print(ui.correcto)
    elif opcion == 7:
        crud.Ley.cambiarPalabrasClaves(nro_normativa)
        print(ui.correcto)

    elif opcion == 0:
        print(ui.decorador)
        print(ui.closer)
        print(ui.decorador)
        exit()


def modificarNorma(nro_normativa):
    i = 1
    while i <= 7:
        modificarCampos(i, nro_normativa)
        i += 1
    print('¿Desea modificar otra norma?')
    eleccion = input('Y/N:')
    if eleccion == 'Y' or eleccion == 'y':
        nro_normativa = input('Ingrese el número de normativa a modificar: ')
        modificarNorma(nro_normativa)

