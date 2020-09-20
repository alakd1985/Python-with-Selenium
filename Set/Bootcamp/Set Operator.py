s1 = {10, 20, 49}
s2 = {32, 56, 87}
print(s1 == s2)

# In terms of equality, we should have same value in the two sets, but order is not important
r = {23, 45, 65}
r1 = {65, 23, 45}
print(r == r1)

# relational operator in set is not meaningful

r2 = {23, 45, 65}
r3 = {65, 23, 45, 54, 87}
print('Relational operator::', r2 > r3)
print('Relational operator::', r2 < r3)

# Membership operator --- not in or in

print('23 is present in r2::', 23 in r2)
print('23 is present in r2::', 100 in r2)
print('23 is present in r2::', 1004 not in r2)