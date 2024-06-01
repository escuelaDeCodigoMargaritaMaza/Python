# VERSION 1
    
    nombre = ""
    secreto = 15
    numero_dado = 0   #Snakecase para variables y funciones
    atinado = False
    oportunidades = 3
    
    
    nombre = input("Ingresa tu nombre:\n")
    print(f'\n**************** {nombre} ********** Adivina el número secreto *************\n')
    numeroDado=int(input("Ingresa tú  número: "))
    
    print(f'{secreto} es el número secreto, tú ingresaste {numero_dado}, atinaste? {secreto == numero_dado}')

# VERSION 2

        import random
        nombre = ""
        secreto = random.randint(1,100)
        numeros_dados = []   #Snakecase para variables y funciones
        atinado = False
        oportunidades = 3
        
        
        nombre =  input("Ingresa tu nombre:\n")
        print(f'\n**************** {nombre} ********** Adivina el número secreto *************\n')
        #append es método
        numeros_dados.append(int(input("Ingresa un número")))
        numeros_dados.append(int(input("Ingresa otro número")))
        numeros_dados.append(int(input("Ingresa otro número")))
        print(f'los número dados son: {numeros_dados}')
        
        
        #len es funsion
        print(f'{secreto} es el número secreto, tú ingresaste {len(numeros_dados)} números, que fueron: {numeros_dados} atinaste? {secreto in numeros_dados}')
        
        
        indice=int(input("qué indice quieres borrar"))
        borrado = numeros_dados.pop(indice)
        print(numeros_dados)


        numeros_dados.append(int(input("Ingresa otro número")))
        print(numeros_dados.sort(reverse=True))
        
        print(f'el número más aldo dado fue: {max(numeros_dados)} y el menor fue: {min(numeros_dados)}')


# VERSION 3

        import time
        
        print('''-------------------------------------------
        -------ADIVINA EL NÚMERO SECRETO-------------
        ---------TIENES 5 OPORTUNIDADES--------------
        ---------------------------------------------''')
        time.sleep(5)
        # Vamos a iniciar generando el numero secreto, para ello importamos random
        import random
        # Ahora vamos a generar ese número secreto
        numero_secreto = random.randint(1,100)
        
        #Ahora crea las variables donde se almacenará e número que ingrese el usuario y otra con el número de oportunidades que tendrá de adivinar
        num =int(input('Adivina el número secreto'))
        opor = 1
        
        # Vamos a crear el ciclo que se ejecute mientras no se adivie el número y aun queden oportunidades de seguir jugando
        # Recuerda crear una condición que evalue e informe al usuario si el número ingresado es mayor o menor al número secreto
        while numero_secreto != num and opor < 6:
          opor = opor + 1
          if num < numero_secreto:
            print(f'{num} es menor al número secreto')
        
          else:
            print(f'{num} es mayor al número secreto')
            num =int(input('Adivina el número secreto'))
        
        
        # Cuando el usuario le atine o se acaben sus oportunidades entrará a otra condicionante
        if num == numero_secreto:
          print(f'felicidades!!!!! has atinado al número en {opor} oportunidades')
        else:
          print(f'lástima!!!!! se terminaron tus oportunidades, el número secreto era {numero_secreto}')
