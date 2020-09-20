# Inside method implementation if we are using only class variables (static variables), then such type
# of methods we should declare as class method.
# We can declare class method explicitly by using @classmethod decorator.
# For class method we should provide cls variable at the time of declaration

class bird:
    wings = 2

    @classmethod
    def fly(cls, name):
        print('{} flying with {} wings::'.format(name, cls.wings))



bird.fly('Parrot')
bird.fly('Egol')
