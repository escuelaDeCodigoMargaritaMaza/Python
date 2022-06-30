El módulo es un archivo que contiene funciones de Python, variables globales, etc. No es más que un archivo .py que tiene código / instrucción ejecutable de Python.

Por ejemplo: creemos un archivo user.py

def welcome_message(user_name):  
	return "Welcome " + name 
Ahora puede importar el módulo foo.py en el intérprete de python u otro archivo py.

import user 
print user.welcome_message("Quora") 
El paquete es un espacio de nombres que contiene múltiples paquetes / módulos. Es un directorio que contiene un archivo especial __init__.py

Vamos a crear un usuario de directorio. Ahora este paquete contiene múltiples paquetes / módulos para manejar solicitudes relacionadas con el usuario.

user/ # top level package 
  __init__.py 
  get/ # first subpackage 
     __init__.py 
     info.py 
     points.py 
     transactions.py 
 create/ # second subpackage 
      __init__.py  
      api.py  
      platform.py 
Ahora puedes importarlo de la siguiente manera

from user.get import info # imports info module from get package 
from user.create import api #imports api module from create package  
Cuando importamos cualquier paquete, el intérprete de Python busca subdirectorios / paquetes.

Biblioteca

Es una colección de varios paquetes. No hay diferencia entre el paquete y la biblioteca de Python conceptualmente.

Mira esta requests/requests biblioteca. Lo usamos como un paquete

Framework

Es una colección de varias bibliotecas que crea el flujo de código.

Tomemos un ejemplo de Django que tiene varias bibliotecas integradas como Auth, user, database connector etc.
