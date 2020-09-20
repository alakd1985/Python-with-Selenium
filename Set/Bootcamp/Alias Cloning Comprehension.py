# Aias and cloning

s = {1, 2, 3, 4, 5, 6}
t = s.copy()
s1 = s
print(t)
print(s)
print(s1)
s1.pop()
print(s)

# In tuple comprehension concept is not applicable
# set comprehension

y = {x * x for x in range(1, 6)}
print(y)

u = {2 ** x for x in range(1, 10)}
print(u)

# how to remove dulicates from list
o = [1, 2, 3, 3, 3, 4, 5, 6, 7]
print(o)
h = set(o)
print(h)
k = list(h)
print(k)

# approach 2
v = [1, 2, 3, 3, 3, 4, 5, 6, 7]
g = []
for x in v:
    if x not in g:
        g.append(x)
print('The new list is :: ', g)

# unique vowels
word = input('Enter any word to search for vowels::')
s = set(word)
vow = {'a', 'e', 'i', 'o', 'u'}

result = s.intersection(vow)  # it will give you the unique vowels
print('The unique vowels present in {} are : {}'.format(word, result))
print('The unique vowels present in {} are : {}'.format(word, sorted(result)))
