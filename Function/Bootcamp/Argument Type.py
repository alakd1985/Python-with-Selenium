# 4 types of arguments --positional, keyword,default,variable length arguments
def subtraction(a, b):
    print(a - b)


print(subtraction(200, 100))

# keyword arguments
print(subtraction(a=200, b=400))
# We can use positional and key word arguments simultaneously. First we have to take
# positional and then we have to take key word arguments
# subtraction(a=200)
subtraction(200, b=233)


# default arguments

def wish(name='Guest'):
    print('Hello', name, 'Good morning')


print(wish())
print(wish("alak"))
print(wish('toma'))

#def wish(name,msg):
#    pass
#def wish(name='none',msg='good morning'):
#    pass
# positional arguments should be declated First
def wish(name,msg='I am good'):
    print('Hello',name,msg)
wish('toma')
wish('alak')
