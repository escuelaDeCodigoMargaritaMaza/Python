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

### Crea un template con Jinja2:
* En tu directorio templates, crea un archivo saludo.html.
* Añade el siguiente contenido, que incluye sintaxis de Jinja2:

      <!DOCTYPE html>
      <html lang="es">
      <head>
          <meta charset="UTF-8">
          <title>Saludo</title>
      </head>
      <body>
          <h1>Hola, {{ nombre }}!</h1>
          {% if edad >= 18 %}
              <p>Eres mayor de edad.</p>
          {% else %}
              <p>Eres menor de edad.</p>
          {% endif %}
      </body>
      </html>

* Aquí, {{ nombre }} es una variable que se pasará desde la función de vista en Flask.
* {% if %} y {% else %} son declaraciones condicionales que controlan qué parte del template se renderiza basado en la variable edad
* Renderiza el template desde una ruta:

  En tu app.py, crea una nueva ruta que pase variables al template:

    @app.route('/greet/<nombre>/<int:edad>')
    def saludar(nombre, edad):
    return render_template('saludo.html', nombre=nombre, edad=edad)

*  Esta ruta acepta un nombre y una edad como parte de la URL y las pasa al template saludo.html.
*  inicia tu servidor Flask y visita http://127.0.0.1:5000/greet/Juan/20.
