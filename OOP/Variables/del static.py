# how to delete static variable: either by class name or cls
class test:
    a = 900
    b = 9000

    @classmethod
    def m(cls):
        del cls.a  # or del test.a


# test.m()
del test.a
# del cls.b # out side the class we can not use the cls method to delete
print(test.__dict__)


# example 2
class student:
    a = 100

    def __init__(self):
        student.b = 20
        del student.a

    def m(self):
        student.c = 90
        del student.b

    @classmethod
    def classm(cls):
        student.d = 89
        del student.c

    @staticmethod
    def staticm():
        student.e = 67
        del student.d


u = student()
u.m()
u.classm()  # we can call by class name or obj ref but recommended to use class name as they are not related to the obj
u.staticm()
del student.e
print(student.__dict__)
