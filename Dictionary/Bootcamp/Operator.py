# plus and multiply operator, <, > are not applicable
l = {100: 'alak', 200: 'Toma', 500: 'alaka', 400: 'Tomo'}
l1 = {100: 'alak', 200: 'Toma', 500: 'alaka', 400: 'Tomo'}
#x = l + l1

# Equality operator
print(l==l1)

# Membership operator applicable but only for keys
print(100 in l)
print(1000 in l)
print('alak' in l)