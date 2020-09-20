# nested list

l = [10, 20, 30, [40, 50]]
print(l[1])
print(l[3])
print(l[3][1])

u = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
print(u)
print('Print row wise::  ')
for x in u:
    print(x)

print('Matrix style:: ')

for x in u:
    for y in x:
        print(y, end=' ')
    print()
