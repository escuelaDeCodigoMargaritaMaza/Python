Los valores booleanos son además el resultado de expresiones que utilizan operadores relacionales (comparaciones entre valores):

Operador ==
El operador == evalúa que los valores sean iguales para varios tipos de datos.

![image](https://user-images.githubusercontent.com/91554777/180248792-2cdff8f1-b21c-4772-a559-a48395f12b4e.png)

Operador !=
El operador != evalúa si los valores son distintos.

![image](https://user-images.githubusercontent.com/91554777/180248840-128c3d77-eb5b-4322-9523-2d70bd40ac22.png)

Operador <
El operador < evalúa si el valor del lado izquierdo es menor que el valor del lado

![image](https://user-images.githubusercontent.com/91554777/180248878-a1f14b5d-18a2-4611-b15b-878b783b32c3.png)

Operador >
El operador > evalúa si el valor del lado izquierdo es mayor que el valor del lado derecho.

![image](https://user-images.githubusercontent.com/91554777/180248961-95fb6351-7f8b-417d-bf08-b0508ff7d4ce.png)

Operador <=
El operador <= evalúa si el valor del lado izquierdo es menor o igual que el valor del lado derecho.

![image](https://user-images.githubusercontent.com/91554777/180249004-0c10b79a-e1fa-46ba-92d8-f8c2ef907d13.png)

Operador >= El operador >= evalúa si el valor del lado izquierdo es mayor o igual que el valor del lado derecho.

![image](https://user-images.githubusercontent.com/91554777/180249044-e56ad6b0-9359-4af9-bfbf-89a79adcee0b.png)

Si un programa no fuera más que una lista de órdenes a ejecutar de forma secuencial, una por una, no tendría mucha utilidad. Los condicionales nos permiten comprobar condiciones y hacer que nuestro programa se comporte de una forma u otra, que ejecute un fragmento de código u otro, dependiendo de esta condición.

Aquí es donde cobran su importancia el tipo booleano y los operadores lógicos y relacionales.

# If
La forma más simple de un estamento condicional es un if (del inglés si) seguido de la condición a evaluar, dos puntos (:) y en la siguiente línea e indentado, el código a ejecutar en caso de que se cumpla dicha condición.

      fav = “mundogeek.net"
      if fav == “mundogeek.net”:
      print (“Tienes buen gusto!”)
      
 # if ... else
      
Vamos a ver ahora un condicional algo más complicado. ¿Qué haríamos si quisiéramos que se ejecutaran unas ciertas órdenes en el caso de que la condición no se cumpliera?

      if fav == “mundogeek.net”:
      print “Tienes buen gusto!"
      else:
      print “Vaya, que lástima”
      
Vemos que la segunda condición se puede sustituir con un else (del inglés: si no, en caso contrario). Si leemos el código vemos que tiene bastante sentido: “si fav es igual a mundogeek.net, imprime esto y esto, si no, imprime esto otro”.
