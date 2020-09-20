class employee:
    def __init__(self, name, salary):
        self.salary = salary
        self.name = name

    def __mul__(self, other):
        return (self.salary * other.workingdays)


class timesheet:
    def __init__(self, name, workingdays):
        self.workingdays = workingdays
        self.name = name


e = employee('alak', 1000)
t = timesheet('alak', 899)
print('Monthly income is:: ', e * t)
