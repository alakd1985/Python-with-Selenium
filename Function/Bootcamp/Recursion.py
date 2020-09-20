# lenght of code will be reduced and solve complex problems
# factorial

def factorial(n):
    result = 1
    while n>=1:
        result *= n
        n = n-1
    return result
print(factorial(5))


# recursive way
def factorialr(n):
    print('Executing factorial value of n is::',n)
    if n==0:
        res = 1
    else:
        res= n*factorialr(n-1)
    print('Returning factorial value of {} is: {}'.format(n,res))
    return res

print(factorialr(3))

#for x in range(11):
#    print('The factorial of {} is:{}'.format(x,factorialr(x)))
count = 0
def fact(n):
    global count
    count += 1
    print('Executing factorial value of n is::',n)
    if n==0:
        res = 1
    else:
        res= n*fact(n-1)
    print('Returning factorial value of {} is: {}'.format(n,res))
    return res

print(fact(10))
print(count)
