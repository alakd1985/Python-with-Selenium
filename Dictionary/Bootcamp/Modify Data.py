class parent:
    pass


# In the dictionary key and value can be any type

l = {100: 'alak', 200: 'Toma', 500: 'alaka', 400: 'Tomo'}
print('Value is ::', l[100])
key = eval(input('Enter the key to find the value:'))
if key in l:
    print('The value corresponding to the key is ::', l[key])
else:
    print('The key is not valid')

# Update and modify

l[500] = 'rakesh'
print('Newly formed dictionary', l)
l[100] = 'Om'
print('After the modification the newly dictionary is ::', l)

# delete the data
del l[400]
print('after the delete the key', l)
del l[100], l[200]
print('After the multiple deletion::', l)

# problem
n = eval(input('Enter the number of students'))
d = {}
for i in range(n):
    name = input('Enter the student name::')
    marks = int(input('Enter the student marks::'))
    d[name] = [marks]
# print('Newly formed dictionary is ::', d)
print('*' * 20)
print('Name', '\t\t', 'Marks')
print('*' * 20)
for name in d:
    print(name, '\t\t', d[name])
