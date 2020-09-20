## This is the start of Python list

## When to use list-- A group of objects as a single entity, insertion order must be preserved, and duplicate is allowed,
## heterogenious objects are allowed, list are dynamic, we can change the content; list is mutable;

# Empty list object
l = []
l.append('durga')
l.append(10)
l.append('durga')
print(l)
l[0] = 90
print(l)
print(type(l))

# Dynamic input

l = eval(input('Enter a list:  '))
print(l)


# using the list function

l = list('alak')
print(l)

# in range function

l = list(range(0,20,2)) # will be printing until n-1 value
print(l)

# creating list based on split function

s= 'I love to eat rice'
l= s.split()
print(l)