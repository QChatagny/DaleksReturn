import Board
import Characters
import Camera
import os
import time
import input as i

class Game():

  def __init__(self, board, camera, inputManager):
    self.board = board
    self.camera = camera 
    self.inputManager = inputManager

  def run(self):
    while(1):
      self.board.actualizeMap()
      self.board.print()
      time.sleep(0.3333)
      clrscr()

# code copié de stackoverflow, nt c'est windows else unix based 'clear'
def clrscr():
  os.system('cls' if os.name == 'nt' else 'clear')


camera = Camera.Camera(0,0,0,0)
charac = [Characters.Dalek(2,2,'@',True), Characters.Doctor(3,3,'I', True)]
board  = Board.Board(50,10,charac)
game   = Game(board, camera)

game.run()




