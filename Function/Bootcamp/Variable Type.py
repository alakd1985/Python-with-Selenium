# global and local variable
# can you please explain global keyword

def f1():
    global a # global key word can not be declared and assigned at the same time.
    a=90
    print(a)

def f2():
    print(a) # local varibale is the high priority

print('The value of a',f1())
print('The value of a',f2())
