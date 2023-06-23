
import BBDD

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

    def busquedaPalabraClave(self):
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
        valor = self.palabras_clave,
        cursor.execute (consulta , valor)
        resultado_consulta = cursor.fetchone()
        leyes.imprimirEnPantalla (resultado_consulta)

        base_de_datos.confirmarCambios()
        cursor.close()
        base_de_datos.cerrarBase


        
    def imprimirEnPantalla(self, resultado_consulta):   
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
        elif busqueda == 1:
            print("No se encontró ninguna ley con el número de normativa especificado.")
        else:
            print("No se encontró ninguna ley con la palabra especificada.")



            def busquedaNroNormativa (self):
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
        valor = self.nro_normativa,
        cursor.execute (consulta , valor)
        resultado_consulta = cursor.fetchone()
        leyes.imprimirEnPantalla (resultado_consulta)

        base_de_datos.confirmarCambios()
        cursor.close()
        base_de_datos.cerrarBase