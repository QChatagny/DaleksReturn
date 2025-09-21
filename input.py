
import msvcrt
  

# Class Input asks for input using the getch() for msvcrt package
# parses the input using the input manager associated values

class Input:

  def __init__(self):
    pass
    
  @staticmethod
  def clrBuffer(self):
    while (msvcrt.kbhit()):
      msvcrt.getch()

  @staticmethod
  def getC(self):
    self.clrBuffer()
    char = msvcrt.getch()

    if (char == b'\xe0'): # si le char est un escape char
      char = msvcrt.getch().decode('utf-8') # decode to string
    else:
      char = char.decode('utf-8')
    
    return char

  @staticmethod
  def getCTest():

    Input.clrBuffer()
    char = '\0'

    while (char != 'q'):
      char = Input.getC() 

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

