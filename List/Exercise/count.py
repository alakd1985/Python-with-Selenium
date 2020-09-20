# Write a Python program to count the number of elements in a list within a specified range
def countinrange(lis, min, max):
    ctn = 0
    for x in lis:
        if min <= x <= max:
            ctn += 1
    return ctn


print(countinrange([10, 1, 2, 3, 100], 1, 10))
