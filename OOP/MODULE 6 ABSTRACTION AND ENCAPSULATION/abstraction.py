from abc import ABC, abstractclassmethod

class parent(ABC):
    @abstractclassmethod
    def fun1(self):
        pass
    def fun2(self):
        print("This is a parent class")

#creating a subclass or child class or derived class
class child(parent):
    def fun1(self):
        print("This is child class")

obj = child()
obj.fun1()
obj.fun2()


class Employee:
    #constructor
    def __init__(self, name, salary, project):
        #data members
        self.name = name
        self.salary = salary
        self.project = project
    
    #method
    # to display employee's details
    def show(self):
        print('Name:', self.name, 'Salary:', self.salary,'Project:', self.project)

    def work(self):
        print(self.name, 'is working on', self.project)

#creating object
emp= Employee('Kat', 25000, 'MPL')

emp.show
emp.work

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary= salary


emp = Employee('Kat', 20000)

print('Name:', emp.name)
#direct access to private member using name mangling
print('Salary:', emp._Employee__salary)


#public method to access private members

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary= salary
    def show(self):
        print('Name:', self.name, 'Salary:', self.__salary)  

emp = Employee('Kat', 20000)
emp.show()


#protected member
class Company:
    def __init__(self):
        self._project = "Mpl"

class Employee:
    def __init__(self, name):
        self.name = self
        Company.__init__(self)

    def show(self):
        print("Employee name:", self.name)
        print("Working project:", self._project)

c = Employee('Kat')
c.show()

print('Project:', c._project)



