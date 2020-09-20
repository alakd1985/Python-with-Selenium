# self is a ref variable which always points to the current object
class job():
    def __init__(self):
        print('The address of object pointed by self is ::', id(self))


s = job()

print('The address of object pointed by id is::', id(s))


class test():
    def __init__(self):
        print('constructor')

    def demo(self, x):
        print(x)


s = test()

print(s.demo(10))
