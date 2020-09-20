# Write a Python program to get the largest number from a list.
def max_number(list):
    max = list[0]
    for x in list:
        if x > max:
            max = x
    return max


print('Max number is:: ', max_number([1, 2, -90, 98, 456]))

# Write a Python program to get the smallest number from a list.
