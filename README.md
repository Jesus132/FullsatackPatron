# FullsatackPatron

Implementación
.Crear un entorno virtual para posteriormente instalar flask dentro de este, luego
creamos un archivo.py en donde importamos la clase Flask, render template y la
base de datos “SQLite”
.Se crea funcion def Base_Datos() Para abrir la conexión , a sú vez conectamos un
cursor como estructura de control para el recorrido de los registros del resultado
para la consulta en la base de datos.
.Se crea una función para mostrar de vista la ruta “/”, en la cual se establece la
conexión a una base de datos. Esto permite acceder a las columnas por nombre y
finalizando esta función va retornar un html
.Para listar el archivo json escribimos la ruta en la que se va a visualizar la el listado
JSON, en este caso “/api/v1/users/”.En el cual se creó un ciclo for para que itere el
número de veces tanto como datos existan en la base.
.Para la parte del frontend se clasificó en Templates ( Index.html) y static (css,js)
.En la implementación de docker primero creamos una carpeta de trabajo, luego
copiamos el contenido en el contenedor , instalamos los paquetes necesarios y
definimos la variable de entorno para iniciar el contenedor CMD ["python", "app.py"]

#Factory
Este patron de diseño creacion nos brinda la creacion de objetos en una SUPERCLASE 
que nos ayuda con las SUBCLASES alteren el tipo de objetos que retornaran y es por
eso que lo vimos optimo ya que nuestro programa proporciona 2 servicion usando
una base de datos.

<td><img src="https://refactoring.guru/images/patterns/diagrams/factory-method/structure.png"</th>

#API

<td><img src="https://github.com/Jesus132/FullsatackPatron/blob/master/api.jpg"</th>

#Tabla

<td><img src="https://github.com/Jesus132/FullsatackPatron/blob/master/tabla.jpg"</th>
