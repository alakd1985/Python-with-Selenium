# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.

def number():
    color = ['red', 'blue', 'green', 'black', 'white']
    newcolor = [x for (i, x) in enumerate(color) if i not in (1, 3)]
    return newcolor


print('After removing specific color:', number())
