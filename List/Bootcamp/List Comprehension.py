# Regular way of creating list
l = []
for x in range(1, 21):
    l.append(x)
print(l)

# List comprehension way of creating list

u = [x for x in range(1, 21)]  # here the first x is called the expression
print(u)

# creation of list with square values from 1 to 10
p = [x * x for x in range(1, 11)]
print(p)

# list creation with the power of 2

k = [2 ** x for x in range(1, 11)]
print(k)

# list 1-100 where values are divided by 10

m = [x for x in range(1, 101) if x % 10 == 0]
print(m)

# element present in one list but not in other

m = [1, 2, 3, 4, 5, 6, 7, 8]
n = [5, 6, 7, 8, 9, 10, 11]
c = [x for x in m if x not in n]
print(c)

# print common elements in two lists

g = [10, 11, 12, 13, 14]
d = [12, 13, 14, 15, 16, 17]
z = [x for x in g if x in d]
print(z)

# Create a list with first letter of each word

i = ['alak', 'toma', 'lucky', 'krish']
b = [word[3].upper() for word in i]
print(b)

# split every word with corresponding letter count
s = 'Quick brown fox jumps over the lazy dog'
word = s.split()
print(word)
v = [[i.upper(), len(i)] for i in word]
print(v)

# search for vowels

vow = ['a', 'e', 'i', 'o', 'u']
result = []
s = input('Enter a string:: ')
for ch in s:
    if ch in vow:
        if ch not in result:
            result.append(ch)
print(result)


# another way

for ch in vow:
    if ch in s:
        result.append(ch)
print(result)
