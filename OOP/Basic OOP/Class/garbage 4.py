# example 2
class test:
    def __init__(self):
        print('This is a constructor')

    def __del__(self):
        print('This is a destructor')


p = test()
p = None
print('End of application')
