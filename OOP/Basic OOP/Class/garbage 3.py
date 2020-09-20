# example 1
class student:
    def __init__(self):
        print('constructor will be called')

    def __del__(self):
        print('destructor will be called')


t = student()
print('End of application')


