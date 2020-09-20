# What is difference between Tuple and List
# duplicate/heterogeneous
# Tuple is not Immutable
# Tuple parenthesis is optional

p = (10,20,40)
# p[2] = 90 immutable tuple
print(p)
t = tuple('alak')
print(t)

# with dynamic input
t = eval(input('Enter tuple of values::  '))
print(t)
