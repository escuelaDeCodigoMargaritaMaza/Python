## Tipos de datos complejos (Colecciones)

Existen ciertos tipos de datos más complejos que los que acabamos de enumerar, destinados a agrupar elementos:

* Listas

Se trata de conjuntos ordenados de elementos, encerrados por corchetes y separados por comas. El orden comienza con el índice 0 para el primer lugar de la Lista. Pueden agruparse valores de distintos tipos de datos básicos, y es posible agregar, eliminar o modificar elementos de las listas en cualquier momento (decimos que las Listas son mutables en Python)


    lista = [10,20,30,40]
    print(lista)
    print(lista[0])
    print(lista[3])
    [10, 20, 30, 40]

    


* Tuplas

Las Tuplas son básicamente Listas de elementos estáticas, es decir, que no pueden modificarse (decimos que las Tuplas son inmutables en Python). Para su definición, en lugar de corchetes se encierran valores separados por comas entre paréntesis.


    # Definición de una tupla y referencia a un índice
    tupla = (6, 7, 8,9)
    print(tupla)
    print(tupla[0])
    print(tupla[3])
    (6, 7, 8, 9)

 

La similitud entre Listas y Tuplas es tan explícita que se puede bloquear una lista tranformándola en una tupla con la función tuple() o bien desbloquear una tupla para transformarla en una lista con la función list()

    print(tuple(lista))
    print(list(tupla))
    (10, 25, 30, 40)
    [6, 7, 8, 9]

* Diccionarios

En los Diccionarios cada elemento se compone de un par clave-valor, y para su definición es necesario encerrar los elementos entre llaves. Es posible acceder a un valor utilizando su clave, pero no al revés. Por este motivo, no se pueden repetir las claves para elementos distintos, pero sí es posible agregar, eliminar o modificar valores (Los diccionarios son mutables).


    # Definición de un diccionario
    diccionario = {"Codigo":7512,"Materia":"Análisis Numérico I"}
    print(diccionario)
    {'Codigo': 7512, 'Materia': 'Análisis Numérico I'}

    # Referencia a un índice
    print(diccionario["Codigo"])
    print(diccionario["Materia"])
    
    7512
    Análisis Numérico I



https://colab.research.google.com/drive/1Q5NPPGU9ULLXhw1VYgoQc8e9X4qILbfV
