# By has a relationship(Composition)
# By is a relationship(Inheritance)

class Engine:
    def __init__(self):
        self.power = '135k'
    def useEngine(self):
        print('Engine specific functionality')


class car:
    def __init__(self):
        self.engine = Engine()

    def useCar(self):
        print('Car required engine functionality')
        self.engine.useEngine()
        print(self.engine.power)


c = car()  # when we created car obj, automatically engine obj will be created, so using engine obj
# ref we can call useEngine method
c.useCar()
