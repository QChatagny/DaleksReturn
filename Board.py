
import Characters
import os
from enum import Enum 

def clrscr():
  os.system('cls' if os.name == 'nt' else 'clear')

class Board:

  class CharacterEnum:
    DOC = 0
    CASE_VIDE = 0
    DALEK = 1

  def pin():
    print("alo")

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

  def moveDocLeft(self):
    for character in self.characters:
      if isinstance(character, Characters.Doctor):
          character.moveLeft()

  def moveDocRight(self):
    for character in self.characters:
      if isinstance(character, Characters.Doctor):
          character.moveRight()
          break
    for character in self.characters:
      if isinstance(character, Characters.Dalek):
        character.moveDaleksToDoc()

  def moveDocUp(self):
    for character in self.characters:
      if isinstance(character, Characters.Doctor):
          character.moveUp()

  def moveDocDown(self):
    for character in self.characters:
      if isinstance(character, Characters.Doctor):
          character.moveDown()

  def comparePosition(character1, character2):
    return character1.posX == character2.posX and character1.posY == character2.posY
    

  def collision(self):
    for character in self.characters:
      for testedCharacter in self.characters:
        if character == testedCharacter:
          pass
        else:
          pass




  # code copié de stackoverflow, nt c'est windows else unix based 'clear'
  def render(self):
    self.actualizeMap()
    clrscr()
    self.print()

  
Board.pin();



  
  

  
  

  


    

