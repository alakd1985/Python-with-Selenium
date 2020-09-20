# How to access elements in the list

# 1. by using index

l = [10, 20, 30, 40]
print(l[0])
print(l[-1])

# 2. using slicing operator
# list(begin,end,step); +ve==forward direction begin to end-1; -ve==backward direction begin to end+1

l = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(l[2:7])
print(l[2:7:2])
print(l[2::2])
print(l[8:2:-2])
print(l[2:100])  # we will not get any index error
print(l[::1])
print(l[::-1])
