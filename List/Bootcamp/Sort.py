# alphabetical and ascending order

l = [10, -10, 9, 0, 45, 67]
print(l)
l.sort()
print('after sorting', l)

u = ['apple','banana', 'ant']
u.sort()
print(u)
# print('Extending the list:: ',l.extend(u))

## Reverse sorting
i = [10, -10, 9, 19, 45, 167]
i.sort(reverse=True)
print(i)

p = ['mango', 'apple','tangerin']
p.sort(reverse=True)
print(p)

# sort is a list specific function and sorted is a python inbuilt function which returns a list
