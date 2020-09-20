# Write a Python program to count the number of strings where the string length is
# 2 or more and the first and last character are same from a given list of strings.

def match(word):
    total = 0
    for x in word:
        if len(x) > 1 and x[0] == x[-1]:
            total += 1
    return total


print('The total number of match word is::', match(['abc', 'bgh', 'aba', 'mamam']))
