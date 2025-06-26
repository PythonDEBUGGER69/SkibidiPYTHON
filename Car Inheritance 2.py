class  Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def printcarinfo(self):
        print(self.color, self.brand)

a = Car("Red", "Lamborghini")
a.printcarinfo()

#childclass/subclass
class  Lamborghini(Car):
    def __init__(self,  color, brand, model):
        super().__init__(color, brand)
        self.model = model
b = Lamborghini ("Yellow", "Lamborghini", "Aventador")
b.printcarinfo()
