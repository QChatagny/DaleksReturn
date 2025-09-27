
class Character:
  
  nbCharacters = 0

  def __init__(self, char ,isAlive):
    Character.nbCharacters += 1
    self.isAlive = isAlive
    self.char = char
      
class Dalek(Character):
  nbDaleks = 0

  def __init__(self, char, isAlive):
    Dalek.nbDaleks += 1
    super().__init__(char, isAlive)
  
  ## MOVE TO BOARD LOGIC
  # def directionTo(self, point):
  #   isUp = False
  #   isRight = False

  #   if self.posX > point.posX:
  #     isRight = True

  #   if self.posY > point.posY:
  #     isUp = True

  #   return isUp, isRight
  
  # def directionToDocTest(self):
  #   doc = Doctor(10,10, '@', True)
  #   dal = Dalek(0,0, '*', True)
  #   print(dal.directionTo(doc))
  
  # def moveToward(self, tuple):
  #   if tuple[0]:
  #     self.moveUp()
  #   else:
  #     self.moveDown()

  #   if tuple[1]:
  #     self.moveRight()
  #   else:
  #     self.moveDown()

  # def moveDaleksToDoc(self, doc):
  #   dir = self.directionTo(doc)
  #   self.moveToward(dir)


class Doctor(Character):

  def __init__(self, char, isAlive):
    super().__init__(char, isAlive)



