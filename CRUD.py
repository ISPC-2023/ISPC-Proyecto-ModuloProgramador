import BBDD

#DEFINICION DE LA CLASE LEY
class Ley():
    def __init__(self):
        self.nro_normativa = 0
        self.fecha = ""
        self.descripcion = ""
        self.link = ""
        self.id_categoria = 0
        self.id_jurisdiccion = 0
        self.id_organo_legislativo = 0
        self.id_tipo_normativa = 0
        self.palabras_clave = ""       
        
#METODO PARA AGREGAR UNA LEY     
    def agregarLey():
        base_de_datos = BBDD.Base_de_datos()
        base_de_datos.abrirBase()
        cursor= base_de_datos.cursor()

        nro_normativa = int(input("Ingrese el número de normativa: "))
        while True:
            print("\nElija la opción que corresponde al tipo de normativa:\n 1- Ley\n 2- Decreto\n 3- Resolución\n")
            opcion = int(input("Ingrese la opción: "))
            if opcion >= 1 and opcion <= 3:
                id_tipo_normativa = opcion
                break
            else:
                print("Elija una opción correcta\n")

        fecha = input("\nIngrese la fecha: ")
        descripcion = input("\nIngrese una descripción: ")
        while True:
            print("\nElija una opción de categoría:\n 1- Laboral\n 2- Penal\n 3- Civil\n 4- Comercial\n 5- Familia y Sucesiones\n 6- Agrario y Ambiental\n 7- Minería\n 8- Derecho informático\n")
            opcion = int(input("Ingrese la opción: "))
            if opcion >= 1 and opcion <= 8:
                id_categoria = opcion
                break
            else:
                print("Elija una opción correcta\n")

        while True:
            print(
                "\nElija una opción de la jurisdicción correspondiente:\n 1- Nacional\n 2- Provincial\n")
            opcion = int(input("Ingrese la opción: "))
            if opcion == 1 or opcion == 2:
                id_jurisdiccion = opcion
                break
            else:
                print("Elija una opción correcta\n")

        while True:
            print("\nElija la opción que corresponde al órgano legislativo:\n 1- Congreso de la Nación\n 2- Legislatura de Córdoba\n")
            opcion = int(input("Ingrese la opción: "))
            if opcion == 1 or opcion == 2:
                id_organo_legislativo = opcion
                break
            else:
                print("Elija una opción correcta\n")

        link = input("\nIngrese el enlace: ")
        palabras_clave = input(
            "\nIngrese las palabras separadas por un espacio: ")
        lista_palabras = palabras_clave.split()

        # Crear la consulta SQL para insertar los datos en la tabla Ley
        consulta = "INSERT INTO Ley (nro_normativa, id_tipo_normativa, fecha, descripcion, link, id_categoria, id_jurisdiccion, id_organo_legislativo) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        valores = (nro_normativa, id_tipo_normativa, fecha, descripcion, link, id_categoria, id_jurisdiccion, id_organo_legislativo)
        cursor.execute(consulta, valores)

        # Obtener el id_ley
        id_ley = cursor.lastrowid

        # Agrega las palabras claves a la tabla palabra_clave
        for palabra in lista_palabras:
            consulta_palabra = "INSERT OR IGNORE INTO Palabra_clave (Palabra) VALUES (?)"
            valores_palabra = (palabra,)
            cursor.execute(consulta_palabra, valores_palabra)

        # Vincular la palabra clave con la ley en la tabla Ley_por_palabra_clave
        consulta_vinculo = "INSERT INTO Ley_por_palabra_clave (id_ley, id_palabra_clave) VALUES (?, ?)"
        for palabra in lista_palabras:
            consulta_id_palabra = "SELECT id_palabra_clave FROM Palabra_clave WHERE Palabra = ?"
            valores_id_palabra = (palabra,)
            cursor.execute(consulta_id_palabra, valores_id_palabra)
            resultado_id_palabra = cursor.fetchone()
            if resultado_id_palabra:
                id_palabra_clave = resultado_id_palabra[0]
                valores_vinculo = (id_ley, id_palabra_clave)
                cursor.execute(consulta_vinculo, valores_vinculo)

        base_de_datos.confirmarCambios()
        cursor.close()
        base_de_datos.cerrarBase()
#METODO PARA BORRAR UNA LEY 
    
    def borrarLey (nro_normativa):
        base_de_datos = BBDD.Base_de_datos()
        base_de_datos.abrirBase()
        cursor = base_de_datos.cursor()

        #Borra las palabras claves 
        consulta = "SELECT id_ley FROM Ley WHERE Nro_Normativa = ?"
        valor = nro_normativa,
        cursor.execute(consulta, valor)
        id_ley = cursor.fetchone()
        consulta_eliminar = "DELETE FROM Ley_por_palabra_clave WHERE id_ley = ?"
        valores_eliminar = (id_ley[0])
        cursor.execute(consulta_eliminar, (valores_eliminar,))

        consulta= "DELETE FROM Ley WHERE Nro_Normativa = ?"
        valor = nro_normativa,
        cursor.execute (consulta , valor)

        print("La ley N° {} ha sido borrada con éxito".format(str(nro_normativa)))

        base_de_datos.confirmarCambios()
        cursor.close()
        base_de_datos.cerrarBase
        # Create Agregado de registros a la base de datos
                
#METODO DE BÚSQUEDA POR PALABRA CLAVE
    def busquedaPalabraClave(palabras_clave):
        base_de_datos = BBDD.Base_de_datos()
        base_de_datos.abrirBase()
        cursor = base_de_datos.cursor()

        consulta= """
            SELECT TN.Tipo_normativa, L.Nro_Normativa, L.Fecha, L.Descripcion, C.Categoria, J.Jurisdiccion, OL.Organo_legislativo, L.Link 
            FROM Ley L
            JOIN Categoria C ON C.id_categoria = L.id_categoria
            JOIN Tipo_normativa TN ON TN.id_tipo_normativa = L.id_tipo_normativa
            JOIN Jurisdiccion J ON J.id_jurisdiccion = L.id_jurisdiccion
            JOIN Organo_legislativo OL ON OL.id_organo_legislativo = L.id_organo_legislativo
            JOIN Ley_por_palabra_clave LP ON L.id_ley = LP.id_ley
            JOIN Palabra_clave P ON LP.id_palabra_clave = P.id_palabra_clave
            WHERE P.Palabra = ?;
            """
        valor = palabras_clave,
        cursor.execute (consulta , valor)
        resultado_consulta = cursor.fetchone()
        Ley.imprimirEnPantalla (resultado_consulta)

        base_de_datos.confirmarCambios()
        cursor.close()
        base_de_datos.cerrarBase
#METODO PARA BUSCAR NORMATIVA POR NÚMERO
    def busquedaNroNormativa (nro_normativa):
        base_de_datos = BBDD.Base_de_datos()
        base_de_datos.abrirBase()
        cursor = base_de_datos.cursor()

        consulta= """
            SELECT TN.Tipo_normativa, L.Nro_Normativa, L.Fecha, L.Descripcion, C.Categoria, J.Jurisdiccion, OL.Organo_legislativo, L.Link 
            FROM Ley L
            JOIN Categoria C ON C.id_categoria = L.id_categoria
            JOIN Tipo_normativa TN ON TN.id_tipo_normativa = L.id_tipo_normativa
            JOIN Jurisdiccion J ON J.id_jurisdiccion = L.id_jurisdiccion
            JOIN Organo_legislativo OL ON OL.id_organo_legislativo = L.id_organo_legislativo
            WHERE L.Nro_Normativa = ?;
            """
        valor = nro_normativa,
        cursor.execute (consulta , valor)
        resultado_consulta = cursor.fetchone()
        Ley.imprimirEnPantalla (resultado_consulta)

        base_de_datos.confirmarCambios()
        cursor.close()
        base_de_datos.cerrarBase

#METODO PARA MOSTRAR RESULTADO EN PANTALLA        
    def imprimirEnPantalla(resultado_consulta):   
        if resultado_consulta:
            # Obtenemos los datos de la ley
            id_tipo_normativa,nro_normativa, fecha, descripcion, id_categoria, id_jurisdiccion, id_organo_legislativo, link = resultado_consulta
            # Mostrar la información de la ley
            print("Número de normativa:", nro_normativa)
            print("El tipo de normativa es: ",id_tipo_normativa)
            print("Fecha:", fecha)
            print("Descripción:", descripcion)
            print("Categoría:", id_categoria)
            print("Jurisdicción:", id_jurisdiccion)
            print("Organo Legislativo:", id_organo_legislativo)
            print("Enlace:", link)
        #elif busqueda == 1:
        #    print("No se encontró ninguna ley con el número de normativa especificado.")
        else:
            print("No se encontró ninguna ley con la palabra especificada.")

            
#METODO PARA MODIFICAR NORMATIVA
    def modificarLey(nro_normativa, campo, nuevo_valor):
        datos = BBDD.Base_de_datos()
        datos.abrirBase()
        cursor = datos.cursor()

        # Crear la consulta SQL para actualizar el valor del campo en la tabla Ley
        consulta = "UPDATE Ley SET {} = ? WHERE nro_normativa = ?" .format(
            campo)
        valores = (nuevo_valor, nro_normativa)
        cursor.execute(consulta, valores)

        datos.confirmarCambios()
        cursor.close()
        datos.cerrarBase
    #cambiar palabras clave
    def cambiarPalabrasClaves(nro_normativa):
        datos = BBDD.Base_de_datos()
        datos.abrirBase()
        cursor = datos.cursor()
        
        consulta = "SELECT id_ley FROM Ley WHERE Nro_Normativa = ?"
        valor = nro_normativa,
        cursor.execute(consulta, valor)
        id_ley = cursor.fetchone()

        # Eliminar las palabras clave existentes para la normativa específica
        consulta_eliminar = "DELETE FROM Ley_por_palabra_clave WHERE id_ley = ?"
        valores_eliminar = (id_ley[0])
        cursor.execute(consulta_eliminar, (valores_eliminar,))

        # Nuevas palabras
        palabras_clave = input(
            "\nIngrese las palabras claves nuevas separadas por un espacio: ")
        lista_palabras = palabras_clave.split()

        for palabra in lista_palabras:
            consulta_palabra = "INSERT OR IGNORE INTO Palabra_clave (Palabra) VALUES (?)"
            valores_palabra = (palabra,)
            cursor.execute(consulta_palabra, valores_palabra)

        # Insertar las nuevas palabras clave para la normativa específica
        consulta_id_palabra = "SELECT id_palabra_clave FROM Palabra_clave WHERE Palabra = ?"
        consulta_vinculo = "INSERT INTO Ley_por_palabra_clave (id_ley, id_palabra_clave) VALUES (?, ?)"
        for palabra in lista_palabras:
            valores_id_palabra = (palabra,)
            cursor.execute(consulta_id_palabra, valores_id_palabra)
            resultado_id_palabra = cursor.fetchone()
            if resultado_id_palabra:
                # Extraer el valor de la tupla id_palabra_clave
                id_palabra_clave = resultado_id_palabra[0]
                # Utilizar los valores individuales
                valores_vinculo = (id_ley[0], id_palabra_clave)
                cursor.execute(consulta_vinculo, valores_vinculo)
        #Cerrar la base de datos y guardar los cambios
        datos.confirmarCambios()
        cursor.close()
        datos.cerrarBase


