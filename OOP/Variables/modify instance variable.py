# access the instance variable

class test:
    def __init__(self):
        self.a = 10
        self.b = 90

    def info(self):
        print('The value is:', self.a)
        print('The value is:', self.b)


t = test()
# access the instance variable outside of the class
print(t.a)
print(t.b)
# access the instance variable through the instance method
print(t.info())


# delete the instance variable


class parent:
    def __init__(self):
        self.c = 10
        self.d = 90
        self.e = 900
        self.f = 190

    # delete instance variable inside the class
    def m(self):
        del self.c


u = parent()
u.m()
print('After the deletion of c', u.__dict__)

# delete instance variable outside the class

u1 = parent()
del u1.d, u1.e
print('After the deletion of d and e outside the class', u1.__dict__)


# How to update of instance variable

class student:
    def __init__(self):
        self.a = 10
        self.b = 90


p = student()
# instance variable update
p.a = 900
p.b = 800
print('After the modification of a and b', p.__dict__)
