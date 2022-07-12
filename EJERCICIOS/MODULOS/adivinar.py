# Este es el juego de adivinar el número.
from numero import numero
from error import *
intentosRealizados = 0
print('¡Hola! ¿Cómo te llamas?')
miNombre = input()
print('Bueno, ' + miNombre + ', estoy pensando en un número entre 1 y 20.')
while intentosRealizados < 6:
  print('Intenta adivinar.') # Hay cuatro espacios delante de print.
  estimación = input()
  estimación = int(estimación)
  intentosRealizados = intentosRealizados + 1
  if estimación < numero:
      print(mensaje_error)
      print('Tu estimación es muy baja.') # Hay ocho espacios delante de print.
  if estimación > numero:
      print(mensaje_error)
      print('Tu estimación es muy alta.')
  if estimación == numero:
      break
  if estimación == numero:
      intentosRealizados = str(intentosRealizados)
      print(mensaje_felicitacion)
      print('¡Buen trabajo, ' + miNombre + '! ¡Has adivinado mi número en ' + intentosRealizados + ' intentos!')
  if estimación != numero:
      numero = str(numero)
      print('Pues no. El número que estaba pensando era ' + numero)