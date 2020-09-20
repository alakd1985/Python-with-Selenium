# First approach

d = {}

# if you know already data
f = {'A': 300, 200: 'Alak', 100: 'toma'}

# import set or tuple or list:: by using dict function
l = [(100, 'A'), (200, 'B')]  # list of tuples
g = dict(l)
print('Newly created dictionary', g)

# list of tuples, tuples of tuples,set of tuples,lists of list,tuples of list but
# set of list are not acceptable since the list is no hashable object

a = [[100, 'A'], [200, 'B']]
b = dict(a)
print('List of list object dictionary:', b)

# By using dynamic input
f= eval(input('Enter dictionary'))
h= dict(f)
print('Newly created dictionary::',h)

