# it removes the last element of the list

l = [10, 20, 30, 40, 10, 20, 60, 50]
print(l.pop())
print(l)

# pop method can not be used in the empty list
print(l.pop(2))
print(l)

# clear method to remove all the elements in the list
print(l.clear())
print(l)
