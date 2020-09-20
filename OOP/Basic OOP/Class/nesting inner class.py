class outer:
    def __init__(self):
        print('This is outer class')

    class inner:
        def __init__(self):
            print('This is inner class')

        class insideinner:
            def __init__(self):
                print('This is inside inner class')

            def m1(self):
                print('This is a instance method inside inner class')


p = outer().inner().insideinner().m1()
