# union
s1 = {12,32,34,54,65}
s2 = {112, 132, 134, 154, 165}
s3= {21,54,32,12}

# | is called pipe symbol

s4 = s1.union(s2)
print(s4)

# second method
s5 = s1|s2
print(s5)

# Intersection
s6 = s3 & s1
print(s6)

s7 = s3.intersection(s1)
print(s7)

# difference
s8 = s2-s3
print(s8)
s8 = s2.difference(s3)
print(s8)

# symmetric difference
s9 = s1 ^ s2
print(s9)
