#parent class


class Person:
    def __init__(self, fname, lname):
        self.firstname= fname
        self.lastname =lname
    def printname(self):
        print(self.firstname, self.lastname)

x= Person ("katrina", "batin")
x.printname()


#child class

class Student (Person):
    pass

x= Student("ricci", "batin")
x.printname()



#SINGLE INHERITANCE
#base class
class Vehicle:
    def Vehicle_info(self):
        print('inside Vehicle class')
# child class
class Car(Vehicle):
    def car_info(self):
        print('inside Car class')
#create object of a car
car = Car()
car.Vehicle_info()
car.car_info()

#MULTIPLE INHERITANCE

#Parent Class 1
class Person:

    def person_info(self, name, age):
        print('Inside Person_class')
        print('Name:', name, 'Age:', age )

#Parent Class 2
class Company:
    def company_info(self, company_name, location):
        print('Inside Company class')
        print('Name:', company_name, 'location:', location)

#Child class
class Employee(Person, Company):
    def Employee_info(self, salary, skill):
        print('inside Employee class')
        print('Salary:', salary, 'skill:', skill )

#create object of Employee
emp = Employee()

#access data
emp.person_info('kat',21)
emp.company_info('google', 'tabi lang')
emp.Employee_info(30, 'matulog')


#MULTILEVEL INHERITANCE

#Base Class
class Vehicle:
    def Vehicle_info(self):
        print('inside Vehicle class')
#Child class
class Car(Vehicle):
    def Car_info(self):
        print('inside Car class')
#Child class 2
class SportsCar(Car):
    def SportsCar_info(self):
        print('inside SportsCar class')

s_car= SportsCar()

s_car.Vehicle_info()
s_car.Car_info()
s_car.SportsCar_info()


#HIERACHICAL INHERITANCE
class Vehicle:
    def info(self):
        print("This is Vehicle")

class Car:
    def car_info(Self, name):
        print("Car name is:", name)

class Truck:
    def truck_info(Self, name):
        print("Truck name is:", name)

obj1 =Vehicle()
obj1.info()
obj1 = Car()
obj1.car_info("BMW")

obj2 =Vehicle()
obj2.info()
obj2= Truck()
obj2.truck_info("Ford")

#HYBRID INHERITANCE

class Vehicle:
    def vehicle_info(self):
        print('inside Vehicle class')

class Car(Vehicle):
    def car_info(self):
        print('inside Car class')

class Truck(Vehicle):
    def truck_info(self):
        print('inside Truck class')

class Sportscar(Car,Vehicle):
    def sportscar_info(self):
        print('inside Sportscar class')

s_car = SportsCar()
s_car.Vehicle_info()
s_car.Car_info()
s_car.SportsCar_info()

#SUPER FUNCTION IN SINGLE INHERITANCE
class Company:
    def company_name(self):
        return'Google'

    