import CRUD
# Menu de opciones del C.R.U.D.

while True:
    print("\nElija una opción :\n 1- Agregar\n 2- Modificar\n 3- Borrar \n 4- Buscar\n 5- Salir\n")
    opcion = int(input("Ingrese la opción: "))
    if opcion == 1:
        leyes = CRUD.Ley()
        leyes.agregarLey()
        print("Los datos se han agregado correctamente.")
    elif opcion == 2:
        leyes = CRUD.Ley()
        # Especificar el número de normativa de la ley que deseas modificar
        leyes.nro_normativa = int(input("Ingrese el numero de normativa que quiere modificar: "))
        leyes.mostrarMenuModificar()

    elif opcion == 3 :
        leyes= CRUD.Ley()
        # Especificar el número de normativa de la ley que deseas borrar
        leyes.nro_normativa = int(input("Ingrese el numero de normativa que quiere borrar: "))
        leyes.borrarLey ()
        
    elif opcion == 4 :
        leyes = CRUD.Ley()
        while True:
            print(" 1- Busqueda por N° de normativa \n 2- Busqueda por palabras clave \n")
            busqueda= int(input("Ingrese su opcion: "))
            if busqueda == 1:
                # Especificar el número de normativa de la ley que deseas buscar
                leyes.nro_normativa = int(input("Ingrese el numero de normativa que quiere buscar: "))
                leyes.busquedaNroNormativa ()
                break

            elif busqueda == 2:
                # Especificar la palabra clave para buscar la ley que deseas
                leyes.palabras_clave = input("Ingrese una palabra clave: ")
                leyes.busquedaPalabraClave()   
                break
            else:
                print("Elija una opción correcta\n")
    elif opcion == 5 :
        break
    else:
        print("Elija una opción correcta\n")
        
        
