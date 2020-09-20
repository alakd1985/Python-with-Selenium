# Write a Python program to sum all the items in a list.
def sumlist(items):
    sum = 0
    for x in items:
        sum += x
    return sum


print('The sum of the elements are ::', sumlist([1, 2, 3]))
