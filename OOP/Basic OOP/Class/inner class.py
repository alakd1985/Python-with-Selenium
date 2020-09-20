# When we are going for inner class
# Without existing one type of obj if there is no chance of existing another type of objects
# then we should go for inner class
# it improves the modularity and security of the application.

class university:
    class department:
        pass


class car:
    class engine:
        pass


class head:
    class brain:
        pass


class outer:
    def __init__(self):
        print('Outer class obj is created')

    class inner:
        def __init__(self):
            print('Inner class obj is created')

        def m(self):
            print('Inner class method is created')


inner_obj = outer().inner().m()

