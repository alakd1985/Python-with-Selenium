class test:
    count = 0

    def __init__(self):
        test.count += 1

    @classmethod
    def noofObjects(cls):
        print('The number of objects are :::', cls.count)


print(test.noofObjects())
t = test()
t1 = test()
print(test.noofObjects())
