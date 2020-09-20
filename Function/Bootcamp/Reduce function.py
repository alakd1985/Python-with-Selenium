# reduce function reduces the element into only one element
from functools import reduce
l = [1,2,3,4,5,6]
result=reduce(lambda x,y:x+y,l)
print(result)

# calculate the sum of first 100 numbers

result=reduce(lambda x,y:x+y,range(1,11))
print(result)
