# Count method
l = [10, 20, 30, 40, 10, 20, 60, 50]
print('Length is :', len(l))
print('Number of 30 in the list is :', l.count(40))
print('Number of 30 in the list is :', l.count(140))
print('Number of 30 in the list is :', l.count(0))
print('Number of 30 in the list is :', l.count(20))

# Index method:: It returns the first time occurrence of indexed element

print('Index of 20 is :', l.index(20))
print('Index of 30 is :', l.index(50))
# print('Index of 30 is :', l.index(500)) # will through error since it is not part of the list

x = eval(input("Please enter a number in the l list to find:: "))

if x in l:
    print('{} is present in index {}'.format(x, l.index(x)))
else:
    print(x, "is not present in the list")

## Append method

l = []
l.append(10)
l.append(60)
l.append(30)
print("The new list value is:: ", l)
l.append(60)
print("The new list value is:: ", l)

# problem: Add numbers in the list which are divisible by 10
l = []
for x in range(1, 101):
    if x % 10 == 0:
        l.append(x)
print('The new list which is divisible by 10 is: ', l)

## insert method

l = [10, 20, 30]
l.insert(1, 777)
print('New inserted value is:: ', l)

#
l.insert(-100, 9000)
print('Newly inserted value is:  ', l)  # since the negative index is out of range, therefore the 9000 will
# be added in the 0th index
l.insert(900, 8765)
print('Newly inserted value is:  ', l)  # since the positive index is out of range, therefore the 8765 will
# be added in the last index

## Extend method

order = ['rice', 'lentil', 'drink']
order1 = ['water', 'veg']
order1.extend(order)
print('The newly added order is :; ', order1)

t = [10, 20, 30]
t1 = [40, 50, 60]
t2 = ['abcd']
t.append(t1)
print('The newly list of t is :: ', t)
t.append(t2)
print('After appending t is::', t)
t.extend(t2)
print('After extending of t2 is ::', t)

x = [10, 20, 30]
x1 = ['abcd']
x.extend('abcd')
print('The newly x list is :: ', x)
