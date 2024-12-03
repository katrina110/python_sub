
#public method to access private members

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary= salary
    def show(self):
        print('Name:', self.name, 'Salary:', self.__salary)  

emp = Employee('Kat', 20000)
emp.show()