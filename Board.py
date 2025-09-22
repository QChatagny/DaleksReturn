
import Characters
import os

def clrscr():
  os.system('cls' if os.name == 'nt' else 'clear')

class Board:

  def __init__(self, width, height, characters):
    self.width = width
    self.height = height
    self.characters = characters
    self.map = [['#' for x in range(self.width)] for y in range(self.height)] 

  def actualizeMap(self):
    self.map = [['#' for x in range(self.width)] for y in range(self.height)] 
    for character in self.characters:
      if character.isAlive:
        self.map[character.posY][character.posX] = character.char

  def print(self):
    for lines in self.map:
      for tile in lines:
        print(tile, end="  ")
      print('\n', end="  ")

  def moveDoc(self):
    print("doctor moved")
    for character in self.characters:
      if isinstance(character, Characters.Doctor):
          character.moveLeft()


  # code copié de stackoverflow, nt c'est windows else unix based 'clear'
  def render(self):
    self.actualizeMap()
    clrscr()
    self.print()

  
  

  
  

  


    

