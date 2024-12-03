class Student:
    school_name = 'katkat school'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print('Student:', self.name, self.age, Student.school_name)

    def change_age(self, new_age):
        self.age = new_age

    def modify_school_name(cls, new_name):
        cls.school_name = new_name  

s1 = Student("kat", 21)
s1.show()
s1.change_age(18)

