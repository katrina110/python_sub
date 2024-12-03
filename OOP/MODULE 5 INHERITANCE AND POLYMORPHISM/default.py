#default
class Employee:
    
    def display(self):
        print('instant display')

emp = Employee()
emp.display()

#non-parametized
class Company:
    def __init__(self):
        self.name = 'wew'
        self.address = 'dyan lang'
    def show(self):
        print('Name:', self.name, 'Address:', self.address)

cmp =Company()
cmp.show()

#paranetized

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def show(self):
        print(self.name, self.age, self.salary)
    
Kat =Employee('Kat', 21, 20000)
Kat.show()

Ricci =Employee('Ricci', 23, 25000)
Ricci.show()


