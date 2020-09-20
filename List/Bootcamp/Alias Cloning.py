# The process of creating duplicate ref variable is called aliasing
l = [10, 20, 30, 40, 10, 20, 60, 50]
u = l
print(l)
print(l is u)
l[1] = 777
print(l)

# creation of duplicate object is called as cloning
x = l[::]
print(id(x))
print(id(l))
print(x is l)

f = l.copy()
print(f)
