class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")

car1 = Car("Lamborgini", "Veneno")
boat1 = Boat("Yamaha", "touring 20") 
plane1 = Plane("Ibixa", "747")

for x in (car1, boat1, plane1):
    x.move()  
