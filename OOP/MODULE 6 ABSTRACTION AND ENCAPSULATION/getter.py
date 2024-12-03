
#GETTER

class Student:
    def __init__(self, name, age):
        self.name= name 
        self.__age= age

    #getter method
    def get_age(self):
        return self.__age

    #setter method
    def set_age(self, age):
        self.__age = age

stud = Student('Kat', 14)

#retrieving age using getter
print('Name:', stud.name, stud.get_age())

#changing age using setter
stud.set_age(16)

#retrieving age using getter
print('Name:', stud.name, stud.get_age())


class Student:
    def __init__(self, name, stud_no, age):
        #private method
        self.name = name
        #private members to restrict access
        #avoid direct modification
        self.__stud_no =  stud_no
        self.__age = age

    def show(self):
        print('Student Details:', self.name, self.__stud_no)

    #getter methods
    def get_stud_no(self):
        return self.__stud_no

    #setter method to modify data member
    #condition to allow data modification with rules
    def set_stud_no(self, number):
        if number > 50:
            print('Invalid stu no. Please set correct number')
        else:
            self.__stud_no = number

Kat = Student('Kat', 10, 15)

#before modify
Kat.show()
#changing student number using setter
Kat.set_stud_no(150)

Kat.set_stud_no(50)
Kat.show()