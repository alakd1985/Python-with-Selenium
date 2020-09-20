# variable length argument, internally variable length argument becomes tuple


def f1(*n):
    print('variable length argument function')

print(f1())
print(f1(10,20,30))
print(f1((12,34),(32,56)))
# sum of numbers
def addition(*n):
    total = 0
    for x in n:
        total = total+ x
    print('The sum is :: ', total)

addition(10)
addition(20,10)
addition(34,67,89,90,32,45,67)


def f2(*n):
    print(n)

f2(10,20,30)
f2((12,34,56),(21,45,56))

# using normal and variable length argument at the same time

def f3(x,*y):
    print(x)
    print(y)

def x(*u,g):
    print(u)
    print(g)

#print(x(12,34,54))
print(x(12,34,54,g=90))

# Both variable length argument
# we can not take more than one variable length arguments
#def b(*x,*f): not possible
