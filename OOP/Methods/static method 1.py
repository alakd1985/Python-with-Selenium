class test:
    def m():
        print('some method')


t = test()


# t.m()

class student:
    def m1(x):
        print('some method')


t = student()
#t.m1()
student.m1(10) # since we are not using any decorator it can be either static method or instance staticmethod
# so when we call by class name then it will be considered as staticmethod but we have to pass arguments
