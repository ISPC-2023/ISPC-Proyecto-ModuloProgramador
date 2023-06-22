import sqlite3

class Base_de_datos():
            
    def abrirBase(self):
        # Conectarse a la base de datos
        self.conexion = sqlite3.connect("leyes_vigentes.db")
        return self.conexion

    def cursor(self):
        # Obtener la conexión a la base de datos
        self.base = self.abrirBase()
        # Crear un cursor para ejecutar consultas SQL
        self.cursor = self.base.cursor()
        return self.cursor

    def confirmarCambios(self):
        # Confirmar los cambios en la base de datos
        self.base.commit()

    def cerrarBase(self):
        # Cerrar el cursor y la conexión a la base de datos
        self.cursor.close()
        self.base.close()