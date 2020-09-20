class student:
    schoolname = 'Govt lab'

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    # instance method declaration to get the instance variable inside the constructor
    def getstudentinfo(self):
        print('The student name is::', self.name)
        print('The roll number is ::', self.roll)

    # class method should be declared as @classmethod
    @classmethod
    def getschoolinfo(cls):
        print('School name is::', cls.schoolname)

    # static method should be declared as @staticmethod,, here a and b are called local variable
    @staticmethod
    def getsum(a, b):
        return a + b
