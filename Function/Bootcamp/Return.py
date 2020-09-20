def sum(a, b):
    add = a * b
    return add


# sum(10,20)
result = sum(10, 20)
print(result)


def f1():
    print('none')


# default value for return in python is none
x = f1()
print(x)


def factorial(num):
    res = 1
    while num >= 1:
        res = res * num
        num = num - 1
    return res


print('The factorial of 4 is :: ', factorial(4))

for i in range(1, 12):
   # print('Factorial of the number', i, 'is', factorial(i))
    print('Factorial of the number {} is : {}'.format(i, factorial(i)))
