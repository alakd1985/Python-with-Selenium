class dad:
    def m1(self):
        print('parent class one ')


class mom:
    def m2(self):
        print('parent class two')


class child(dad, mom):
    def m3(self):
        print('child class')


c = child()
c.m3()
c.m2()
