n = int(input('Enter the number of students::  '))
d = {}
for i in range(n):
    name = input('Enter the student name:  ')
    marks = int(input('Enter the student marks:  '))
    d[name] = marks
# print('Student data insertion completed')
print('Name', '\t\t', 'Marks')
# print('*' * 30)
for k, v in d.items():
    print(k, '\t\t', v)

print('Search operation started:: ')

while True:
    name = input('Enter the student name:: ')
    marks = d.get(name, -1)  # name to the corresponding marks will be available but if not then it will
    # return false
    if marks == -1:
        print('Student not found')
    else:
        print('Marks of ', name, 'is', marks)
        option = input('do you want to continue with another student:: Please say Yes or No::  ')
        if option.lower() == 'no':
            break


print('Thanks for using the application')