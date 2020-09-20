class student:
    a = 10
    b = 20
    c = 90
    d = 123
    e = 435

    # inside constructor: by using either self or classname
    def __init__(self):
        print('Accessing static variable by self inside the constructor', self.a)
        print('Accessing static variable by class name inside the constructor', student.a)

    # inside instance method: by using either self or classname
    def m(self):
        print('Accessing static variable by self inside the instance method', self.b)
        print('Accessing static variable by class name inside the instance method', student.b)

    # inside class method: by using either cls variable or classname
    @classmethod
    def m2(cls):
        print('Accessing static variable by cls inside the class method', cls.c)
        print('Accessing static variable by class name inside the class method', student.c)

    # inside static method: by using class name
    @staticmethod
    def m3():
        print('Accessing static variable by class name inside the static method', student.d)


u = student()
u.m()
student.m2()
student.m3()

# From outside of class: by using either object reference or class name
print('Accessing static variable by class name outside the class', student.e)
print('Accessing static variable by obj ref outside the class', u.e)
