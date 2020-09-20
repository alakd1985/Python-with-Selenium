from math import *
import  os
x=999
y=888
def add(x,y):
    result = x+y
    return result
print(add(12,23))

def prod(x,y):
    result = x*y
    return result
print(prod(12,12))

print(dir())
"""Hello How are you"""
print(__doc__)
print('file name is :',__file__)
# to get the absolute path
print('The absolute path is ::',os.path.abspath(__file__))
# to get the directory
print('The directory name is ::',os.path.dirname(os.path.abspath(__file__)))
print(__name__)



# calulate the area of the circle
r = eval(input('Please enter a value of radius'))
area1 = pi*r**2
print('The area of the circle is::',area1)
