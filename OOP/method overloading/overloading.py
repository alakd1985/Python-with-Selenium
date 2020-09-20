# in python method overloading concepts are not supported. if we declare more than one methods,
# with same name, then the last method will be called

class test:
    def m(self):
        print('there is no argument')

    def m(self, x):
        print('there is one argument')

    def m(self, x, y):
        print('there is two arguments')


c = test()
c.m(45, 6)
