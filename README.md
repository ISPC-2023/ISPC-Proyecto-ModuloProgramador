# :mortar_board: ISPC
## :newspaper: Proyecto
### :computer: ModuloProgramador 
Grupo creado para trabajar contenidos dictados en el Módulo Programador.

*Comisión 3*.


#### Integrantes del grupo

- :girl: Ponce María Elena Haydee - [@hechizera10](https://github.com/hechizera10) - ponce.me@hotmail.com
- :woman: Analia Anahi Pellicer Palacios - [@AnaliaPellicer](https://github.com/AnaliaPellicer) - analiapellicer86@gmail.com
- :princess: Maria celeste Trujillo - [@CeleTru](https://github.com/CeleTru) - celespam@yahoo.com.ar
- :boy: Gaston Alejandro Sanchez - [@GastonAlejandroSanchez](https://github.com/GastonAlejandroSanchez) - gastonalejandrosanchez@outlook.com
- :man: Franco Daniel Vega - [@Francovega](https://github.com/Francovega) - francovega1234@gmail.com
- :man_with_gua_pi_mao: Raúl Cristian Roberto Sasinka - [@Luarrr](https://github.com/Luarrr) - Sasinkaa2011@gmail.com
- :woman: Nathalie Pereyra - [@nathyjanet](https://github.com/nathyjanet) - nathaliejanetpereyra@gmail.com

### :computer: Descripción
El presente software permite:
- Realizar consultas a los usuarios de las distintas leyes vigentes según a) Número de ley y b) Palabras claves.
- Mostrar los datos mínimos de la normativa, como así también una breve descripción de sus contenidos en un párrafo de no más de cinco renglones.
- Agregar nuevas normativas según los requerimientos mínimos.
- Borrar Normativas existentes según su número.
- Actualizar campos de las normativas, sea de forma indiviual o total.

El programa está compuesto de:
- 2 Clases principales: *Ley* y *Base_de_datos*
  - La clase *Ley*, se define en el archivo [*CRUD.py*](/CRUD.py) y posee los métodos:
    - *agregarLey()*,
    - *cambiarPalabrasClaves()*,
    - *modificarLey()*,
    - *borrarLey()*,
    - *busquedaNroNormativa()*,
    - *busquedaPalabraClave()*,
    - *imprimirEnPantalla()*.

  - La clase *Base_de_datos*, se define en el archivo [*BBDD.py*](/BBDD.py) y posee los métodos:
    - *abrirBase()*,
    - *cursor()*,
    - *confirmarCambios()*,
    - *cerrarBase()*.

- Un archivo [*menuUpdate.py*](menuUpdate.py) que aloja el menú de opciones del método UPDATE y ejecuta su procesamiento.
- Un archivo [*menuPrincipal.py*](menuPrincipal.py) que inicia el programa y permite acceder a todos las funcionalidades.
- Un archivo [*ui.py*](ui.py) que permite personalizar fácilmente los mensajes reutilizables de la interfaz de usuario.
- La tabla [*leyes_vigentes.db*](leyes_vigentes.db) corresponde a la Base de Datos con la que está trabajando el programa.
- En la carpeta [*Tabla de Referencia Leyes*](https://github.com/ISPC-2023/ISPC-Proyecto-ModuloProgramador/tree/76c6aaed17c748fbb2fbe31cdbb777280f85ce83/Evidencia-Tabla%20de%20Referencia%20Leyes), encontrará los datos de las leyes cargadas.
- En la carpeta [*DiagramasBBDD*](Evidencia_DiagramasBBDD), encontrará los diagramas DER y el modelo ER con el que se construyó la Base de Datos.
- En la carpeta [*Consigna*](Consigna), se encuentra el documento de base que motivó el desarrollo.

### :computer: Ejecución
- Para ejecutar el programa debe correrse el archivo
  >[*menuPrincipal.py*](/menuPrincipal.py)**

  
**Es de suma importancia abrir el IDE para su ejecución desde la carpeta que tiene todos los archivos, dado que la base de datos es local. Si se corre de forma autónoma el archivo menuPrincipal, sin ejecutarlo desde la carpeta con su dependencias se producirá un error "no such table Ley". Este error se corrige realizando la ejecución como ha sido indicado.

#### *2023*






