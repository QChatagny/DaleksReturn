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

  @staticmethod
  def sayHi():
    print("hi")

# calls a function from the dictionary
  def getAction(self, key):
    return self.actions[key]()

  def validateChar(self, char):
    return char in self.actions.keys() #returns true if char is a key from the actions dictionary

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

# 
  def listen(self,char):
    if self.validateChar(char):
      self.getAction(char)
      return True
    else:
      return False