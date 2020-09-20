import time
class student:
    def __init__(self):
        print('constructor will be called')

    def __del__(self):
        print('destructor will be called')


l = [student(), student(), student()]
print('Making list eligible for destruction')
del l # without the del also destructor will be called but it should be end of the application
# after the last print statement
time.sleep(10)
print('end of application')
