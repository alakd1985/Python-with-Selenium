# creation of set

# empty set
s = set()

# if we have set already
s = {10, 20, 40}
print(s)

# By using set function
l = [10, 34, 56]
s1 = set(l)
print(s1)

# By using range function

t = set(range(0, 101, 10))
print('Creation of t is::', t)

g = set('apple')
print('Set of apple::', g)

# From user input

p = eval(input('Enter a set of values::'))
print('From user input the set function is ::', set(p))
