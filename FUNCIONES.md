## Funciones

Una función es un fragmento de código con un nombre asociado que realiza una
serie de tareas y devuelve un valor. A los fragmentos de código que tienen un
nombre asociado y no devuelven valores se les suele llamar procedimientos. En
Python no existen los procedimientos, ya que cuando el programador no
especifica un valor de retorno la función devuelve el valor None (nada),
equivalente al null de Java. Además de ayudarnos a programar y depurar
dividiendo el programa en partes las funciones también permiten reutilizar
código.En Python las funciones se declaran de la siguiente forma:

    def mi_funcion(param1, param2):

    print param1
    print param2

Es decir, la palabra clave def seguida del nombre de la función y entre paréntesis
los argumentos separados por comas. A continuación, en otra línea, indentado
y después de los dos puntos tendríamos las líneas de código que conforman el
código a ejecutar por la función.

También podemos encontrarnos con una cadena de texto como primera línea
del cuerpo de la función. Estas cadenas se conocen con el nombre de docstring
(cadena de documentación) y sirven, como su nombre indica, a modo de
documentación de la función.

    def mi_funcion(param1, param2):
    “““Esta función imprime los dos valores pasados
    como parámetros”””
    print param1
    print param2

Esto es lo que imprime el operador ? de iPython o la función help del lenguaje
para proporcionar una ayuda sobre el uso y utilidad de las funciones. Todos los
objetos pueden tener docstrings, no solo las funciones, como veremos más
adelante.
