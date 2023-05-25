from abc import ABC, abstractmethod

# Abstract class representing a vehicle
class Vehicle(ABC):
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

# Concrete class representing a Car
class Car(Vehicle):
    def start(self):
        print("Car started.")

    def stop(self):
        print("Car stopped.")

# Concrete class representing a Motorcycle
class Motorcycle(Vehicle):
    def start(self):
        print("Motorcycle started.")

    def stop(self):
        print("Motorcycle stopped.")

# Usage of the Vehicle hierarchy
car = Car("Toyota", "Red")
car.start()
car.stop()

motorcycle = Motorcycle("Honda", "Blue")
motorcycle.start()
motorcycle.stop()
