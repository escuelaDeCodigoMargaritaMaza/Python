## 1.1.¿Qué es Python?
Python es un lenguaje de programación creado por Guido van Rossum a
principios de los años 90 cuyo nombre está inspirado en el grupo de cómicos
ingleses “Monty Python”. Es un lenguaje similar a Perl, pero con una sintaxis
muy limpia y que favorece un código legible. Se trata de un lenguaje interpretado
o de script, con tipado dinámico, fuertemente tipado, multiplataforma y orientado
a objetos.

### Lenguaje interpretado o de script
Un lenguaje interpretado o de script es aquel que se ejecuta utilizando un
programa intermedio llamado intérprete, en lugar de compilar el código a
lenguaje máquina que pueda comprender y ejecutar directamente una
computadora (lenguajes compilados).
Fuertemente tipado
No se permite tratar a una variable como si fuera de un tipo distinto al que tiene,
es necesario convertir de forma explícita dicha variable al nuevo tipo
previamente. Por ejemplo, si tenemos una variable que contiene un texto
(variable de tipo cadena o string) no podremos tratarla como un número (sumar
la cadena “9” y el número 8). En otros lenguajes el tipo de la variable cambiaría
para adaptarse al comportamiento esperado, aunque esto es más propenso a
errores.

### Multiplataforma
El intérprete de Python está disponible en multitud de plataformas (UNIX, Solaris,
Linux, DOS, Windows, OS/2, Mac OS, etc.) por lo que si no utilizamos librerías
específicas de cada plataforma nuestro programa podrá correr en todos estos
sistemas sin grandes cambios.

### Orientado a objetos
La orientación a objetos es un paradigma de programación en el que los
conceptos del mundo real relevantes para nuestro problema se trasladan a
clases y objetos en nuestro programa. La ejecución del programa consiste en
una serie de interacciones entre los objetos. Python también permite la
programación imperativa, programación funcional y programación orientada a
aspectos.

### Instalación de Python
Primero comprueba si tu ordenador ejecuta la versión 32 bits de Windows o
la de 64, en "Tipo de sistema" en la página de "Acerca de". Para llegar a esta
página, intenta uno de estos métodos:
Presiona la tecla de Windows y la tecla Pause/Break al mismo tiempo
Abre el Panel de Control desde el menú de Windows, después accede a
Sistema & y Seguridad, luego a Sistema
Presiona el botón de Windows, luego accede a Configuración > Sistema >
Acerca de

Puedes descargar Python para Windows desde la siguiente web
https://www.python.org/downloads/windows/.
Da clic en el enlace "Latest Python 3 Release -Python x.x.x".
Si tu ordenador ejecuta la versión de 64 bits de Windows, descarga Windows
x86-64 executable installer. De lo contrario, descarga Windows x86
ejecutable installer. Después de descargar el instalador, deberías ejecutarlo
(dándole doble click) y seguir las instrucciones.
Una cosa para tener en cuenta: Durante la instalación, verás una ventana
de "Setup". Asegúrate de marcar las casillas "Add Python 3.6 to PATH" o
"Add Python to your environment variables" y hacer click en "Install Now",
como se muestra aquí (puede que se vea un poco diferente si estás
instalando una versión diferente):

![image](https://user-images.githubusercontent.com/91554777/173450028-d8b42537-b1d2-4dde-8945-cfc176a55e4b.png)

Cuando la instalación se complete, verás un cuadro de diálogo con un enlace
que puedes seguir para saber más sobre Python o sobre la versión que has
instalado. Cierra o cancela ese diálogo.
Comprobar que se instalo Python con el siguiente comando desde la cmd

python –versión

### Python en Linux
actualizaremos la lista de paquetes usando el siguiente comando. Puedes ejecutar este comando como administrador o como usuario normal con privilegios sudo. En ese caso, debes añadir sudo al comando antes de ejecutar la actualización.

    sudo apt update

Python 3 se instala por defecto en la distribución Linux Ubuntu 18.04. Entonces necesitaremos instalar el paquete python3-pip usando el siguiente comando. También instalará las dependencias requeridas, agilizando así el proceso.

    apt install python3-pip
    
Normalmente, los comandos de Python están configurados para Python 2.7 y los comandos de Python 3 están configurados para la última versión 3. En sistemas operativos anteriores, la instalación predeterminada es Python 2.7. El procedimiento es más o menos el mismo para todas las versiones.

Puedes verificar las versiones de cada uno utilizando los siguientes comandos pip:

    pip --version
    python -V
    
Aunque los desarrolladores web crean sus sitios web mediante el uso de herramientas como Node.js, ASP.NET o Java, y ejecutan su código localmente mediante el uso de herramientas en editores de código como Visual Studio Code, los desarrolladores de Python tienen algunas otras herramientas a su disposición.

Una de esas herramientas útiles se llama notebook / notebook . Un notebook es un entorno interactivo que un desarrollador puede usar para ejecutar bloques de código y agregar áreas de documentación para explicar el código en sí. Aunque los desarrolladores de Python también pueden usar archivos .py para ejecutar programas de Python directamente, pueden usar notebooks para ejecutar y documentar su código, explicando su lógica en el camino.

Hay muchas maneras de ejecutar notebooks. En este módulo, sin embargo, aprenderás a configurar tu entorno de trabajo para ejecutar notebooks localmente a través de Visual Studio Code.

Para comenzar a crear tu notebook, debes tener el siguiente software (programas) disponible en su computadora:

* Python
* Visual Studio Code
* Extensión Jupyter de Visual Studio Code

## Instalando la extensión de Python

Esta extensión permite ejecutar notebooks de Jupyter desde Visual Studio Code mediante un [Kernel](https://es.wikipedia.org/wiki/N%C3%BAcleo_(inform%C3%A1tica)). Un kernel en Visual Studio Code le ayuda a activar un entorno de Anaconda, por lo que puede ejecutar sus notebooks mediante la instalación de Python.

En Visual Studio Code, en el panel de extensiones de la izquierda, busque Jupyter de Microsoft. Para instalar esta extensión, seleccione Instalar.

![image](https://user-images.githubusercontent.com/91554777/173451818-b3d8d036-c81e-4fac-90bc-1b96591ad920.png)

Ahora que tienes configurados los tres elementos del área de trabajo, puedes empezar a trabajar con los notebooks de Jupyter en Visual Studio Code.


![image](https://user-images.githubusercontent.com/91554777/173451847-93594db1-dda3-409d-8ab3-b696b34459fd.png)

La extensión Jupyter debe mostrar el archivo en blanco, con la opción de agregar código (python) y bloques Markdown (Un lenguaje de etiquetas, similar a html que hemos ya trabajado de manera básica).

### Crear un elemento de tipo Markdown

En la parte superior del notebook, verás dos opciones para crear dos tipos diferentes de bloques de contenido en el notebook: **Markdown** y **código ejecutable**.

La primera tarea es crear un título de documento. En la parte superior de la interfaz del notebook de Visual Studio Code, selecciona el botón más (+) situado junto a Markdown. Aparecerá un cuadro. Agregue el siguiente Markdown al cuadro:

`` # Taller de Python en PILARES``

Selecciona la palomita para ver el resultado.

![image](https://user-images.githubusercontent.com/91554777/173451765-f0734bd4-88d3-4d48-a38c-a9a0754def45.png)

¡Acabas de nombrar tu notebook! Para ver cómo se representa este archivo Markdown, elige ejecutar todo desde la parte superior del notebook o la flecha pequeña a la izquierda del cuadro Markdown.`<h1>`

### Ejecutar el notebook

Ahora necesitas ejecutar tu notebook. Elige un kernel de la lista desplegable en la parte superior derecha. Es posible que tengas uno o varios núcleos para elegir, así que asegúrese de elegir un kernel de Python 3.


### Crear código ejecutable

Ahora puedes agregar algo de código al notebook. Agreguemos una forma de mostrar un widget para iniciar el notebook.

Primero, debes instalar una biblioteca llamada ``ipywidgets``. Instala la biblioteca agregando un nuevo bloque de código debajo del bloque de título del notebook. Utilizando el administrador de paquetes de Python ``pip``, para instalar la biblioteca.

``pip install ipywidgets``

![image](https://user-images.githubusercontent.com/91554777/173451981-6eecb098-5b0b-4745-a962-49d2c8f4522d.png)

Después de instalarlo, te pedirá que reinicies el kernel. Basta con dar clic en la sección señalada de amarillo para reiniciar el kernel.

![image](https://user-images.githubusercontent.com/91554777/173452013-0cc65a48-bc49-41ca-9ba5-ca873cce0247.png)

A continuación, crearemos un botón en el notebook que, cuando se presiona, muestra un mensaje.

En un nuevo bloque de código, agrega el código siguiente:

```
import ipywidgets as widgets

prueba = widgets.ToggleButton(
    value=False,
    description='Iniciar prueba',
    button_style='success',
    tooltip='prueba de instalacion',
    icon='rocket'
)

output = widgets.Output()

display(prueba, output)

def on_value_change(change):
    with output:
        if change['new'] == True:
            print("Prueba iniciada")
        else:   
            print("Prueba detenida")

prueba.observe(on_value_change, names='value')
```


¿Qué está pasando aquí? Utilizamos la biblioteca ``ipywidget`` para crear un botón y éste escucha cuando hacemos un clic provocando que su valor cambie, imprimiendo el mensaje observado.


https://minhaskamal.github.io/DownGit/#/home

https://replit.com/languages/python3
