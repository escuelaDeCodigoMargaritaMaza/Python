Instalar MySQL
https://dev.mysql.com/downloads/windows/installer/

Crea un archivo llamado app.py y coloca el código principal allí:

Crea una carpeta llamada templates en el mismo directorio que app.py y dentro de ella, crea un archivo HTML llamado registro.html con el siguiente contenido:

Asegúrate de tener instalados Flask y Flask-MySQLdb. Puedes instalarlos ejecutando el siguiente comando en tu terminal:

pip install flask flask-mysqldb

Ejecuta el archivo app.py y abre tu navegador en http://localhost:5000/registro para acceder al formulario de registro.

Ten en cuenta que necesitarás tener un servidor MySQL en ejecución y haber creado una base de datos con una tabla llamada usuarios que contenga las columnas nombre_usuario y contraseña. Asegúrate de reemplazar los valores de tu_usuario, tu_contraseña y nombre_de_la_base_de_datos en el archivo app.py con los valores correctos según tu configuración de MySQL.

Si da error Mysql puede ser la incompatibilidad de idioma para ello buscamos region en el panel de control, administrativo y cambiar configuracion regional del sistema, hbilitar beta y reiniciar
