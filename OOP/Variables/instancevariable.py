# inside constructor,inside instance method by using self and outside the class
# by using obj ref variable we can declare instance variable
class test:
    def __init__(self):
        # instance variable
        self.a = 10
        self.b = 20


t = test()
print(t.__dict__)


# inside the instance method

class student:
    def __init__(self):
        self.g = 200
        self.k = 100

    def stdtest(self):
        self.d = 300


t1 = student()
print(t1.stdtest())
print(t1.__dict__)


# outside the class
class parent:
    def __init__(self):
        self.m = 900

    def g(self):
        self.f = 899


i = parent()  # m will be added to the obj
print(i.g())  # f will be added to the obj
i.h = 100  # h will be added to the obj
print(i.__dict__)
