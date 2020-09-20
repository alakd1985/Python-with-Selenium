class student:
    """ This class is developed for demo purpose"""
    # method
    # variables


print(student.__doc__)


# 3 types of variables==instance,static and local variables
# instance leve variabels are known as obj level variabels
# static are class level variables, local vairables are method level variables
# there are three types of mehtods --- static, class and instance methods

# creating object

# ref var = classname()


class teacher():
    """ This teacher class is developed for demo purpose"""

    def __init__(self):
        self.name = 'Alak'
        self.roll = 12
        self.address = 'Duke St'

    def talk(self):
        print('Hello I am ::', self.name)
        print('My roll number is::', self.roll)
        print('My address is ::', self.address)


refvariable = teacher()
print(refvariable.name)
print(refvariable.talk())


# self is used to declare instance variable and also access the instance variables
# self is ref variable pointing to the current object
# first argument should be self, python will automatically provide value for it


class parent():
    def __init__(self, name, address, role, phone):
        self.name = name
        self.address = address
        self.role = role
        self.phone = phone

    def chat(self):
        print('Hello my name is:', self.name)
        print('Hello my address is:', self.address)
        print('Hello my role is:', self.role)
        print('Hello my phone is:', self.phone)


refvariable1 = parent('toma', 'alexandria', 12, 87654)
revar = parent('rakesh', 'duke', 34, 87654)
print(revar.chat())
print(refvariable1.chat())
