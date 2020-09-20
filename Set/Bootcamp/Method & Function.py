# Update the set

s = {1, 2, 3, 4}
l = [67, 43, 32]
s.update(l)
print(s)
s.update(range(1, 10), 'alak')  # since alak contains two a so only one of them will be added
print(s)

# valid or invalid
p = {12, 43, 21, 45, 65, 76}
# p.add (32,54)
# p.update(10)
#p.update(12,43,54)
#p.update(range(1,23,5),'toma')
print(p)

# Remove discard pop clear

j = {12, 43, 21, 45, 65, 76}
j.remove(21)
print(j)

# discard
j.discard(100)
print(j)

# pop method:: it will remove element randomly
j.pop()
print('after popping ::',j)

# clear method
j.clear()
print('after clearing j::',j)

