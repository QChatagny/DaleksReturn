
class Board:

  def __init__(self, width, height, characters):
    self.width = width
    self.height = height
    self.characters = characters
    self.map = [['#' for x in range(self.width)] for y in range(self.height)] 

  def actualizeMap(self):
    for character in self.characters:
      if character.isAlive:
        self.map[character.posX][character.posY] = character.char

  def print(self):
    for lines in self.map:
      for tile in lines:
        print(tile, end="  ")
      print('\n', end="  ")

  
  

  


    

