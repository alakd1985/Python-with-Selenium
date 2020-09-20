# pop method
l = {100: 'alak', 200: 'Toma', 500: 'dutta', 400: 'Tomo'}
print('After remove ::', l.pop(500))
print(l)

d = {100: 'alak', 200: 'Toma', 500: 'dutta', 400: 'Tomo'}
print('After remove new dictionary::', d.pop(300, 'guest'))
print(d)
print('After remove new dictionary::', d.pop(400, 'guest'))
print(d)

# pop item
print('Pop item removal::',d.popitem())
print('After using pop item',d)

# clear removes all the item in the dict
d.clear()
print('after clearing the dictionary',d)