class parent:
    def m1(self):
        print('parent method')


class child(parent):
    def m2(self):
        self.m1()  # to invoke the parent method; if the parent class method and the child class method have the same
        # name,
        # then there will be name conflict and we'll use super to call the parent class method
        print('child method')


c = child()
c.m2()


# example 2
class p:
    def p1(self):
        print('this is a parent method')


class ch(p):
    def p1(self):
        super().p1()
        print('this is a child method')


chobj = ch()
chobj.p1()
