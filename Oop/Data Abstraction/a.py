#Abstract classes are created using abc module and @abstractmethod decorator

from abc import ABC, abstractmethod

class Great(ABC):
  @abstractmethod
  def say_hello(self):
    pass
class English(Great):
  def say_hello(self):
    return "Hello"
  
g= English()
print(g.say_hello())