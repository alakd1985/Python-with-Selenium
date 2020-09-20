# How to Call Method of a Particular Super Class:
class a:
    def m1(self):
        print('a class method')


class b(a):
    def m1(self):
        print('b class method')


class c(b):
    def m1(self):
        print('c class method')


class d(c):
    def m1(self):
        b.m1(self)
        print('d class method')

dobj = d()
dobj.m1()