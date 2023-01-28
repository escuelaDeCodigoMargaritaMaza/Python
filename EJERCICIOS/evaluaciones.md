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

https://colab.research.google.com/drive/1nxCF0Ke5nzl2EwNhBZoo5YepihKPVu7A?authuser=5

EVALUACION 7

https://colab.research.google.com/drive/1EfeXvaBo3ejRY6uoCcShXkFV8yqPENJ-?authuser=5
