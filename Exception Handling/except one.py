try:
    x = int(input('enter a number'))
    y = int(input('enter the second number'))
    print(x/y)
except ZeroDivisionError:
    print('this is a ZeroDivisionError')
except TypeError:
    print('this is a TypeError')
    
