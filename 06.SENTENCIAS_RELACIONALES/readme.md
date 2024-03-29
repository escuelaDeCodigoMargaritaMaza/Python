# Bucles

Mientras que los condicionales nos permiten ejecutar distintos fragmentos de
código dependiendo de ciertas condiciones, los bucles nos permiten ejecutar un
mismo fragmento de código un cierto número de veces, mientras se cumpla una
determinada condición.

## while
El bucle while (mientras) ejecuta un fragmento de código mientras se
cumpla una condición.

    edad = 0
    while edad < 18:
        edad = edad + 1
        print “Felicidades, tienes “ + str(edad)

La variable edad comienza valiendo 0. Como la condición de que edad es menor
que 18 es cierta (0 es menor que 18), se entra en el bucle.
Se aumenta edad en 1 y se imprime el mensaje informando de que el usuario ha
cumplido un año. Recuerda que el operador + para las cadenas funciona
concatenando ambas cadenas. Es necesario utilizar la función str (de string,
cadena) para crear una cadena a partir del número, dado que no podemos
concatenar números y cadenas.

Ahora se vuelve a evaluar la condición, y 1 sigue siendo menor que 18, por lo
que se vuelve a ejecutar el código que aumenta la edad en un año e imprime la
edad en la pantalla.

El bucle continuará ejecutándose hasta que edad sea igual a 18, momento en el
cual la condición dejará de cumplirse y el programa continuaría ejecutando las
instrucciones siguientes al bucle.

## for ... in
A los que tenga experiencia previa con según que lenguajes este bucle nos va
a sorprender gratamente. En Python for se utiliza como una forma genérica de
iterar sobre una secuencia. Y como tal intenta facilitar su uso para este fin.
Este es el aspecto de un bucle
for en Python:

    secuencia = [“uno”, “dos”, “tres”]
    for elemento in secuencia:
        print elemento

Como hemos dicho los for se utilizan en Python para recorrer secuencias, por lo
que vamos a utilizar un tipo secuencia, como es la lista, para nuestro ejemplo.
Leamos la cabecera del bucle como si de lenguaje natural se tratara: “para cada
elemento en secuencia”. Y esto es exactamente lo que hace el bucle: para cada
elemento que tengamos en la secuencia, ejecuta estas líneas de código. Lo que
hace la cabecera del bucle es obtener el siguiente elemento de la secuencia y
almacenarlo en una variable de nombre elemento. Por esta razón en la primera
iteración del bucle elemento valdrá “uno”, en la segunda “dos”, y en la tercera
“tres”.


# Funciones

El uso de una función de Python es el primer paso para codificar después de las estructuras de datos y los condicionales básicos. Las funciones permiten la reutilización, lo que evita la duplicación de código. Cuando los proyectos reutilizan código con funciones, se vuelven más legibles y fáciles de mantener.

Las funciones son el siguiente paso después de haber aprendido los conceptos básicos de programación de Python. En su forma más sencilla, una función contiene código que siempre devuelve un valor (o valores). En algunos casos, una función también tiene entradas opcionales u obligatorias.

Una función es un fragmento de código con un nombre asociado que realiza una
serie de tareas y devuelve un valor. A los fragmentos de código que tienen un
nombre asociado y no devuelven valores se les suele llamar procedimientos. En
Python no existen los procedimientos, ya que cuando el programador no
especifica un valor de retorno la función devuelve el valor None (nada),
equivalente al null de Java. Además de ayudarnos a programar y depurar
dividiendo el programa en partes las funciones también permiten reutilizar
código.

### Funciones sin argumentos
Para crear una función, utilizamos la palabra clave `def`, seguida de un nombre, paréntesis y, después, del cuerpo con el código de función:

```
# Defino mi función
def partes():
    print('cuerpo, estructura y forma')
    return
```

En este caso, partes es el nombre de la función. Ese nombre va seguido de paréntesis vacíos, que indican que no se necesitan argumentos. El último es el código, con sangría de cuatro espacios. Para trabajar con la función, debes llamarla por su nombre usando paréntesis:


```
# Llamo a mi función

>>> partes()
'cuerpo, estructura y forma'
```


### Argumentos opcionales y requeridos
En Python, varias funciones integradas requieren argumentos. Algunas funciones integradas hacen que los argumentos sean opcionales. Las funciones integradas están disponibles de inmediato, por lo que no es necesario importarlas explícitamente.

## Uso de argumentos en una función de Python

Ahora que sabes cómo crear una función sin entradas, el paso siguiente es crear funciones que requieran un argumento. El uso de argumentos hace que las funciones sean más flexibles, ya que pueden hacer más y condicionalizar lo que hacen.

### Exigencia de un argumento
Si vas a manejar un coche, una función sin entradas obligatorias es como un coche con un botón que le indique la hora. Si presionas el botón, una voz computarizada te indicará la hora. Pero una entrada necesaria puede ser un destino para calcular la distancia del viaje. Las entradas obligatorias se denominan *argumentos* para la función.

Para requerir un argumento, agrégalo entre paréntesis:

```
def distancia(destino):
    if destino == 'CentroAzcapotzalco':
        return '1.5'
    else:
        return 'No se puede calcular el destino'
```
Intenta llamar a la función distancia() sin argumento alguno:

```
>>> distancia()
Traceback (most recent call last):
  File '<stdin>', line 1, in <module>
TypeError: distancia() missing 1 required positional argument: 'destino'
```

Python genera `TypeError` con un mensaje de error que indica que la función requiere un argumento denominado destino. Si se pide al equipo del coche que calcule la distancia del viaje con un destino, debes solicitar que un destino es un requisito. El código de ejemplo tiene dos rutas de acceso para una respuesta, una para CentoAzcapotzalco y la otra para cualquier otra cosa.

```
>>> distanca('CentroAzcapotzalco')
'15'
```

Dado que hay una condición catch-all, intenta usar cualquier otra cadena como destino para comprobar ese comportamiento:

```
>>> distancia('Tacuba')
'No se puede calcular el destino'
```
### Varios argumentos necesarios
Para usar varios argumentos, debes separarlos con una coma. Vamos a crear una función que pueda calcular cuántas horas se tardarán en llegar a un destino, dadas la distancia y una velocidad constante:

```
def horas_para_llegar(distancia, velocidad):
    tiempo = distancia/velocidad
    return tiempo

```

Ahora usamos la distancia entre PILARES y un punto a 230 km, para calcular cuántas horas tardaría en llegar con una velocidad de 75 km hora:

```
>>> horas_para_llegar(230, 75)
```



### Funciones como argumentos
Puedes usar el valor de la función horas_para_llegar() y asignarlo a una variable y, después, pasarlo a round() (una función integrada que redondea al número entero más cercano) para obtener un número entero:

```
>>> total_horas = horas_para_llegar(230, 75)
>>> round(total_horas)

```
Pero un patrón útil es pasar funciones a otras funciones en lugar de asignar el valor devuelto:

```
>>> round(minutos_para_llegar(23, 75))

```
**Sugerencia**

Aunque pasar funciones directamente a otras funciones como entrada es útil, existe la posibilidad de que se reduzca la legibilidad. Este patrón es especialmente problemático cuando las funciones requieren muchos argumentos.


## Uso de argumentos de palabra clave en Python

Los argumentos opcionales requieren un valor predeterminado asignado a ellos. Estos argumentos con nombre se denominan *argumentos de palabra clave*. Los valores del argumento de palabra clave deben definirse en las propias funciones. Cuando se llama a una función definida con argumentos de palabra clave, no es necesario usarlos en absoluto.

 Vamos a crear una función que devuelva la hora estimada de llegada considerando tardaremos 12 horas de viaje:

```
from datetime import timedelta, datetime

def tiempo_arribo(horas=12):
    ahora = datetime.now()
    arribo = ahora + timedelta(hours=horas)
    return arribo.strftime('Arribo: %A %d de %B %H:%M') #strftime método que nos permite definir la fecha en el formato que necesitemos
```

La función usa el módulo `datetime` para definir la hora actual. Usa `timedelta` para permitir la operación de suma que da como resultado un objeto de hora nuevo. Después de calcular ese resultado, devuelve la estimación `arribo` con formato de cadena. Intentando llamarla sin algún argumento:

```
>>> tiempo_arribo()
'Arribo: Saturday 16:42'
```

Pequeño tutorial para date en python https://codigofacilito.com/articulos/fechas-python


### Combinación de argumentos y argumentos de palabra clave

A veces, una función necesita una combinación de argumentos de palabra clave y argumentos. En Python, esta combinación sigue un orden específico. Los argumentos siempre se declaran primero, seguidos de argumentos de palabra clave.

Actualizando la función `tiempo_arribo()` para que tome un argumento necesario, que es el nombre del destino:

```
from datetime import timedelta, datetime

def tiempo_arribo(destino, horas=12):
    ahora = datetime.now()
    destino1 = ahora + timedelta(hours=horas)
    return destino1.strftime(f'{destino} Arribo: %A %H:%M')
```
Dado que hemos agregado un argumento necesario, ya no es posible llamar a la función sin ningún argumento:

Usamos 'Puebla' como valor para destino a fin de evitar el error:

```
>>> tiempo_arribo('Puebla')
'Puebla Arribo: Saturday 16:54'
```

### Otro ejemplo
```
def escribe_media():
    media = (a + b) / 2
    print(f"La media de {a} y {b} es: {media}")
    return

a = 3
b = 5
escribe_media()
print("Programa terminado")
```
Salida

    La media de 3 y 5 es: 4.0
    Programa terminado
    
* En la primera instrucción se crea la variable "a".
* En la segunda instrucción se crea la variable "b".
* A continuación se realiza la llamada a la función.
* Se ejecuta la primera instrucción de la función, que calcula la media de las variables "a" y "b" que, como no se les asigna valor en la función, Python considera variables globales.
* Se escribe el resultado de la operación.
* La instrucción return indica el final de la función y continúa la ejecución del programa tras la llamada a la función.
* Se ejecuta la última instrucción del programa y el programa termina.

El problema de una función de este tipo es que es muy difícil de reutilizar en otros programas o incluso en el mismo programa, ya que sólo es capaz de hacer la media de las variables "a" y "b". Si en el programa no se utilizan esos nombres de variables, la función no funcionaría.

Para evitar ese problema, las funciones admiten argumentos, es decir, permiten que se les envíen valores con los que trabajar. De esa manera, las funciones se pueden reutilizar más fácilmente, como muestra el ejemplo siguiente:

```
def escribe_media(x, y):
    media = (x + y) / 2
    print(f"La media de {x} y {y} es: {media}")
    return

a = 3
b = 5
escribe_media(a, b)
print("Programa terminado")
```
Salida

        La media de 3 y 5 es: 4.0
        Programa terminado

* En la primera instrucción se crea la variable "a".
* En la segunda instrucción se crea la variable "b".
* A continuación se realiza la llamada a la función. De acuerdo con la definición de la función, se deben enviar dos argumentos. En este caso, se envían las variables "a" y "b".
* Se ejecuta la primera instrucción de la función, que calcula la media de los argumentos "x" e "y". Los argumentos cogen su valor de los la llamada de la función. En esta caso la variable "x" toma su valor de la variable "a" y la variable "y" lo hace de "b".
* Se escribe el resultado de la operación.
* La instrucción return indica el final de la función y continúa la ejecución del programa tras la llamada a la función.
* Se ejecuta la última instrucción del programa y el programa termina.

Esta función puede ser utilizada con más flexibilidad que la del ejemplo anterior, puesto que el programador puede elegir a qué valores aplicar la función.

Pero esta función tiene todavía un inconveniente. Como las variables locales de una función son inaccesibles desde los niveles superiores, el programa principal no puede utilizar la variable "media" calculada por la función y tiene que ser la función la que escriba el valor. Pero eso complica la reutilización de la función, porque aunque es probable que en otro programa nos interese una función que calcule la media, es más difícil que nos interese que escriba el valor nada más calcularlo.

Para evitar ese problema, las funciones pueden devolver valores, es decir, pueden enviar valores al programa o función de nivel superior. De esa manera, las funciones se pueden reutilizar más fácilmente, como muestra el ejemplo siguiente:

```
def calcula_media(x, y):
    resultado = (x + y) / 2
    return resultado

a = 3
b = 5
media = calcula_media(a, b)
print(f"La media de {a} y {b} es: {media}")
print("Programa terminado")
```
Salida

        La media de 3 y 5 es: 4.0
        Programa terminado
        
* La tercera instrucción guarda en la variable "media" el valor que devuelve la función calcula_media(). Pero en primer lugar se ejecuta la llamada a la función. De acuerdo con la definición de la función, se deben enviar dos argumentos. En este caso, se envían las variables "a" y "b".
* Se ejecuta la primera instrucción de la función, que calcula la media de los argumentos "x" e "y". Los argumentos cogen su valor de los la llamada de la función. En esta caso la variable "x" toma su valor de la variable "a" y la variable "y" lo hace de "b".
* La instrucción return indica el final de la función pero también el valor que devuelve la función. La ejecución del programa continúa tras la llamada a la función.
* El valor devuelto por la función se guarda en la variable "media"
* Se escribe el resultado de la operación.
* Se ejecuta la última instrucción del programa y el programa termina.

Esta función puede ser utilizada con más flexibilidad que la del ejemplo anterior, puesto que el programador puede elegir qué hacer con el valor calculado por la función.

Pero esta función tiene todavía un inconveniente y es que sólo calcula la media de dos valores. Sería más interesante que la función calculara la media de cualquier cantidad de valores.

Para evitar ese problema, las funciones pueden admitir una cantidad indeterminada de valores, como muestra el ejemplo siguiente:

```
def calcula_media(*args):
    total = 0
    for i in args:
        total += i
    resultado = total / len(args)
    return resultado

a, b, c = 3, 5, 10
media = calcula_media(a, b, c)
print(f"La media de {a}, {b} y {c} es: {media}")
print("Programa terminado")
```
Salida

        La media de 3 y 5 es: 4.0
        Programa terminado
        
* En la primera instrucción se crean las variables "a", "b" y "c".
* La segunda instrucción guarda en la variable "media" el valor que devuelve la función calcula_media(). Pero en primer lugar se ejecuta la llamada a la función. De acuerdo con la definición de la función, se puede enviar cualquier número de argumentos. En este caso, se envían las variables "a", "b" y "c".
* Se ejecuta la primera instrucción de la función. Para calcular la media, el programa va a sumar todos los argumentos recibidos y dividir por el número de argumentos recibidos. Para calcular el total, se utiliza una variable auxiliar llamada "total" cuyo valor inicial es 0.
* El bucle se ejecutará tantas veces como argumentos se hayan recibido, puesto que args es una tupla con tantos elementos como como argumentos.
* Finalmente se divide el total por el número de elementos.
* La instrucción return indica el final de la función pero también el valor que devuelve la función. La ejecución del programa continúa tras la llamada a la función.
* El valor devuelto por la función se guarda en la variable "media".
* Se escribe el resultado de la operación.
* Se ejecuta la última instrucción del programa y el programa termina.


____________________________________________________________________________________________________________________________________________________________________

## Uso de argumentos de variable en Python

En Python, puedes usar cualquier número de argumentos de palabra clave y argumentos sin necesidad de declarar cada uno de ellos. Esta capacidad es útil cuando una función puede obtener un número desconocido de entradas.

### Argumentos de variable
Los argumentos en las funciones son necesarios. Pero cuando se usan argumentos de variable, la función permite pasar cualquier número de argumentos (incluido `0`). La sintaxis para usar argumentos de variable es agregar un asterisco único como prefijo (`*`) antes del nombre del argumento.

La función siguiente imprime los argumentos recibidos:

```
def variable_length(*args):
    print(args)
```

En este caso, `*args` indica a la función que acepta cualquier número de argumentos (incluido `0`). En la función, `args` ahora está disponible como la variable que contiene todos los argumentos como una tupla. Pruebe la función pasando cualquier número o tipo de argumentos:

```
>>> variable_length()
()
>>> variable_length('one', 'two')
('one', 'two')
>>> variable_length(None)
(None,)
```
Como puedes ver, no hay ninguna restricción en el número o tipo de argumentos que se pasan.

Un cohete realiza varios pasos antes de un lanzamiento. En función de las tareas o retrasos, estos pasos pueden tardar más de lo previsto. Vamos a crear una función de longitud variable que pueda calcular cuántos minutos quedan hasta el inicio, dado el tiempo que va a tardar cada paso:

```
def secuencia(*args):
    total_minutos = sum(args)
    if total_minutos < 60:
        return f'Tiempo total para despegue {total_minutos} minutos'
    else:
        return f'Tiempo total para despegue {total_minutos/60} horas'
```
Probamos la función pasando cualquier número de minutos:

```
>>> secuencia(4, 14, 18)

```


https://colab.research.google.com/drive/1nxCF0Ke5nzl2EwNhBZoo5YepihKPVu7A
