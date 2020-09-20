d = eval(input('enter any dictionary:'))
sum1 = 0
for item in d.items():
    sum1 = sum1 + item[1]
print('The sum of values::', sum1)

# Method 2
print('The sum of values::', sum(d.values()))
