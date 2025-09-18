import Board
import Characters
import Camera
import os
import time

class Game():

  def __init__(self, board, camera):
    self.board = board
    self.camera = camera 
    

  def run(self):

    while(1):
      self.board.actualizeMap()
      self.board.print()
      time.sleep(1)
      clrscr()

def clrscr():
  os.system('cls' if os.name == 'nt' else 'clear')


camera = Camera.Camera(0,0,0,0)
charac = [Characters.Character(2,2,'@', True), Characters.Character(3,3,'@', True)]
board  = Board.Board(50,10, charac)
game   = Game(board, camera)

game.run()

