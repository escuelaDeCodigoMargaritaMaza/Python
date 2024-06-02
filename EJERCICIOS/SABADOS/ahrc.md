import random

class Ahorcado:
    def __init__(self):
        self.palabras = [
            "python",
            "programacion",
            "objetos",
            "ahorcado",
            # Agrega más palabras aquí
        ]
      self.palabra_secreta = self.elegir_palabra_aleatoria()
      self.intentos = 6
      self.letras_adivinadas = set()

  def elegir_palabra_aleatoria(self):
      return random.choice(self.palabras)

  def mostrar_palabra(self):
      palabra_mostrada = ""
      for letra in self.palabra_secreta:
          if letra in self.letras_adivinadas:
              palabra_mostrada += letra
          else:
              palabra_mostrada += "_"
      return palabra_mostrada

  def adivinar_letra(self, letra):
      if letra in self.palabra_secreta:
          self.letras_adivinadas.add(letra)
          return True
      else:
          self.intentos -= 1
          return False

  def dibujar_ahorcado(self):
      dibujo = [
          "+---+",
          "|   |",
          "|   " + ("O" if self.intentos < 6 else ""),
          "|  " + ("/|\\" if self.intentos < 5 else ""),
          "|  " + ("/ \\" if self.intentos < 4 else ""),
          "|",
          "=========",
      ]
      return "\n".join(dibujo[:7 - self.intentos])

  def jugar(self):
      print("¡Bienvenido al juego del ahorcado!")
      while self.intentos > 0:
          print("\nPalabra: " + self.mostrar_palabra())
          print(self.dibujar_ahorcado())
          letra = input("Ingresa una letra: ").lower()
          if letra in self.letras_adivinadas:
              print("Ya adivinaste esa letra. Intenta con otra.")
          elif self.adivinar_letra(letra):
              print("¡Correcto! La letra está en la palabra.")
          else:
              print("Incorrecto. Pierdes un intento.")
      print("\nLa palabra secreta era:", self.palabra_secreta)
      print("¡Gracias por jugar!")

# Ejecutar el juego
if __name__ == "__main__":
  juego = Ahorcado()
  juego.jugar()
