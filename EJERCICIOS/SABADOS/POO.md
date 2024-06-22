# PROGRAMACION ESTRUCTURADA
## usando variables

    nombre = input("Ingrese su nombre: ")
    telefono = input("Ingrese su teléfono: ")
    correo_electronico = input("Ingrese su correo electrónico: ")
    sexo = input("Ingrese su sexo (M/F): ")
    edad = input("Ingrese su edad: ")
    
    #Imprimir los datos del usuario
    print("\nDatos del usuario:")
    print(f"Nombre: {nombre}")
    print(f"Teléfono: {telefono}")
    print(f"Correo Electrónico: {correo_electronico}")
    print(f"Sexo: {sexo}")
    print(f"Edad: {edad}")

## usando listas

    #Solicitar datos al usuario y añadirlos a la lista
    datos_usuario.append(input("Ingrese su nombre: "))
    datos_usuario.append(input("Ingrese su teléfono: "))
    datos_usuario.append(input("Ingrese su correo electrónico: "))
    datos_usuario.append(input("Ingrese su sexo (M/F): "))
    datos_usuario.append(input("Ingrese su edad: "))
    
    #Imprimir los datos del usuario
    print("\nDatos del usuario:")
    print(f"Nombre: {datos_usuario[0]}")
    print(f"Teléfono: {datos_usuario[1]}")
    print(f"Correo Electrónico: {datos_usuario[2]}")
    print(f"Sexo: {datos_usuario[3]}")
    print(f"Edad: {datos_usuario[4]}")

## usando listas para cada dato

    #Listas para almacenar los datos de múltiples usuarios
    nombres = []
    telefonos = []
    correos_electronicos = []
    sexos = []
    edades = []
    
    while True:
        #Solicitar datos al usuario y añadirlos a las listas correspondientes
        nombres.append(input("Ingrese su nombre: "))
        telefonos.append(input("Ingrese su teléfono: "))
        correos_electronicos.append(input("Ingrese su correo electrónico: "))
        sexos.append(input("Ingrese su sexo (M/F): "))
        edades.append(input("Ingrese su edad: "))
        
        #Preguntar al usuario si desea agregar otro registro
        continuar = input("¿Desea agregar otro usuario? (s/n): ").lower()
        if continuar != 's':
            break
    
    #Imprimir los datos de todos los usuarios
    print("\nDatos de los usuarios:")
    for i in range(len(nombres)):
        print(f"\nUsuario {i + 1}:")
        print(f"Nombre: {nombres[i]}")
        print(f"Teléfono: {telefonos[i]}")
        print(f"Correo Electrónico: {correos_electronicos[i]}")
        print(f"Sexo: {sexos[i]}")
        print(f"Edad: {edades[i]}")


# POO

    #creacion de la clase
    class Usuario():
        def __init__(self,nombre,telefono,correo,sexo,edad):
            self.nombre= nombre
            self.telefono= telefono
            self.correo= correo
            self.sexo = sexo
            self.edad = edad
    
        def mostrar(self):
          print( f'''************DATOS DEL USUARIO **********
          nombre : {self.nombre}
          telefono: {self.telefono}
          correo: {self.correo}
          sexo: {self.sexo}
          edad: {self.edad}''')
    
        def modificar(self):
            print("Ingrese los datos del usuario a modificar:")
            self.nombre = input("Nombre: ")
            self.telefono = input("Teléfono: ")
            self.correo_electronico = input("Correo Electrónico: ")
            self.sexo = input("Sexo: ")
            self.edad = int(input("Edad: "))
    
    
        #instanciamos el objeto
        usuario1 = Usuario("David","54545454","sadsa@gsd","m",25)    
        #accedo a los atributos
        #print(usuario1.nombre)
        usuario1.mostrar()
        usuario1.modificar()
        usuario1.mostrar()


## HERENCIA, POLIMORFISMO Y ENCAPSULAMIENTO

https://colab.research.google.com/drive/15F7WtuAFIE8xfFTA4Aqj883Ne0GUIGD-?usp=sharing
