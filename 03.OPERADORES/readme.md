## ¿Qué son los operadores en Python?

Por lo general, las matemáticas implican alrededor de cuatro operaciones principales: suma, resta, multiplicación y división. Python es compatible con estos cuatro operadores y algunos otros. Exploremos los operadores más comunes que usarás en tus programas.

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


