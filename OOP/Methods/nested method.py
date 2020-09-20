class test:
    def m(self):
        def calc(a, b):
            print('The sum is ::', a + b)
            print('The difference is :: ', a - b)
            print('The product is ::', a * b)
            print('The division is :: ', a / b)

        calc(10, 20)

t = test()
t.m()
