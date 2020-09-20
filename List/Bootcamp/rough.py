class uppercase:
    def __init__(self):
        pass

    def getstring(self):
        self.s = input()

    def printstring(self):
        print(self.s.upper())


u = uppercase()
u.getstring()
u.printstring()
