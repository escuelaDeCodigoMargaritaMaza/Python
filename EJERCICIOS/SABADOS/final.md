1. Crea una carpeta para el proyecto, dentro crea tres archivos python: main, palabras y figuras

2. En palabras crea una lista con varias palabras de tu elección

3. En figuras crea una lista con las figuras del ahora

          +----+
           |    |
                |
                |
                |
                |
                ==========
        
            +----+
            |    |
            O    |
                 |
                 |
                 |
                 ==========
        
            +----+
            |    |
            O    |
            |    |
                 |
                 |
                 ==========
        
            +----+
            |    |
            O    |
           /|    |
                 |
                 |
                 ==========
        
            +----+
            |    |
            O    |
           /|\   |
                 |
                 |
                 ==========
        
            +----+
            |    |
            O    |
           /|\   |
            |    |
                 |
                 ==========
        
            +----+
            |    |
            O    |
           /|\   |
            |    |
           /     |
                 ==========
        
            +----+
            |    |
            O    |
           /|\   |
            |    |
           / \   |
                 ==========

4. En main importa radom, y las dos listas de cada archivo.

5. Implementa una funcion (palabra_secreta()) para seleccionar una palabra aleatoria de la lista, esto via el indice.

       def palabra_secreta():
            indice = random.randint(0,len(palabras) - 1)
            return palabras[indice]

7. Crea otra función(visual()), esta tendrá argumentos: palabra_a_buscar y las oportunidades, la función tendrá una condicionante simple, si las oportunidades son mayor a 0 invocará a otra función (encabezado()) que muestre el encabezado del juego, más adelante se creaará, también esta función imprimira la figura actual (indice en la lista), la palabra_a_buscar representada por guiones, estás más adelante serán trabajadas, por ahora solo se establecen en las funciones por el nombre de las variables

          def visual(palabra_buscar, oportunidades):
                if oportunidades > 0:
                    encabezado()
                print(figuras[oportunidades])
                print('')
                print(palabra_buscar)
                print('\n----------------------------------------------')

8. Crea otra función(iniciar_juego()) que inicia el juego esta inicializa la palabra = palabra_secreta(), Crea una lista llamada palabra_buscar con guiones para representar la palabra oculta (palabra_buscar = ['-'] * len(palabra)) e inicia oportunidades en 0.

       def iniciar_juego():
        palabra = palabra_secreta()
        palabra_buscar = ['-'] * len(palabra)
        oportunidades = 0

10. Mientras el jugador no haya adivinado la palabra o haya agotado las oportunidades (while True):
    
          while True:
                visual(palabra_buscar, oportunidades)
                letra_ingresada = str(input('Ingresa una letra: '))
                letras_escritas = []
    
    Llama a visual(palabra_buscar, oportunidades) para mostrar la interfaz del juego.
    Pide al jugador que ingrese una letra y la guarda en letra_ingresada.
    Verifica si la letra esta ya en las se han ingresado con un for
   
         for i in range(len(palabra)):
            if palabra[i] == letra_ingresada:
                letras_escritas.append(i)
   
    Si no se encuentra la letra, incrementa oportunidades.
   
        if len(letras_escritas) == 0:
            oportunidades += 1
    
   Si el jugador ha agotado las oportunidades, muestra un mensaje de derrota con la palabra secreta, dentro del mismo if

          if oportunidades == 7:
                visual(palabra_buscar, oportunidades)
                print('')
                print(f'Lo siento {self.nombre} has perdido la palabra era : {palabra}')
                break
   
   Si se encontraron letras coincidentes, Actualiza palabra_buscar en las posiciones correspondientes con la letra 
   ingresada y  Reinicia la lista  letras_escritas

        else:
                for i in letras_escritas:
                    palabra_buscar[i]= letra_ingresada
                letras_escritas = []
   
   genera una excepción para que si al buscar un caracter - no lo encuentre nos diga que hemos ganado

       try:
            palabra_buscar.index('-')
        except ValueError:
            print('')
            print(f'Felicidades,has adivinado la palabra {palabra}!')
            break
11. Define la función encabezado()   Esta función muestra el título y las instrucciones del juego.
    
        def encabezado():
            print('=================================')
            print('======JUEGO DEL AHORCADO=========')
            print('A D I V I N A la palabra secreta')
            print('(Palabras relacionadas al taller)')
            print('=================================')

12. Invoca las funciones encabezado() y iniciar_juego()



# main

          import random
          from palabras import palabras
          from figuras import figuras
          
          def palabra_secreta():
              indice = random.randint(0,len(palabras) - 1)
              return palabras[indice]
          
          def visual(palabra_buscar, oportunidades):
              if oportunidades > 0:
                  encabezado()
              print(figuras[oportunidades])
              print('')
              print(palabra_buscar)
              print('\n----------------------------------------------')
          
          def iniciar_juego():
              palabra = palabra_secreta()
              palabra_buscar = ['-'] * len(palabra)
              oportunidades = 0
              while True:
                  visual(palabra_buscar, oportunidades)
                  letra_ingresada = str(input('Ingresa una letra: '))
                  letras_escritas = []
          
                  for i in range(len(palabra)):
                      if palabra[i] == letra_ingresada:
                          letras_escritas.append(i)
          
                  if len(letras_escritas) == 0:
                      oportunidades += 1
          
                      if oportunidades == 7:
                          visual(palabra_buscar, oportunidades)
                          print('')
                          print(f'Lo siento has perdido la palabra era : {palabra}')
                          break
                  else:
                      for i in letras_escritas:
                          palabra_buscar[i]= letra_ingresada
                          letras_escritas = []
          
                  try:
                      palabra_buscar.index('-')
          
                  except ValueError:
                      print('')
                      print(f'Felicidades,has adivinado la palabra {palabra}!')
                      break
          
          
          def encabezado():
              print('=================================')
              print('======JUEGO DEL AHORCADO=========')
              print('A D I V I N A la palabra secreta')
              print('(Palabras relacionadas al taller)')
              print('=================================')
          
          
          
          encabezado()
          iniciar_juego()

# figuras

          figuras = ['''+----+
              |    |
                   |
                   |
                   |
                   |
                   ==========''','''
           
               +----+
               |    |
               O    |
                    |
                    |
                    |
                    ==========''','''
           
               +----+
               |    |
               O    |
               |    |
                    |
                    |
                    ==========''','''
           
               +----+
               |    |
               O    |
              /|    |
                    |
                    |
                    ==========''','''
           
               +----+
               |    |
               O    |
              /|\   |
                    |
                    |
                    ==========''','''
           
               +----+
               |    |
               O    |
              /|\   |
               |    |
                    |
                    ==========''','''
               +----+
               |    |
               O    |
              /|\   |
               |    |
              /     |
                    ==========''','''
                +----+
               |    |
               O    |
              /|\   |
               |    |
              / \   |
                    ==========''']


# palabras

          palabras = "pilares computo usuario taller tallerista".split()
