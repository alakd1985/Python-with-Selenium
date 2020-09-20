def sum_sub(a, b):
    sum = a + b
    sub = a - b
    return sum, sub


x, y = sum_sub(12, 10)
print('The sum is ::', x)
print('The subtraction is : ', y)


def calc(a, b):
    sum = a + b
    sub = a - b
    mul = a * b
    div = a / b
    return sum, sub, mul, div


t = calc(20, 10)
print(t)

for x in t:
    print(x)
