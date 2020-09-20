class student:
    def __init__(self, Name, roll):
        self.roll = roll
        self.Name = Name
    def __str__(self):
        return 'Name is: {}, Roll number is: {},'.format(self.Name,self.roll)

s = student('alak', 12)
s1 = student('toma', 23)
print(s)
print(s1)
