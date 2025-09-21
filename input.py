
import msvcrt

# Class InputManager
# Retrieves input and assigns them to function
# associated with the input.
# works with a dictionary called actions
# a function associates pairs of key -> function 
# at the index of the char corresponding to the key pressed
# with bit[0] returns the int corresponding to the char

class InputManager:

  def __init__(self):
    self.actions = {}

  def associate(self, char, function):
    self.actions[char] = function

# Class Input asks for input using the getch() for msvcrt package
# parses the input using the input manager associated values
class Input:

  def __init__(self, inputManager):
    self.keys = inputManager.actions.keys()
    pass
    
  def getC():
    char = msvcrt.getch().decode("utf-8")
    return char

  def clrBuffer():
    while (msvcrt.kbhit()):
      msvcrt.getch()

  def getInputTest(self):

    char = self.getC() 

    if (char == b'\xe0'): # si le char est un escape char

      if (char == b'K'):
        print("left arrow")

      elif (char == b'H'):
        print("up arrow")

      elif (char == b'M'):
        print("right arrow")

      elif (char == b'P'):
        print("down arrow")

    else:
      print(char)


  