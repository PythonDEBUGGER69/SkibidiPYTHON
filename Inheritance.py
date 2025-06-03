# Inheritance
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.fname, self.lname,
              "to the class of", self.graduationyear)

x = Student("Hadi", "Naqvi", 2035)
x.welcome()
