class Animal:
  def sound(self):
    return "some generic sound"
  
class Dog(Animal):
  def sound(srlf):
    return "burk"
  
class Cat(Animal):
  def sound(self):
    return "meaw"
  
Animal = [Dog(), Cat(), Animal()]
for x in Animal:
  print(x.sound())