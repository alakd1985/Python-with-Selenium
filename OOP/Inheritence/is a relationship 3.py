class parent:
    def m(self):
        print('This is a parent class')
class child(parent):
    def m1(self):
        print('This is a child class')
c = child()
c.m()
c.m1()

