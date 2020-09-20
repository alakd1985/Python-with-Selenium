class student:
    def __init__(self,name, roll):
        self.roll = roll
        self.name = name

    def display(self):
        print('The name is :', self.name)
        print('The roll is :',self.roll)
s = student("Alak", 5)
s.display()