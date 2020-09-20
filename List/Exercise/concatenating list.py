# Write a Python program to create a list by concatenating a given list which range goes from 1 to n.

list = ['a', 'b']
n = 3
newlist = ['{}{}'.format(x, y) for y in range(1, n + 1) for x in list]
print(newlist)
