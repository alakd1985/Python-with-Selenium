## in order to be equal the number of elements must be same, the order of elements must be same,
## and the content must be same including the case


l1 = ['dog', 'cat', 'tiger']
l2 = ['dog', 'cat', 'tiger']
l3 = ['dog', 'cat', 'Tiger']
l4 = ['cat', 'dog', 'tiger']
print(l1 == l2)
print(l2 == l3)
print(l3 == l4)

print(l1 != l2)
print(l2 != l3)
print(l3 != l4)

## Relational operator

t1 = [10, 20, 30]
t2 = [5, 20]
t3 = [5, 20]
t4 = [5, 20, 30]
print(t2 < t1)
print(t2 > t1)
print(t2 <= t1)
print(t2 >= t1)
print(t3 >= t2)
print(t4 >= t3)

## Membership Operator
print('Memberhsip in', 10 in l1)
print('Memberhsip non in', 40 not in l1)
print('Memberhsip in', 5 in l3)

s1 = ['alak', 'toma']
s2 = ['tom', 'harry']
print(s2 > s1)
