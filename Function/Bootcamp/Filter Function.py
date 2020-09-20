# print out the even numbers without filter function

l = [1,2,3,4,5,6]
def withoutfilter(n):
    if n % 2 ==0:
        return True
    else:
        return False

l1=[]
for x in l:
    if withoutfilter(x)==True:
        l1.append(x)
print('Even numbers are :',l1)


# with filter function
l2 = [1,2,3,4,5,6,8,9,10]
def wfilter(n):
    if n % 2 ==0:
        return True
    else:
        return False

l4= filter(wfilter,l2)  # filter function returns filter obj not list
print('Using filter function even numbers are:',list(l4))

# filter with lambda
fLamda = list(filter(lambda x:x%2==0,l2))
fLamda1 = set(filter(lambda x:x%2!=0,l2))
fLamda2 = set(filter(lambda x:x%2!=0 and x%3==0,l2))
#print(fLamda1)
print('Filter even numbers with lambda function::',fLamda)
print('Filter odd numbers with lambda function::',fLamda1)
print('Filter odd numbers and divisible by 3 with lambda function::',fLamda2)


# another example

names=['alak','toma','audrija','anirban','rakesh','lucky','om','krish']
nlamda=set(filter(lambda name:name[0]=='k',names))
print('Name starts with K::',nlamda)
# name length divisible by 5

dlambda=tuple(filter(lambda name:len(name)%5==0,names))
print('Name length divisible by 5 is ::',dlambda)
