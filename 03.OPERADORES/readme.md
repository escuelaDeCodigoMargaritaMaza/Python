## ¿Qué son los operadores en Python?

Por lo general, las matemáticas implican alrededor de cuatro operaciones principales: suma, resta, multiplicación y división. Python es compatible con estos cuatro operadores y algunos otros. Exploremos los operadores más comunes que usarás en tus programas.

![image](https://user-images.githubusercontent.com/91554777/180104277-5d71b833-5f22-49f7-933a-46ed9a7803a5.png)


Veamos ahora qué podemos hacer con nuestros números usando los operadores por defecto. 



### Adición (Suma)

En python usamos ``+`` para indicar la adición. Usando ``+`` entre dos números los suma y proporciona el total.

```
answer = 30 + 12
print(answer)
```
*Salida: 42*

Los operadores se comportan igual cuando usan números literales (como ``42``) o variables.

### Sustracción (Resta)

Del mismo modo, Python utiliza ``-`` para la resta. El uso de ``-`` entre dos números resta los dos números y proporciona la diferencia.

```
difference = 30 - 12
print(difference)
```
*Salida: 18*

### Multiplicación

En Python ``*``, es el operador de multiplicación. Proporciona el producto de dos números:

```
product = 30 * 12
print(product)
```

*Salida: 360*

### División

Por último, se utiliza ``/`` para la división. Proporciona el cociente de dos números:

```
quotient = 30 / 12
print(quotient)
```

*Salida: 2.5*

Puede que tengas dudas sobre cómo funciona el operador de módulo, y cuál es la diferencia entre división y división entera.

El operador de módulo no hace otra cosa que devolvernos el resto de la división entre los dos operandos.

En el ejemplo, 7/2 sería 3, con 1 de resto, luego el módulo es 1.

La diferencia entre división y división entera no es otra que la que indica su nombre.

En la división el resultado que se devuelve es un número real, mientras que en la división entera el resultado que se devuelve es solo la parte entera. No obstante hay que tener en cuenta que si utilizamos dos operandos enteros, Python determinará que queremos que la variable resultado también sea un entero, por lo que el resultado de, por ejemplo, 3 / 2 y 3 // 2 sería el mismo: 1. Si quisiéramos obtener los decimales necesitaríamos que al menos uno de los operadores fuera un número real, bien indicando los decimales.

### Orden de funcionamiento (Jerarquía de Operaciones)

Python respeta el orden de operación para las matemáticas. El orden de operación dicta que las expresiones deben evaluarse en el siguiente orden:

* 1.- Paréntesis
* 2.- Exponentes
* 3.- Multiplicación y división
* 4.- Suma y resta

Observa cómo se evalúan los paréntesis antes de cualquier otra operación. Esto permite asegurarte de que el código se ejecuta de manera predecible y que su código sea más fácil de leer y mantener.

Como resultado, es una buena práctica usar paréntesis incluso si el orden de operación se evaluaría de la misma manera sin ellos. En las siguientes dos líneas de código, la segunda es más comprensible porque el paréntesis es una indicación clara de qué operación se realizará primero.

```
result_1 = 1032 + 26 * 2
result_2 = 1032 + (26 * 2)
```

*El resultado es el mismo en ambos casos - 1084*

---

# Boleanos.
Una variable o dato de tipo booleano sólo puede tener dos valores: True (cierto) y False (falso). Estos valores son especialmente importantes para las expresiones condicionales y los bucles, como veremos más adelante.

En realidad el tipo bool (el tipo de los booleanos) es una subclase del tipo int. Puede que esto no tenga mucho sentido para tí si no conoces los términos de la orientación a objetos, que veremos más adelante, aunque tampoco es nada importante. Estos son los distintos tipos de operadores con los que podemos trabajar con valores booleanos, los llamados operadores lógicos o condicionales.

![image](https://user-images.githubusercontent.com/91554777/180104542-459468e0-31d9-4725-9b3c-0aaab7868835.png)

# Operadores lógicos

Estos son operadores que actúan sobre las representaciones en binario de los operandores. Por ejemplo:

Si ves una operación como 3 & 2, lo que estás viendo es un and bit a bit entre los números binarios 11 y 10 (las representaciones en binario de 3 y 2).

El operador and (&), del inglés “y”, devuelve 1 si el primer bit operando es 1 y el segundo bit operando es 1. Se devuelve 0 en caso contrario.

El resultado de aplicar and bit a bit a 11 y 10 sería entonces el número binario 10, o lo que es lo mismo, 2 en decimal (el primer dígito es 1 para ambas cifras, mientras que el segundo es 1 sólo para una de ellas).

El operador or (|), del inglés “o”, devuelve 1 si el primer operando es 1 o el segundo operando es 1.

Para el resto de casos se devuelve 0. El operador xor u or exclusivo (^) devuelve 1 si uno de los operandos es 1 y el otro no lo es. El operador not (~), del inglés “no”, sirve para negar uno a uno cada bit; es decir, si el operando es 0, cambia a 1 y si es 1, cambia a 0.

![image](https://user-images.githubusercontent.com/91554777/180104723-80dc040b-22d4-42aa-b2f4-831439e5a011.png)

# Cadenas

Las cadenas no son más que texto encerrado entre comillas simples(‘cadena’)o dobles (“cadena”). Dentro de las comillas se pueden añadir caracteres especiales escapándolos con \, como \n, el carácter de nueva línea, o \t, el de tabulación.

También, es posible encerrar una cadena entre triples comillas (simples o dobles). De esta forma podremos escribir el texto en varias líneas, y al imprimir la cadena, se respetarán los saltos de línea que introdujimos

      triple = “““primera linea
      esto se vera en otra linea”””
      
También podriamos hacer esto mismo con el caracter especial \n

      triple = 'primera linea \n segunda linea'
      
Las cadenas también admiten operadores como +, que funciona realizando una concatenación de las cadenas utilizadas como operandos y *, en la que se repite la cadena tantas veces como lo indique el número utilizado como segundo operando.

      a = “uno”
      b = “dos”
      c = a + b
      print(c)
      
salida

    unodos

    c = a * 3 
    
salida

    unounouno

Fechas
Cuando estás creando programas, es probable que interactúes con las fechas. Una fecha en un programa generalmente significa tanto la fecha del calendario como la hora.

Una fecha se puede utilizar en varias aplicaciones, como estos ejemplos:

Archivo de copia de seguridad. Usar una fecha como parte del nombre de un archivo de copia de seguridad es una buena manera de indicar cuándo se realizó una copia de seguridad y cuándo debe realizarse nuevamente. Condición. Es posible que desee llevar una lógica específica cuando hay una fecha determinada. Métrica. Las fechas se utilizan para comprobar el rendimiento del código para, por ejemplo, medir el tiempo que se tarda en ejecutar una función. Para trabajar con una fecha, debe importar el módulo: date

    from datetime import date

A continuación, puede invocar las funciones con las que desea trabajar. Para obtener la fecha de hoy, puede llamar a la función: today()

    date.today()

Para mostrar la fecha en la consola, puede usar la función. La función toma muchos tipos de datos como entrada. Así es como puedes mostrar la fecha de hoy: print()

    print(date.today())

