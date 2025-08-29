class Student:
  def __init__(self, fname, lname):
    self.fname= fname
    self.lname=lname

  def printname(self):
    print(self.fname, self.lname)

x= Student("Rahim", "Hossain")
x.printname()