
class Character:
  
  nbCharacters = 0

  def __init__(self, posX, posY, char ,isAlive):
    Character.nbCharacters += 1
    self.posX = posX
    self.posY = posY
    self.isAlive = isAlive
    self.char = char

  def moveUp(self):
    self.posY -= 1

  def moveDown(self):
    self.posY += 1

  def moveLeft(self):
    self.posX -= 1

  def moveRight(self):
    self.posX += 1
      
class Dalek(Character):
  nbDaleks = 0

  def __init__(self, posX, posY, char, isAlive):
    Dalek.nbDaleks += 1
    super().__init__(posX, posY, char, isAlive)

class Doctor(Character):

  def __init__(self, posX, posY, char, isAlive):
    super().__init__(posX, posY, char, isAlive)
      


