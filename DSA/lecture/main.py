# 1. using direct from .. import
from vehicle import Car

# 2. import all the classes
#           from vehicle import *    
# from vehicle import *    

# 3. Using import for the whole file of classes:
#  You can simply import the entire module and then access its classes using the dot notation:
# import vehicle
# my_car = vehicle.Car("Red", "Sedan", "Toyota")

# Creating an instance of the Car class
my_car = Car("Red", "Sedan", "Toyota")

# Accessing and printing attributes using getter methods
print(f"Color: {my_car.getColor()}")
print(f"Model: {my_car.model}")
print(f"Brand: {my_car.brand}")

# Modifying attributes using setter methods
my_car.setColor("Blue")
print(f"Updated Color: {my_car.getColor()}")
