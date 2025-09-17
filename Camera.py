

class Camera: 

  def __init__(self, posX, posY, width, height):
    self.posX = posX
    self.posY = posY
    self.width = width
    self.height = height

  def moveUp(self):
    self.posY -= 1

  def moveDown(self):
    self.posY += 1

  def moveLeft(self):
    self.posX -= 1

  def moveRight(self):
    self.posX += 1

