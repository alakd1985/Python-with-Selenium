# only first occurrence will be removed

l = [10, 20, 30, 30, 40, 10, 20, 60, 30, 50]

print('removal of 30', l.remove(30))
print('currently l is: ', l)
# l.remove(100) value error

x = eval(input("Please enter a number to remove:  "))
print('Before removal:', l)
if x in l:
    l.remove(x)
    print('After removal of the element::', l)
else:
    print(x, 'not present in the list')

# another example

u = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3]
print('Before removal::', u)
x= eval(input('enter a element to remove'))
while True:
    if x in u:
        u.remove(x)
    else:
        break
print('After removal', u)
