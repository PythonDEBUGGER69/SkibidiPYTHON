
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def print_details(self):
        print(f"Welcome! This the W@fflersd main genarel {self.name} he earns {self.salary} and manages the {self.department} department.")

x = Manager("Sibisis", 180, "Terror")
x.print_details()
