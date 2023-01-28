EVALUACION 4

1

    import random # para poder generar los números aleatorios
    lista_numeros = [] # la lista donde se guardarán
    # Primer recorrido para leer la lista
    for indice in range(1,11):
      lista_numeros.append(random.randint(1,10))
    ## Segundo recorrido para mostrar el resultado
    for numero in lista_numeros:
      print(numero," ",numero ** 2," ",numero ** 3) 

2

    i=0
    palabras=[]
    while i < 5:
      palabra=input('ingresa una palabra')
      palabras.append(palabra)
      i=i+1
    palabras.sort(reverse=True)
    palabras
    
3
    
    i=1
    calificaciones=[]
    suma_cal=0
    while i < 6:
      cal=int(input('ingresa la calificación '))
      if cal < 10 and cal > 0:
        calificaciones.append(cal)
        suma_cal=suma_cal + cal
        i=i+1
      else:
        print('rango de calificacion incorrecto')

    print(f'la calificación máxima fue {max(calificaciones)} ')
    print(f'la calificación mínima fue {min(calificaciones)} ')
    print(f'el promedio de calificaciones es {suma_cal/5} ')

4 (modificalo para cumplir los requerimientos)

    alumnos={}
    nombres=[]
    promedio=[]
    veces=int(input('de cuantos alumnos quieres capturar las calificaciones '))
    i=0
    while i < veces:
      i=i+1
      nombre=input('ingresa el nombre del alumno')
      if nombre in alumnos:
        print('ya existe')
        break
      else:
        nombres.append(nombre)
        alumnos['nombre']=nombres
        cal1=int(input('ingresa la cal1'))
        cal2=int(input('ingresa la cal2'))
        cal3=int(input('ingresa la cal3'))
        prom=(cal1+cal2+cal3)/3
        promedio.append(prom)
        alumnos['promedio']=promedio
        print(' nombre: \n', alumnos['nombre'],'\n promedio:','\n', alumnos['promedio'])
        
5

    meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre","Noviembre", "Diciembre")
    salir = int(input('ingresa un número entre 1 y 12 para imprimir el mes al que corresponde, para salir presiona 0'))
    while salir != 0:
      print(meses[salir - 1])
      salir = int(input('ingresa un número entre 1 y 12 para imprimir el mes al que corresponde, para salir presiona 0'))
    print('has salido')


EVALUACION 6

1

        print(f'''Menú de recomedaciones
        (1) Literatura
        (2) Cine
        (3) Música
        (4) Videojuegos
        (5) Salir
        ''')

        seleccion=0

        while seleccion != 5:
          seleccion=int(input(f'Introduce tu elección (1,2,3,4,5): '))
          if seleccion==1:
              print(f'''
                  Lecturas recomendables:

                  °Esperándolo a Tito y otros cuentos de fútbol (Eduardo Sacheri)
                  °El juego de Ender (Orson Scott Card)
                  °El sueño de los héroes (Adolfo Bioy Casares)
              ''')


          elif seleccion==2:
            print(f'''
                  Películas recomendables:

                  °Matrix (1999)
                  °El último samuray (2003)
                  °Cars (2006)
              ''')

          elif seleccion==3:
            print(f'''
                  Discos recomendables:

                  °Despedazado por mil partes (La Renga, 1996)
                  °Búfalo (La Mississippi, 2008)
                  °Gaia (Mago de Oz, 2003)
              ''')

          elif seleccion==4:
            print(f'''
                  Videojuegos clásicos recomendables

                  °Día del tentáculo (LucasArts, 1993)
                  °Terminal Velocity (Terminal Reality/3D Realms, 1995)
                  °Death Rally (Remedy/Apogee, 1996)
              ''')

          elif seleccion==5:
            print('Gracias, vuelva pronto')
            break
          else:
            print(f'''
            Opción inválida.
            ''')

            print(f'''Menú de recomedaciones
            (1) Literatura
            (2) Cine
            (3) Música
            (4) Videojuegos
            (5) Salir
            ''')  

2

    numero=int(input('Dame un número entero positivo: '))
    while numero >= 1:
      x=1
      validador=0
      while x <= numero:
        if numero % x == 0:
          validador=validador+1
        x=x+1
      if validador==2:
        print(f'{numero} es un número primo')
      else:
        print(f'{numero} no es un número primo')
      numero=numero-1

3

    pago=10
    total=0
    for i in range(1,21):
      print(f' {i} pago : {pago} ')
      total = total + pago
      pago = pago * 2

    print('pago en total ',total)
    
4

    num=int(input('ingresa el numero del que deseas el factorial'))
    fact=1
    for i in range(1,num+1):
      fact = i * fact
    print(fact)

EVALUACION 7

https://colab.research.google.com/drive/1EfeXvaBo3ejRY6uoCcShXkFV8yqPENJ-?authuser=5
