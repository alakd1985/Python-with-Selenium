# read line by line one by one
f = open('abc.txt', 'r')
line1 = f.readline()
print(line1, end= '')
line2 = f.readline()
print(line2)

# using while loop
f1 = open('abc.txt', 'r')
line = f1.readline()
while line != '':
    print(line, end= '')
    line = f1.readline()
f1.close()

# printing in the List

o = open('abc.txt','r')
ln = o.readlines()
for line in ln:
    print(line, end='')
o.close()


