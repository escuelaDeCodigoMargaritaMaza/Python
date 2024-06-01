#VERSION 1
    
    nombre = ""
    secreto = 15
    numero_dado = 0   #Snakecase para variables y funciones
    atinado = False
    oportunidades = 3
    
    
    nombre = input("Ingresa tu nombre:\n")
    print(f'\n**************** {nombre} ********** Adivina el número secreto *************\n')
    numeroDado=int(input("Ingresa tú  número: "))
    
    print(f'{secreto} es el número secreto, tú ingresaste {numero_dado}, atinaste? {secreto == numero_dado}')
