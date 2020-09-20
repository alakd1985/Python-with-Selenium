# Anywhere either with in the class or outside of class we can modify by using classname.
# But inside class method, by using cls variable.

class student:
    a = 10

    # inside constructor: by using class name
    def __init__(self):
        student.a = 20
        print('Modifying static variable by class name inside the constructor', student.a)

    # inside instance method: by using class name
    def m(self):
        student.a = 30
        print('Modifying static variable by class name inside the instance method', student.a)

    # inside class method: by using either cls variable or class name
    @classmethod
    def m2(cls):
        student.a = 40
        print('Modifying static variable by cls inside the class method', cls.a)
        print('Modifying static variable by class name inside the class method', student.a)

    # inside static method: by using class name
    @staticmethod
    def m3():
        student.a = 50
        print('Modifying static variable by class name inside the static method', student.a)


u = student()
u.m()
student.m2()
student.m3()

# From outside of class: by using either object reference or class name
# print('Accessing static variable by class name outside the class',student.e)
student.a = 70
print('Accessing static variable by obj ref outside the class', student.a)
