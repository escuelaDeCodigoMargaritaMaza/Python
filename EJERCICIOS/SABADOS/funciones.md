    def menu():
        print("menu de operaciones")
        print("1. suma")
        print("2. resta")
        print("3. multiplicación")
        print("4. división")
        print("5. salir")
    
        op = int(input("Ingresa númeor de operación"))
        if op == 1:
            suma()
        elif op == 2:
            resta()
        elif op == 3:
            multiplicacion()
        elif op == 4:
            division()
        elif op == 5:
            exit()
        else:
            print("opcion invalida")
    
    def solicitar():
        num1 = int(input("Ingresa el numero 1"))
        num2 = int(input("Ingresa el numero 2"))
        return num1,num2
    
    def suma():
        print("Operacion suma: ")
        print(" ")
        solicitar()
        num1,num2=solicitar()
        print("RESULTADO: ",num1 + num2)
    
    def resta():
        print("Operacion resta: ")
        print(" ")
        solicitar()
        num1,num2=solicitar()
        print("RESULTADO: ",num1 - num2)
    
    def multiplicacion():
        print("Operacion multiplicación: ")
        print(" ")
        solicitar()
        num1,num2=solicitar()
        print("RESULTADO: ",num1 * num2)
    
    def division():
        print("Operacion division: ")
        print(" ")
        solicitar()
        num1,num2=solicitar()
        print("RESULTADO: ",num1 / num2)
    
    
    while True:
        menu()
