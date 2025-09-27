import Board
import Characters
import Camera
import time
import input as i
import InputManager as im

class Game():

  def __init__(self, board, camera, inputManager):
    self.board = board
    self.camera = camera 
    self.inputManager = inputManager

  def runMapTest(self):
    while(1):
      self.render() 
      time.sleep(0.3333)

  def runInManTest(self): # test for input manager
    char = '\0'
    self.board.render()
    while char != 'q':
      char = i.Input.getC()
      if self.inputManager.listen(char):
        self.board.render()

  def run(self):
    # self.runMapTest()
    self.runInManTest()
    pass



camera = Camera.Camera(0,0,0,0)
charac = [Characters.Dalek(0,1,'@',True),
          Characters.Dalek(0,2,'@',True),
          Characters.Dalek(0,3,'@',True),
          Characters.Dalek(0,4,'@',True),
          Characters.Dalek(0,5,'@',True),
          Characters.Dalek(0,6,'@',True),
          Characters.Doctor(10,3,'I', True)]
board  = Board.Board(50,20,charac)

inputMan = im.InputManager()
inputMan.associate('K', board.moveDocLeft)
inputMan.associate('M', board.moveDocRight)
inputMan.associate('H', board.moveDocUp)
inputMan.associate('P', board.moveDocDown)


game   = Game(board, camera, inputMan)

game.run()




