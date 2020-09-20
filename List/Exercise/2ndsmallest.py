#Write a Python program to find the second smallest number in a list.
def secondsmallest(numbers):
    uniquelist = []
    for x in numbers:
        if x not in uniquelist:
            uniquelist.append(x)
    uniquelist.sort()
    return uniquelist[1]

print(secondsmallest([1,2,-9,-4]))
