class Vehicle(object):


    def _init_(self, Brand_name, color,model_name:int):
        self.name = Brand_name
        self.color = color
        self.model_name=model_name

    def display(self):
        print(self.name)
        print(self.color)
        print(self.model_name)



class Car(Vehicle):
   pass

a = Car("Audi" , "Black",222)
a.display()