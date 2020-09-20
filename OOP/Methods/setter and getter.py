# getter method also known as access method
# setter method also known as mutator method
class student:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setMarks(self, marks):
        self.marks = marks

    def getMarks(self):
        return self.marks


n = int(input('Enter the number of students::  '))
studentlist = []
for i in range(n):
    s = student()
    name = input('Enter the student name:: ')
    marks = input('Enter the marks:: ')
    s.setName(name)
    s.setMarks(marks)
    studentlist.append(s)
for j in studentlist:
    print('Hello', s.getName())
    print('Your marks is:: ', s.getMarks())
    print()
