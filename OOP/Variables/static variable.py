# places to delete static variable

# within the class directly but outside the method or constructor
class parent:
    a = 10


print(parent.__dict__)


# inside the constructor we can declare static variable by classname.variable name

class test:
    def __init__(self):
        test.b = 100


t = test()
print(test.__dict__)


# inside the instance maehtod also static variable can be declared

class student:
    def __init__(self):
        student.d = 200

    def m(self):
        student.c = 900


u = student()


# inside the class method either using cls or class classname
class school:
    @classmethod
    def m1(cls):
        cls.y = 999


school.m1()
print(school.__dict__)


# inside static method by using class classname

class covid:
    @staticmethod
    def m2():
        covid.l = 344


covid.m2()
print(covid.__dict__)

# outside of the class by using class classname
