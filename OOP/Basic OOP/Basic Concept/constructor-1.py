# it is a special method
# to declare and initialize instance variable constructor is used
# inside the class, constructor is not mandatory as python will provide default constructor
# we can call constructor explicitly but it will work as method
class student:
    def f(self):
        print('hi')


t = student()
t.f()


class parent:
    def __init__(self):
        print('hello')


i = parent()
i.__init__()


# method or constructor overloading is not allowed in python
class test:
    def __init__(self):
        print('hello')

    def __int__(self, x):
        print('hey')


# y = test()
y = test(10)
