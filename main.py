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
charac = [Characters.Dalek(2,2,'@',True), Characters.Doctor(10,3,'I', True)]
board  = Board.Board(50,20,charac)

inputMan = im.InputManager()
inputMan.associate('K', board.moveDoc)
# inputMan.associate('K', im.InputManager.sayHi)


game   = Game(board, camera, inputMan)

game.run()




