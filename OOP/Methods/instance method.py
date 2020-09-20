# method: instance class and static method
class student:
    def __init__(self, name, marks):
        self.marks = marks
        self.name = name

    def display(self):
        print('Your name is:', self.name)
        print('Your marks are::', self.marks)

    def grade(self):
        if self.marks >= 60:
            print('Your grade is A')
        elif self.marks >= 50:
            print('Your grade is B')
        else:
            print('You are not a good student!!')


n = int(input('Enter the number of students:: '))
for i in range(n):
    name = input('Enter the student name::  ')
    marks = int(input('Enter the student marks:: '))
    obj = student(name, marks)
    obj.display()
    obj.grade()
    print()
