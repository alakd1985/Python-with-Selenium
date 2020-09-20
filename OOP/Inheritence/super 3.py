class person:
    def __init__(self, name, age, height, weight):
        self.weight = weight
        self.height = height
        self.age = age
        self.name = name

    def display(self):
        print('name is :', self.name)
        print('age is ', self.age)
        print('Height is ', self.height)
        print('Weight is ', self.weight)


class student(person):
    def __init__(self, name, age, height, marks, weight, rollno):
        super().__init__(name, age, height,weight)
        # since name,height,weight and age are already there in the person class
        # constructor therefore we are calling that constructor by using super().
        self.rollno = rollno
        self.marks = marks

    def display(self):
        super().display()
        print('marks is ', self.marks)
        print('rollno is ', self.rollno)


s = student('alak', 5, 56, 32, 11, 12)
s.display()
