# == and != operator
# Number order and content of elements should be the same

l1 = ('dog', 'cat', 'tiger')
l2 = ('dog', 'cat', 'tiger')
l3 = ('dog', 'cat', 'Tiger')
l4 = ('cat', 'dog', 'tiger')

print(l1 == l2)
print(l1 == l3)
print(l3 == l2)

# Relational operator < <= >= >
t1 = (10, 3, 56)
t3 = (10, 3, 56, 70)
t2 = (32, 56, 78)
print('Comparison between two tuple:: ', t1 > t2)
print('Comparison between two tuple:: ', t1 < t2)
print('Comparison between two tuple:: ', t1 < t3)

# Membership operator
print('10 in t1:: ', 10 in t1)
print('100 in t1:: ', 100 in t1)
print('1 in t1:: ', 1 in t2)
print('10 not in t1:: ', 10 not in t1)
print('100 not in t1:: ', 100 not in t1)
print('1 not in t1:: ', 1 not in t2)

