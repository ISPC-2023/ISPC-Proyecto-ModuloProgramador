import CRUD as crud
import menuUpdate 
import ui

# Menu de opciones del C.R.U.D.
while True:
    print(ui.header)
    print("\nElija una opción :\n 1- Agregar Nueva Normativa.\n 2- Modificar Normativa Existente.\n 3- Borrar Normativa Existente.\n 4- Buscar Normativa Existente.\n 5- Salir de la Aplicación.\n")
    opcion = int(input("Ingrese la opción elegida: "))
    if opcion == 1:
        crud.Ley.agregarLey()
        print("Los datos se han agregado correctamente.")
    elif opcion == 2:
        # Especificar el número de normativa de la ley que deseas modificar
        nro_normativa = int(
            input("Ingrese el numero de normativa que desea modificar: "))
        menuUpdate.mostrarMenuModificar(nro_normativa)
    elif opcion == 3:
        # Especificar el número de normativa de la ley que deseas borrar
        nro_normativa = int(
            input("Ingrese el numero de normativa que quiere borrar: "))
        crud.Ley.borrarLey(nro_normativa)

    elif opcion == 4:
        while True:
            print(" 1- Busqueda por N° de normativa \n 2- Busqueda por palabras clave \n")
            busqueda = int(input("Ingrese su opcion: "))
            if busqueda == 1:
                # Especificar el número de normativa de la ley que deseas buscar
                nro_normativa = int(
                    input("Ingrese el numero de normativa que quiere buscar: "))
                crud.Ley.busquedaNroNormativa(nro_normativa)
                break

            elif busqueda == 2:
                # Especificar la palabra clave para buscar la ley que deseas
                palabras_clave = input("Ingrese una palabra clave: ")
                crud.Ley.busquedaPalabraClave(palabras_clave)
                break
            else:
                print(ui.erroneo)
    elif opcion == 5:
        print(ui.decorador)
        print(ui.closer)
        print(ui.decorador)
        break
    else:
        print(ui.erroneo)
