s=lambda n:n*n
print('Square of {} is:{}'.format(5,s(5)))
for x in range(1,11):
    print('Square of {} value is: {}'.format(x,s(x)))

# sum of two numbers
s = lambda a,b: a+b
print('The sum of two numbers are::',s(10,20))

# find the largest numbers
bigger = lambda a,b: a if a>b else b
print('The bigger of the two numbers::',bigger(10,20))
bigger1 = lambda a,b,c: a if a>b and a>c else b if b>c else c
print('The biggest of the three numbers::',bigger1(12,65,32))
