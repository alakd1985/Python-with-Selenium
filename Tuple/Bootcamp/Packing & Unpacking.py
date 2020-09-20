# tuple packing

a = 10
b = 12
c = 90
t = a, b, c
print('Tuple packing ::', t)
l = [a, b, c]
print('List packing :: ', l)

# Tuple unpacking
u = (10, 12, 90)
a, b, c = u
print('Tuple unpacking:;', a, b, c) # The number of values and the number of variables must be same during unpacking
