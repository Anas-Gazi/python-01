class Person():
  def __init__(self,fname,lname):
    self.fname= fname
    self.lname= lname

  def Printname(self):
    print(self.fname,self.lname)

class Student(Person):
  def __init__(self,fname,lname, year):
    #Person.__init__(self, fname,lname)
    super().__init__(fname,lname)
    self.graduationYear=year

  def welcome(self):
    print("welcome ", self.fname, self.lname, "to the class of ", self.graduationYear)

x=Student("Emon","khan", 2029)
print(x.graduationYear)
x.welcome() 