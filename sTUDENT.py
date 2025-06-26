
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)

x = Person("Hadi", "Naqvi")
x.printname()

#childclass/subclass
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
y = Student ("Hadi", "Naqvi", 2023)
y.printname()
