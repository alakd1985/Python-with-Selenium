class outer:
    def __init__(self):
        print('This is outer class')
    class inner:
        def __init__(self):
            print('This is inner class')
        class insideinner:
            def __init__(self):
                print('This is inside inner class')
            @staticmethod
            def m1():
                print('This is a staticmethod inside inner class')

# since the m1 method is the staticmethod, we don't need to create obj of the insideinner class'
p = outer().inner().insideinner.m1()