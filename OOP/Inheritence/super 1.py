class parent:
    a = 90

    def __init__(self):
        print('parent constructor')

    def m1(self):
        print('this is a parent method')

    @classmethod
    def m2(cls):
        print('this is a parent class method')

    @staticmethod
    def m3():
        print('this is a parent static method')


class child(parent):
    def __init__(self):
        print('this is a child class constructor')

    def method1(self):
        # we can also use self. instead of super as there is no naming conflict between the parent class methods and
        # child class methods
        print(super().a)
        super().m3()
        super().m2()
        super().m1()
        super().__init__()
        print('.......................using self..............')
        self.m1()
        self.m2()
        self.m3()
        


c = child()
c.method1()
