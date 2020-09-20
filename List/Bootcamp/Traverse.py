l = [10, 20, 30, 40, 5, 60, 7, 80, 9, 100]
# using while loop

i = 0
while i < len(l):
    print(l[i])
    i = i + 1

# by using for loop

for x in l:
    print(x)

# printing only even value

for x in l:
    if x % 2 == 0:
        print(x)

# printing index wise
# -ve = +ve - len(l)

i = 0
while i < len(l):
    print('The element present at the positive index is {}, nexgative index {} is {}'.format(i, i - len(l), l[i]))
    i = i + 1
