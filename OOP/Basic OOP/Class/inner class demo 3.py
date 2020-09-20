class human:
    def __init__(self, names):
        print('Human obj created')
        self.names = names
        self.head = self.Head()

    def info(self):
        print('Hello my self is ', self.names)
        self.head.talk()
        self.head.brain.think()

    class Head:
        def __init__(self):
            print('Head obj is created')
            self.br = self.brain()

        def talk(self):
            print('I can talk now')

        class brain:
            def __init__(self):
                print('Brain obj is created')

            def think(self):
                print('thinking....')


h = human('Alak')
h.info()
