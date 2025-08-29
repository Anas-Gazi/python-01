from abc import ABC, abstractmethod

class Vehicle(ABC):
  @abstractmethod
  def start(self):
    pass

  @abstractmethod
  def stop(self):
    pass

class Car(Vehicle):
  def start(self):
    print("Car engine started")
  
  def stop(self):
    print("Car engine Stoped")

x = Car()
x.start()
x.stop()