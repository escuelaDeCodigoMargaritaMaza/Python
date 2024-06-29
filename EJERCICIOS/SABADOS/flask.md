# ¿Qué es Flask y por qué usarlo?
Flask es un microframework de código abierto para Python, conocido por su simplicidad y flexibilidad.

* Origen: Flask fue creado por Armin Ronacher como un proyecto de 1 de abril, pero rápidamente ganó popularidad debido a su diseño ligero y fácil de usar.
* Filosofía: Su filosofía se centra en la simplicidad y la capacidad de ampliarse con extensiones, lo que permite a los desarrolladores agregar solo lo que necesitan.
* Comunidad: La comunidad de Flask ha crecido significativamente, contribuyendo con una amplia gama de extensiones y plugins que enriquecen su ecosistema.
* Uso Actual: Hoy en día, Flask se utiliza en una variedad de proyectos web, desde aplicaciones pequeñas hasta grandes plataformas, gracias a su capacidad para escalar y adaptarse a diferentes necesidades de desarrollo.

## Breve historia de Flask:

* Origen como broma: Flask comenzó como una broma de April Fools’ Day (Día de los Inocentes en algunos países) en 2010. Armin Ronacher, quien es parte del equipo de Pocoo, lo presentó como un microframework llamado “Denied” que era solo un archivo.
* Evolución: A pesar de su inicio humorístico, la idea detrás de Flask capturó el interés de la comunidad de desarrolladores. Ronacher decidió continuar el desarrollo del proyecto con un enfoque serio, renombrándolo como Flask.
* Crecimiento: Desde entonces, Flask ha crecido en popularidad y funcionalidad, convirtiéndose en uno de los frameworks web más utilizados en Python. Su diseño minimalista y fácilmente extensible lo hace adecuado tanto para prototipos rápidos como para aplicaciones web a gran escala.

## Lugar en el desarrollo web:

* Microframework: A diferencia de frameworks completos como Django, Flask proporciona las herramientas básicas necesarias para comenzar un proyecto web, dejando muchas decisiones y extensiones al desarrollador.
* Flexibilidad y extensibilidad: Esta flexibilidad ha posicionado a Flask como una opción ideal para proyectos que requieren una estructura personalizada o para desarrolladores que prefieren construir su aplicación pieza por pieza.
* Comunidad y ecosistema: La comunidad activa y el ecosistema de extensiones han contribuido al lugar sólido de Flask en el desarrollo web, permitiendo que los desarrolladores encuentren soporte y recursos fácilmente.

* * Instalación de Python: Asegúrate de tener Python instalado en tu sistema. Puedes descargarlo desde la página oficial de Python (python.org).

* Con el entorno virtual activado, instala Flask utilizando pip:
  
       pip install Flask

* Abre tu IDE o editor de código preferido.
* Crea un nuevo archivo llamado app.py.
* Escribe el siguiente código básico de Flask:

      from flask import Flask
      app = Flask(__name__)
      
      @app.route('/')
      def hola_mundo():
          return '¡Hola, mundo!'
      
      if __name__ == '__main__':
          app.run(debug=True)

  * Guarda el archivo.
  * En la terminal, asegúrate de estar en el directorio del proyecto
  * Ejecuta el script con Python:
    
          python app.py
  * Abre un navegador y visita http://127.0.0.1:5000/ para ver tu aplicación Flask en acción.
 ### explicación del código
 
  Importar Flask: from flask import Flask
  
  Esto importa la clase Flask del módulo flask, que es necesario para crear una instancia de una aplicación Flask.
  Crear la aplicación: app = Flask(__name__)
  
  Aquí se crea una instancia de la clase Flask, llamada app. El argumento __name__ es una variable especial de Python que se utiliza para determinar el nombre del módulo en el que se está ejecutando el script. Esto es necesario para que Flask sepa dónde buscar recursos como plantillas y archivos estáticos.
  
  Definir una ruta: @app.route('/')
  
  Este decorador le dice a Flask qué URL debe activar la función que sigue. En este caso, la ruta '/' representa la raíz del sitio web.
  
  Definir una función de vista:

        def hello_world():
            return '¡Hola, mundo!'
      
  
  Esta es la función que se ejecutará cuando se acceda a la URL definida por el decorador de ruta. La cadena '¡Hola, mundo!' será lo que se muestre en el navegador cuando visites la URL raíz del sitio.
  Ejecutar la aplicación:
  
      if __name__ == '__main__':
          app.run(debug=True)
      
  Este bloque condicional verifica si el script se está ejecutando directamente (no siendo importado). Si es así, app.run(debug=True) inicia el servidor de desarrollo de Flask.
  El argumento debug=True activa el modo de depuración, lo que significa que el servidor se reiniciará automáticamente con cada cambio en el código y proporcionará una página de error útil si algo sale mal.

  ### rutas
  
          from flask import Flask
          app = Flask(__name__)
          
          @app.route('/')
          def index():
              return 'Página principal'
          
          @app.route('/about')
          def about():
              return 'Acerca de'
          
          if __name__ == '__main__':
              app.run(debug=True)
              
### ejercicio

    Crea una ruta /hola que devuelva el texto “¡Hola, Mundo!”.
    Página de contacto:
    Crea una ruta /contact que devuelva un mensaje como “Contacto: correo@example.com”.

### Usando templates
* En el mismo directorio que tu app.py, crea una carpeta llamada templates.
* Agrega contenido básico HTML, por ejemplo:

      <!DOCTYPE html>
      <html lang="es">
      <head>
          <meta charset="UTF-8">
          <title>Bienvenido</title>
      </head>
      <body>
          <h1>¡Bienvenido a Flask!</h1>
      </body>
      </html>
  
* Importa render_template de Flask al principio de tu app.py.
* Cambia la función hola() para que renderice el template:

      from flask import render_template
  
      @app.route('/hola')
      def hello():
          return render_template('index.html')

  * Crea una ruta dinámica
  * Añade una nueva función con una variable en la ruta:
    
        @app.route('/user/<username>')
        def user(username):
        return f'¡Hola, {username}!'

* Visita http://127.0.0.1:5000/user/tu_nombre en el navegador, reemplazando “tu_nombre” con cualquier nombre que quieras.

## Templates con Jinja2 en Flask:
Jinja2 es un motor de plantillas para Python que se utiliza en Flask para renderizar vistas. Permite escribir código Python dentro de los archivos HTML para generar contenido dinámico.

## VERSION 1

app.py

        from flask import Flask
        from flask import render_template
        app = Flask(__name__)
        
        @app.route('/')
        def hola_mundo():
            return render_template('index.html')
        
        if __name__ == '__main__':
            app.run(debug=True)


index.html

        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Bienvenido</title>
        </head>
        <body>
            <h1 style="color: cornflowerblue; font-size: 2rem; text-align: center;">BIENVENIDO A MI APLICACION FLESK</h1>
            
        </body>
        </html>
         
.

app = Flask(__name__) se utiliza para crear una instancia de la aplicación Flask. Aquí está el significado de cada parte:

Flask: Es una clase proporcionada por el framework Flask. Representa una aplicación web y proporciona funcionalidades para manejar solicitudes HTTP, rutas, vistas, plantillas, etc.

app: Es el nombre que le das a tu instancia de la aplicación. Puedes elegir cualquier nombre que desees.

__name__: Es una variable especial en Python que se refiere al nombre del módulo o script actual. Cuando ejecutas un archivo Python directamente (como un script), Python asigna el valor __main__ a __name__. Por lo tanto, en este caso, Flask(__name__) crea una instancia de la aplicación Flask y la asocia con el módulo actual.

En resumen, app = Flask(__name__) crea una aplicación Flask que puedes usar para definir rutas, vistas y otras funcionalidades web. Si tienes más preguntas o necesitas más detalles, no dudes en preguntar. 

        if __name__ == '__main__'::
Esta línea verifica si el script de Python está siendo ejecutado directamente (es decir, no importado como un módulo en otro script).
Cuando ejecutas un archivo Python, el intérprete asigna el valor especial __main__ al atributo __name__.

Por lo tanto, esta condición se cumple cuando ejecutas el archivo directamente desde la línea de comandos o desde un entorno de desarrollo.
app.run(debug=True):

app se refiere a la instancia de la aplicación Flask que has creado previamente.

run() es un método de Flask que inicia el servidor web local para manejar las solicitudes HTTP.

El argumento debug=True habilita el modo de depuración. Cuando está activado:
* Se muestra información detallada sobre errores en el navegador.
* El servidor se reinicia automáticamente cuando modificas el código.
* No se debe usar en producción debido a posibles problemas de seguridad.


