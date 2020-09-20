# index and slice operator we can access tuple
t = (10, 20, 40, 50, 60, 70)
print(t[2])
print(t[-3])

## using slice operator

p = (10, 20, 40, 50, 60, 70)
print('Forward direction::', p[2:6])
print('Backward direction::', p[-1:-5:-1])
print('Skipping value::', p[::2])
