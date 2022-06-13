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
