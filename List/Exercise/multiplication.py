# Write a Python program to multiplies all the items in a list.

def multiplies(items):
    result = 1
    for x in items:
        result *= x
    return result


print('Multiplication of the items are ::', multiplies([1, 2, 3, 89]))
