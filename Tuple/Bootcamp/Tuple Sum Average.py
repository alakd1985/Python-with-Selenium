# First Method
t = eval(input('Enter tuple of numbers::'))
sum1 = 0

for x in t:
    sum1 += x
print('The sum of the numbers are::', sum1)
print('The average is ::', sum1 / len(t))

# second method
u = eval(input('Enter tuple of numbers::'))
print('The sum of u are::', sum(u))
print('The average of u are::', sum(u) / len(u))
