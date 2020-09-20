class parent:
    a = 10  # static variable

    def __init__(self):  # constructor
        self.b = 20  #

    def m(self):
        self.a = 888  # instance variable inside the instance method
        self.b = 999


t1 = parent()  # obj created of t1, so the constructor will be called
t2 = parent()  # obj created of t2, so the constructor will be called
t1.m()  # calling the instance method
t2.m()  # calling the instance method

print('t1', t1.a, t1.b)  # since a new reference variable is created,therefore a=888 will be executed by replacing a=10
print('t2', t2.a, t2.b)  # since a new reference variable is created,therefore a=888 will be executed by replacing a=10


# but since there is no change in the obj t2, previous instance variable b=20 will be executed


class test:
    a = 10  # static variable

    def __init__(self):  # constructor
        self.b = 20  #

    @classmethod
    def m(cls):
        cls.a = 888  # instance variable inside the inside instance method
        cls.b = 999


u1 = test()  # obj created of u1, so the constructor will be called
u2 = test()  # obj created of u2, so the constructor will be called
u1.m()  # calling the instance method
u2.m()  # calling the instance method

print('u1', u1.a, u1.b)  # since a new reference variable is created,therefore a=888 will be executed by replacing a=10
print('u2', u2.a, u2.b)  # since a new reference variable is created,therefore a=888 will be executed by replacing a=10
# but since there is no change in the obj u2 previous instance variable b=20 will be executed
print('test', test.a, test.b)
