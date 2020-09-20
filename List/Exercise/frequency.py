# Python: Get the frequency of the elements in a list
import collections

mylist = [10, 20, 30, 2, 1, 30]
print('Original list', mylist)
ctr = collections.Counter(mylist)
print('counting values are :', ctr)
