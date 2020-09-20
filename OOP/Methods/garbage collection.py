import gc
import time

print(gc.isenabled())
gc.disable()
print(gc.isenabled())
gc.enable()
print(gc.isenabled())


class test:
    def __init__(self):
        print('This is test class')

    def __del__(self):
        print('This is test class destructor')


t = test()
#t1= test()
t = None
# time.sleep(10)
print('end of application')
