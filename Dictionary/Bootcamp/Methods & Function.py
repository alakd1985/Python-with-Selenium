l = {100: 'alak', 200: 'Toma', 500: 'dutta', 400: 'Tomo'}
l1 = {10: 'dutta', 20: 'rani', 50: 'dey', 40: 'krish'}
print(len(l))
print(l.get(200))
print(l.get(500, 'usa'))
print(l.update(l1))
print(l)
print(l.keys())
for key in l.keys():
    print(key)

for value in l.values():
    print(value)

# for each pair of key and value are called item

for item in l:
    print('without using l.items()',item)

# to get key and value at the same time

for k,v in l.items():
    print(k,'......',v)
