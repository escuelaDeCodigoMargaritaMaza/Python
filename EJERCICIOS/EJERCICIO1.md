Realiza un cuaderno de Python en Jupiter con el nombre Ejercicio1.ipynb

Dentro vaamos a resolver los siguientes problemas:

1. Una línea de código que  muestre la fecha de hoy.

2. Construir un convertidor de unidades de centimetros a metros (el formato del resultado deberá ser: X cm son igual a X metros, según el usuarios ingrese la cantidad a convertir).

3. Exploremos cómo podemos crear un programa que pueda calcular la distancia entre dos planetas EN KILOMETROS Y EN MILLAS. Comenzaremos usando dos distancias de planetas al sol: Tierra (149.597.870 km) y Júpiter (778.547.200 km). Calcular cuanta distancia hay en kilometos y en millas entre estos dos planetas.

Nota: Quita las comas cuando uses los valores.

Crear una aplicación para trabajar con números y entrada de usuario


Para crear nuestra aplicación, queremos leer la distancia del sol para dos planetas, y luego mostrar la distancia entre los planetas. Haremos esto usando input para leer los valores, int para convertir a entero y luego abs para convertir el resultado en su valor absoluto.

PASOS:

a) Lee los valores

Usando input, agrega el código para leer la distancia del sol para cada planeta, considerando 2 planetas.

b)Convertir a número

Debido a que input devuelve valores de cadena, necesitamos convertirlos en números. Para nuestro ejemplo, usaremos int

c)Realizar el cálculo y convertir a valor absoluto

Con los valores almacenados como números, ahora puedes agregar el código para realizar el cálculo, restando el primer planeta del segundo. Debido a que el segundo planeta podría ser un número mayor, usarás abs para convertirlo a un valor absoluto

d)Prueba tu aplicación

Para probar el proyecto, ejecuta tu notebook. En la parte superior de vscode surgirá un cuadro de diálogo para que proporciones las distancias. Puede utilizar los datos de la tabla siguiente:

Planeta	Y Distancia al sol

Mercurio	57900000

Venus	108200000

Tierra	149600000

Marte	227900000

Júpiter	778600000

Saturno	1433500000

Urano	2872500000

Neptuno	4495100000
