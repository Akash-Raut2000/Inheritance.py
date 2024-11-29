# Base Class
class Vehicle:
    def move(self):
        return "I can move!"

# Derived Class
class Car(Vehicle):
    def wheels(self):
        return "I have 4 wheels."

# Using the classes
car = Car()
print(car.move())    # Inherited method
print(car.wheels())  # Method from derived class
