https://docs.google.com/presentation/d/17GdWdk_hdPkQEr9CPAkV1JcscTy22Z8I246_8AraV3A/edit?usp=sharing


## ¿Qué es la programación orientada a objetos en Python?
La programación orientada a objetos (POO) es un paradigma de programación en el que podemos pensar en problemas complejos como objetos.

Un paradigma es una teoría que proporciona la base para resolver problemas.

Así que cuando hablamos de POO, nos referimos a un conjunto de conceptos y patrones que utilizamos para resolver problemas con objetos.

Un objeto en Python es una colección única de datos (atributos) y comportamiento (métodos). Puedes pensar en los objetos como cosas reales que te rodean:
  
Los datos (atributos) son siempre sustantivos, mientras que los comportamientos (método) son siempre verbos.
  
Esta compartimentación es el concepto central de la programación orientada a objetos. Se construyen objetos que almacenan datos y contienen tipos específicos de funcionalidad.
  
## ¿Por qué utilizamos la programación orientada a objetos en Python?

  La POO permite crear software seguro y fiable. Muchos marcos y bibliotecas de Python utilizan este paradigma para construir su código base. Algunos ejemplos son Django, Kivy, pandas, NumPy y TensorFlow.

Veamos las principales ventajas de usar OOP en Python.

Ventajas de la POO de Python
Las siguientes razones te harán optar por utilizar la programación orientada a objetos en Python.

Todos los lenguajes de programación modernos utilizan la POO
Este paradigma es independiente del lenguaje. Si aprendes POO en Python, podrás utilizarlo en lo siguiente:

* Java
* PHP 
* Ruby
* Javascript
* C#
* Kotlin
  
Todos estos lenguajes están orientados a objetos de forma nativa o incluyen opciones para la funcionalidad orientada a objetos. Si quieres aprender cualquiera de ellos después de Python, será más fácil: encontrarás muchas similitudes entre los lenguajes que trabajan con objetos.

#### La POO te permite codificar más rápido
  Codificar más rápido no significa escribir menos líneas de código. Significa que puedes implementar más funciones en menos tiempo sin comprometer la estabilidad de un proyecto.

La programación orientada a objetos te permite reutilizar el código mediante la implementación de la abstracción. Este principio hace que tu código sea más conciso y legible.

Como ya sabrás, los programadores pasan mucho más tiempo leyendo código que escribiéndolo. Es la razón por la que la legibilidad es siempre más importante que sacar características lo más rápido posible.
  
#### La OOP te ayuda a evitar el código espagueti

La programación orientada a objetos nos da la posibilidad de comprimir toda la lógica en objetos, evitando así largos trozos de if’s anidados.
  
#### La POO mejora el análisis de cualquier situación
  
## Programación estructurada frente a la programación orientada a objetos
La programación estructurada es el paradigma es la forma más sencilla de construir un pequeño programa.

Se trata de ejecutar un programa Python de forma secuencial. Eso significa que le das al ordenador una lista de tareas y luego las ejecutas de arriba a abajo.

  ![image](https://user-images.githubusercontent.com/91554777/177200456-2f43b1f6-3710-4077-b286-be4de9e8558f.png)
  
* Ninguno de los dos paradigmas es perfecto (la POO puede resultar abrumadora en proyectos sencillos).
* Estas son solo dos formas de resolver un problema; hay otras por ahí.
* La POO se utiliza en grandes bases de código, mientras que la programación estructurada es principalmente para proyectos sencillos.

En Python, todo es un objeto.

Recuerda la definición de objeto: Un objeto en Python es una única colección de datos (atributos) y comportamiento (métodos).

Esto coincide con cualquier tipo de datos en Python.

Una cadena es una colección de datos (caracteres) y comportamientos (upper(), lower(), etc.). Lo mismo ocurre con los enteros, los flotantes, los booleanos, las listas y los diccionarios.
  
Una clase es como una plantilla. Te permite crear objetos personalizados basados en los atributos y métodos que definas.
  
  ![image](https://user-images.githubusercontent.com/91554777/177216427-c5ba2d4f-f8f0-4b37-863d-ba7f572f662d.png)
  
Para definir una clase en Python, se utiliza la palabra clave class, seguida de su nombre.
  
Nota: En Python, utilizamos la convención de nombres en mayúsculas para nombrar las clases.
 
El método __init__() también se llama «constructor». Es llamado por Python cada vez que instanciamos un objeto.
  
### 1. Abstracción
  
La abstracción oculta al usuario la funcionalidad interna de una aplicación. El usuario puede ser el cliente final u otros desarrolladores.


Podemos encontrar abstracción en nuestra vida cotidiana. Por ejemplo, sabes cómo usar tu teléfono, pero probablemente no sepas exactamente lo que ocurre dentro de él cada vez que abres una aplicación.

### 2. Herencia
  
La herencia nos permite definir múltiples subclases a partir de una clase ya definida.
  
Puedes pensar en ello como el concepto de herencia genética en la vida real. Los hijos (subclases) son el resultado de la herencia entre dos padres (superclases). Heredan todas las características físicas (atributos) y algunos comportamientos comunes (métodos).
La herencia nos permite definir múltiples subclases a partir de una clase ya definida.

  
### 3. Polimorfismo
El polimorfismo nos permite modificar ligeramente los métodos y atributos de las subclases previamente definidas en la superclase.

El significado literal es «muchas formas«. Esto se debe a que construimos métodos con el mismo nombre pero con diferente funcionalidad.
  
### 4. Encapsulación
La encapsulación es el proceso en el que protegemos la integridad interna de los datos en una clase.
  
Existen métodos especiales llamados getters y setters que nos permiten acceder a atributos y métodos únicos.

Imaginemos una clase Humana que tiene un único atributo llamado _altura. Este atributo solo se puede modificar dentro de ciertas restricciones (es casi imposible ser más alto que 3 metros).
  
  
Se define como el “ocultamiento del estado” osea de “los datos miembros de un objeto”. Hablamos de ocultar los datos de atributos o métodos, más específicamente de protegerlos para que solo puedan ser cambiados mediante “operaciones definidas” para ello. Esto nos asegura por ejemplo que “no podremos modificar un atributo si no es a través de un método que hallamos creado específicamente para ello” y aquí es donde nacen los famosos “Getter, Setter, Deleter”

Anteriormente creamos clases con sus atributos y métodos públicos, es decir, que son accesibles desde su instancia. Basta con crear un objeto a partir de esa clase y podremos acceder y modificar libremente sus atributos. Y no solo desde su instancia sino también desde otra clase que herede de la anterior, por lo que un atributo que almacena información sensible puede ser modificado fácilmente.

      class Usuario ():
          def __init__(self, nombre, folio):
              self.nombre = nombre
              self.folio = folio

      Usuario1 = Usuario ("Roberto", "12345")
      print (Usuario1.nombre, Usuario1.folio)
      
  salida
 
      (‘Roberto’, ‘12345’)

* Atributos protegidos en Python (“_”)

      class Usuario ():
          def __init__(self, nombre, folio):
              self.nombre = nombre
              self._folio = folio

      Usuario1 = Usuario ("Roberto", "12345")
      print (Usuario1.nombre, Usuario1._folio)
      
 salida
 
      (‘Roberto’, ‘12345’)
      
Como ves el atributo clave esta precedido por un guión bajo, lo que indica que es un atributo protegido. Lo cual establece que solo puede ser accedido por esa clase y sus sub-clases, es decir, aquellas que hereden de la clase padre. Se suele ver muy a menudo como una buena practica para atributos o métodos de uso interno y también para evitar la colisión de los mismos nombres de métodos o atributos causado por herencia. 

* Atributos privados en Python (“__”)

En el caso de un atributo privado estamos indicando que este solo podrá ser accedido o modificado si se especifica la clase precedida por un guión bajo seguida del atributo precedido por doble guión bajo.

     class Usuario ():
              def __init__(self, nombre, clave):
                  self.nombre = nombre
                  self.__folio = folio

          Usuario1 = Usuario ("Roberto", "12345")
          print (Usuario1.nombre, Usuario1.__folio)
      
 salida
 
      AttributeError: ‘usuario’ object has no attribute ‘__folio’
      
La forma correcta de acceder a el sería especificando primero la clase a la que pertenece de la siguiente manera:

      class Usuario ():
          def __init__(self, nombre, folio):
              self.nombre = nombre
              self.__folio = folio

      Usuario1 = Usuario ("Roberto", "12345")
      print (Usuario1.nombre, Usuario1._Usuario__folio)
      
salida

      (‘Roberto’, ‘12345’)
      
      
Podemos acceder desde la misma clase pero desde fuera

          class Usuario (object):
              def __init__(self, nombre, folio):
                  self.__nombre = nombre
                  self.__folio = folio

              def imprimir(self):
                return self.__folio + ' ' + self.__nombre

              def pedir(self,nombreFolio):
                self.__nombre, self.__folio = nombreFolio.split(' ')

          Usuario1 = Usuario ("Roberto", "12345")
          Usuario1.imprimir()
          Usuario1.pedir='juan d5f4f'
          print(Usuario1.pedir)

Como ves podemos acceder igualmente a un atributo por más que sea privado y modificarlo de la misma manera. Pero no es lo que se “considera correcto”. Por lo que para ello si deseamos implementar métodos que nos permitan modificar estos atributos de la forma que se suele hacer en otros lenguajes donde se aplica “encapsulamiento” podemos hacerlo utilizando Getter, Setter, Deleter mediante el uso del decorador @Property

En python dentro de las clases podríamos decir que todo son atributos, incluso los métodos podríamos definirlos como “atributos llamables” y las propiedades “atributos personalizables”. Por ende ahora:

Las propiedades son atributos que “manejamos” mediante Getter, Setter y Deleter.

“Atributos manejables” que nos permiten invocar código personalizado al ser creados, modificados o eliminados.

### @Property en python

La función integrada property() nos permitirá interceptar la escritura, lectura, borrado de los atributos y ademas nos permiten incorporar una documentación sobre los mismos. La sintaxis para invocarla es la siguiente:

          @property

Si nosotros no pasamos alguno de los parámetros su valor por defecto sera None.

Getter: Se encargará de interceptar la lectura del atributo. (get = obtener)

Setter : Se encarga de interceptar cuando se escriba. (set = definir o escribir)

Deleter : Se encarga de interceptar cuando es borrado. (delete = borrar)

doc :  Recibirá una cadena para documentar el atributo. (doc = documentación)


