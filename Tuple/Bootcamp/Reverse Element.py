# Reverse function is not available in Tuple since this is immutable
t = (10, 3, 56, 70)
r = reversed(t)
t = tuple(r)
print(t)

# Sorting of elements
sr = sorted(t)
ty = tuple(sr)
print(ty)
s = sorted(t, reverse=True)
print(s)

f = (1, 2, 34, 5, 65, 0, -1)
v = sorted(f, reverse=True)
print(v)

# max and min function
print('Max value in f ::', max(f))
print('Min value in f ::', min(f))

# Append insert extend pop clear are not available in Tuple
