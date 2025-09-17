import Board
import Characters
import Camera
import os
import time

class game():

  def __init__(self, board, camera):
    pass

def clrscr():
  os.system('cls' if os.name == 'nt' else 'clear')

def run():

  charac = [Characters.Character(2,2,'@', True), Characters.Character(2,2,'@', True)]
  camera = Camera.Camera(0,0,0,0)
  board  = Board.Board(50,10,camera, charac)

  while(1):
    board.printBoard()
    time.sleep(0.3333)
    clrscr()

run()
