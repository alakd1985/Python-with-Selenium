# Write a Python program to print the numbers of a specified list after removing even numbers from it.

def rmeven():
    num = [7, 8, 120, 25, 44, 20, 27]
    odd = [x for x in num if x % 2 != 0]
    return odd


print('The value is', rmeven())
