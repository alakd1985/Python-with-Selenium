def arguments(a,b,c=10,d=20):
    print(a,b,c,d)

print(arguments(10,20))
print(arguments(10,20,90,100))
print(arguments(10,20,d=100))
print(arguments()) # will be type error
print(arguments(c=90,a=89,a,b)) # after positional arguments we can not take keyword arguments
print(arguments(10,20,b=900)) # multiple values can not be provided for the same arguments
