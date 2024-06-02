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

    import random
    import time
    nombre = ""
    secreto = random.randint(1,100)
    numeros_dados = []   #Snakecase para variables y funciones
    numero_dado=0
    atinado = False
    oportunidades = 3
    
    
    nombre =  input("Ingresa tu nombre:\n")
    print(f'\n**************** {nombre} ********** Adivina el número secreto *************\n')
    time.sleep(5)
    
    numero_dado = (int(input("Ingresa un número")))
    numeros_dados.append(numero_dado)
    while numero_dado != secreto and oportunidades > 1:
          print(f'Has ingresado los números: {numeros_dados}')
          oportunidades = oportunidades - 1  #oportunidades=-1
          if secreto < numero_dado:
            print(f'{numero_dado} es mayor al número secreto')
            numero_dado =int(input('Adivina el número secreto'))
            numeros_dados.append(numero_dado)
        
          else:
            print(f'{numero_dado} es menor al número secreto')
            numero_dado =int(input('Adivina el número secreto'))
            numeros_dados.append(numero_dado)
    
    # Cuando el usuario le atine o se acaben sus oportunidades entrará a otra condicionante
    if numero_dado == secreto:
      print(f'felicidades!!!!!{nombre} has atinado al número en {oportunidades} oportunidades')
    else:
      print(f'lástima!!!!! {nombre }se terminaron tus oportunidades, el número secreto era {secreto}')
