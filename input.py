
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

  def setActions(self, actions):
    self.actions = actions

  def getAction(self, key):
    return self.actions[key]

# Class Input asks for input using the getch() for msvcrt package
# parses the input using the input manager associated values

class Input:

  def __init__(self, inputManager = InputManager()):
    self.keys = inputManager.actions.keys()
    pass
    
  def clrBuffer(self):
    while (msvcrt.kbhit()):
      msvcrt.getch()

  def getC(self):
    self.clrBuffer()
    char = msvcrt.getch()

    if char != b'\xe0':
      char = char.decode("utf-8")

    return char

  def getCTest(self):

    self.clrBuffer()
    char = '\0'

    while (char != 'q'):
      char = self.getC() 

      if (char == b'\xe0'): # si le char est un escape char
        char = msvcrt.getch().decode('utf-8')
        if (char == 'K'):
          print("left arrow")
        elif (char == 'H'):
          print("up arrow")
        elif (char == 'M'):
          print("right arrow")
        elif (char == 'P'):
          print("down arrow")
      else:
        print(char)

  def validateChar(self, char):
    return char in self.keys


  def validateCharTest(self):

    keys = {
      97  : print("action1"),
      98  : print("action1"),
      99  : print("action1"),
      100 : print("action1")
    }
    
    for a in range(95, 103):
      if self.validateChar(a):
        print(a, "is in keys")
      else:
        print(a, "is not in keys")

# input = Input()
# input.getCTest()


