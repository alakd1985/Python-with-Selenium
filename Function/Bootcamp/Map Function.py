l = [1,2,3,4,5,6]
def squre(n):
    return n*n
l1 = map(squre,l)
print('Map function is ::',tuple(l1))

# using lambda function

t = tuple((map(lambda x:x*x,l)))
print(t)

# using lambda for multiple function

p=[1,2,3,4,5,6]
p1=[10,20,30,40,50,60]

p3= set(map(lambda x,y:x*y,p,p1))
print('Multiple function using map::',p3)

# using lambda for multiple funcion using different lenght of list
v=[1,2,3,4,5,6]
v1=[10,20,30,40,50,60,900,890]

v3= tuple(map(lambda k,i:k*i,v,v1))
print('New map function for different size of list:',v3)
