
import msvcrt
  

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
    return msvcrt.getch()


  def getCTest(self):

    self.clrBuffer()
    char = '\0'

    while (char != 'q'):
      char = self.getC() 

      if (char == b'\xe0'): # si le char est un escape char
        char = msvcrt.getch().decode('utf-8') # decode to string
        if (char == 'K'):
          print("left arrow")
        elif (char == 'H'):
          print("up arrow")
        elif (char == 'M'):
          print("right arrow")
        elif (char == 'P'):
          print("down arrow")
      else:
        char = char.decode("utf-8")
        print(char)




# input = Input()
# input.getCTest()

# Class InputManager
# Retrieves input and assigns them to function
# associated with the input.
# works with a dictionary called actions
# A function associates pairs of key -> function 
# at the index of the char corresponding to the key pressed
# with bit[0] returns the int corresponding to the char

class InputManager:

  def __init__(self):
    self.actions = {}

  def associate(self, char, function):
    self.actions[char] = function

  def setActions(self, actions):
    self.actions = actions

# calls a function from the dictionary
  def getAction(self, key, param):
    return self.actions[key](param)

  def listen():
    
    while (1):
      pass

  def validateChar(self, char):
    return char in self.actions.keys()

  def validateCharTest(self):

    keys = {
      97  : print,
      98  : print,
      99  : print,
      100 : print
    }
    
    for a in range(95, 103):
      if self.validateChar(a):
        print(a, "is in keys")
      else:
        print(a, "is not in keys")