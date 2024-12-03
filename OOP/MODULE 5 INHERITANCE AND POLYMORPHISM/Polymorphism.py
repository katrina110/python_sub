student= ['kat','ricci','batin']
school='sa tabi lang'

print(len(student))
print(len(school))

class Vehicle:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price
    
    def show(self):
        print('Details:', self.name, self.color, self.price)

    def max_speed(self):
        print('Vehicle max speed is 150')
        
    def change_gear(self):
        print('Vehicle change gear 69 gear')

#inherit vehicle class
class Car(Vehicle):
    def max_speed(self):
        print('Car max speed 200')

    def change_gear(self):
        print('Vehicle change gear 96 gear')

# car object
car =Car('Car x1', 'red', 20000)
car.show()
#calls methods from Car class
car.max_speed()
car.change_gear()

Vehicle = Vehicle('Truck 123', 'Pink', 10000)
Vehicle.show()
Vehicle.max_speed()
Vehicle.change_gear()