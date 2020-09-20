class parent:
    a = 10

    def __init__(self):
        self.n = 90
        print('Parent class constructor')

    def parentinfo(self):
        print('Parent instance method')

    @classmethod
    def parclass(cls):
        print('parent class method')

    @staticmethod
    def parstat():
        print('parent class staticmethod')


class child(parent):
    pass
c = child()
c.parstat()
c.parclass()
c.parentinfo()
print(c.n)
print(c.a)
