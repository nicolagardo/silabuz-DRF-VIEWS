tarea ="""



Tarea
Implementar métodos PUT y POST dentro de:

Router customizado

Mixin de genericviewset

Luego de haber implementado ambas rutas y métodos, realizar el ingreso de
 5 usuarios.

Realizar el versionamiento de su proyecto.

Tarea opcional
Crear dos mixin sin hacer uso de Django.

Las clases deben contener lo siguiente.

Clase persona(base):

El constructor debe inicializar el nombre

Clase DictMixin:

Esta clase debe tener el método to_dict que convierta todos los atributos
 de la clase que lo usa a un diccionario.

Clase JsonMixin:

Esta clase debe tener el método to_json que convierta todos los atributos 
de la clase que lo usa a un json.

Clase Empleado:

La clase empleado hace uso de Persona, DictMixin y JsonMixin, el constructor
 debe inicializar el nombre, una lista de skills y un diccionario que contenga los datos de su familia, por ejemplo {"esposa": "María"}. Luego de crear la clase hacer uso de to_dict y to_json.
"""