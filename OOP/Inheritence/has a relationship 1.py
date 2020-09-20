class Car:
    def __init__(self, name, model, color):
        self.color = color
        self.model = model
        self.name = name

    def getInfo(self):
        print('The car is {},{} and {}'.format(self.name, self.color, self.model))


class employee:
    def __init__(self, ename, eid, car):
        self.car = car
        self.eid = eid
        self.ename = ename

    def empInfo(self):
        print('The information about the employee is {},{}'.
              format(self.ename, self.eid))
        # here we are calling getinfo method inside the instance method
        # of class employee
        self.car.getInfo()


car = Car('toyota', 'corolla', 'black')
emp = employee('alak', 13,car)
e.empInfo()