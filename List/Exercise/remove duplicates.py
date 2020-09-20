# Write a Python program to remove duplicates from a list.

def duplicate(items):
    p = []
    for x in items:
        if x not in p:
            p.append(x)
    return p


print('Unique items are::', duplicate([1, 1, 2, 2]))
