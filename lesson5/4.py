# Create a Vehicle class with a method move(). 
# Create two child classes, Car and Bicycle, that override move() to describe their unique ways of moving (e.g., driving and pedaling).

class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} is moving.")

class Car(Vehicle):
    def move(self):
        print(f"{self.name} is driving on the road.")

class Bicycle(Vehicle):
    def move(self):
        print(f"{self.name} is being pedaled.")

vehicle = Vehicle("Generic Vehicle")
car = Car("Sedan")
bicycle = Bicycle("Mountain Bike")


vehicle.move()
car.move()
bicycle.move()