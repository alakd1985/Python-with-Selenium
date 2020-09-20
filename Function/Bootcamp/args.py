def f1(*n):
    print(n)
f1(10,20)

def f2(**g):
    print(g)

f2(name='alak',id=12)
f2(name='toma',id=90,location='comilla')
# What is the difference between args and kwargs:
# args will create tuple and kwargs will create dictionary

def funciton(*args,**kwargs):
    print(args)
    print(kwargs)

funciton(10,20,a=90,b=900,t=43)# after  positional argument we can take key word arguments
# but after key word arguments we can not take positional arguments
def funciton1(**kwargs,*args):
    print(args)
    print(kwargs)
funciton1(a=89,b=90,12,23)    
