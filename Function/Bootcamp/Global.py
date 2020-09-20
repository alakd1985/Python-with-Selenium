


a=999
def f2():
    a = 100
    print(a)
    print(globals().get('a'))
    #print(globals()['a'])
f2()
