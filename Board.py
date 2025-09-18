
class Board:

  def __init__(self, width, height, characters):
    self.width = width
    self.height = height
    self.characters = characters
    self.boardArray = [['#' for x in range(self.width)] for y in range(self.height)] 

  def actualizeCharactersBoardArray(self):
    for character in self.characters:
      if character.isAlive:
        self.boardArray[character.posX][character.posY] = character.char

  def printBoard(self):
    for lines in self.boardArray:
      for tile in lines:
        print(tile, end=" ")
      print('\n', end=" ")

  
  

  


    

