f = open('abc.txt', 'r')
data = f.read()
print(data)
f.close()

# to read n number of characters

f1 = open('abc.txt', 'r')
data1 = f1.read(10)
print(data1)
f.close()