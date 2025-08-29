class Dog:
  #class variable
  species = "canine"  #class

  def __init__(self,name,age):
    self.name= name
    self.age=age

#object
dog1 = Dog("Buddy",3)
#accessing
print(dog1.name)
print(dog1.age)
print(dog1.species)

#updating
dog1.name="gandu"
print(dog1.name)

Dog.species = "halulu"
print(dog1.species)
