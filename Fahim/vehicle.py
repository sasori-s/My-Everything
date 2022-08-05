class Vehicle:
    def __init__(self, brand, model_name, color):
        self.brand = brand
        self.model_name = model_name
        self.color = color

    def describe(self):
        print(f"{self.model_name} vehicle is from {self.brand} coloured {self.color}")

class Car(Vehicle):
    def __init__(self, brand, model_name, color):
        super().__init__(brand, model_name, color)
        print("This is a car")




if __name__ == '__main__':
    vehicle = Vehicle("Scania", 'Elite', 'white')
    vehicle.describe()
    car = Car("BMW", 'M3', 'Black')
    car.describe()