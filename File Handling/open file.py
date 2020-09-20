f = open('abc.txt', 'w')
f.write('alak')
# instead of list we can also use the tuple or set
# when we use set order will not be preserved; rarely the dictionary are used; only keys will be added
# keys should be string type only
l = ['alak\n', 'dutta\n', 'toma\n', 'rani\n', 'dey\n']
f.writelines(l)
