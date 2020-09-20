class employee:
    def __init__(self, name, salary, number):
        self.salary = salary
        self.number = number
        self.name = name

    def display(self):
        print('Employee salary is:', self.salary)
        print('Employee name is:', self.name)
        print('Employee number is:', self.number)


class manager:
    def update(emp):
        emp.salary = emp.salary + 10000
        emp.display()


obj = employee('alak', 899, 2)
manager.update(obj)
