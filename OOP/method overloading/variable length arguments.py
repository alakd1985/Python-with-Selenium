class student:
    def m(self, a=None, b=None, c=None):
        if a is not None and b is not None and c is not None:
            print('there are three arguments')
        elif a is not None and c is not None:
            print('there are two arguments')
        elif a is not None:
            print('there is one argument')


s = student()
s.m()
s.m(10)
s.m(10, 20)


# in order to have any number of arguments we should use variable length arguments

class test:
    def m1(self, *args):
        print('there are variable length arguments')


t = test()
t.m1(34, 56)
t.m1(43, 677, 899)


# example

class add:
    def addition(self, *args):
        total = 0
        for x in args:
            total += x
        print('the sum is:', total)


a = add()
a.addition(12, 23, 45)
a.addition(54, -900, 433)
