# Inheritance
class Vehicle:
    def __init__(brand, speed, color):
        self.brand = brand
        self.speed = speed
        self.color = color

    def printname(self):
        print(self.brand, self.speed, self.color)

class Car(Vehicle):
    def __init__(self, brand, speed, color, model, year):
        super().__init__(brand, speed, color)
        self.model = model
        self.year = year

    def print_details(self):
        print(f"Welcome! This is a {self.year} {self.brand} {self.model} in {self.color} color with top speed {self.speed}.")

x = Car("Lamborgini", 180, "Red", "Veneno", 2022)
x.print_details()