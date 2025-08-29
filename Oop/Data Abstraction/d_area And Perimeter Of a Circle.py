from abc import ABC, abstractmethod

class Shape(ABC):
  @abstractmethod
  def area(self):
    pass

  @abstractmethod 
  def perimeter(self):
    pass

class Circle(Shape):
  def __init__(self, radius):
    self.radius= radius

  def area(self):
    return 3.1416 * self.radius ** 2
  
  def perimeter(self):
    return 2 * 3.1416 * self.radius
  
r= Circle(5)
print(f"Area: {r.area()} \nPerimeter: {r.perimeter()}")