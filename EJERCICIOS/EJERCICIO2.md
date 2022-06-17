## Realiza el siguiente ejercicio en un cudernillo de Jupyter
Saber cómo dar formato a las cadenas es esencial cuando se presenta información de un programa. Hay algunas maneras diferentes de lograr esto en Python.
En este ejercicio, se utilizan variables que contienen datos clave sobre usuarios y luego se utilizan para dar formato e imprimir la información.

![image](https://user-images.githubusercontent.com/91554777/174206918-440767f6-eba2-4aff-8ca4-6652cc374577.png)

### Datos con los que vas a trabajar
taller = "Escuela de Código"

folio = 3

nombre = "Juan"

* Primero, crea un título para el texto. Debido a que este texto trata sobre la gravedad en la Tierra y la Luna, úsalo para crear un título significativo. Utiliza las variables en lugar de escribir.

* Ahora crea una plantilla de cadena multilínea para contener el resto de la información. 

* Finalmente, usa ambas variables para unir el título y los hechos.

* Ahora usa información de un usuario diferente para ver si la plantilla todavía funciona.

Datos muestra:

taller = 'Huertos '

folio  = 34

nombre = 'María'

* La salida no muestra información sobre María. Todavía muestra información sobre la Juan. 
Esto sucede porque las cadenas f están ansiosas en su evaluación, por lo que las variables una vez asignadas no se pueden reasignar. 
Para evitar este problema, vuelva a hacer la plantilla para utilizar .format():

