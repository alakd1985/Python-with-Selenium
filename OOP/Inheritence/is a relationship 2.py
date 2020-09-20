class person:
    def __init__(self, name, id):
        self.id = id
        self.name = name

    def eatInfo(self):
        print('eat vegetable food')


class employee(person):
    def __init__(self, name, id, cellphone, address):
        super().__init__(name, id)  # calling the parent class constructor by super key word
        self.address = address
        self.cellphone = cellphone

    def work(self):
        print('I am working')

    def empInfo(self):
        print('employee name:', self.name)
        print('employee id:', self.id)
        print('employee cellphone:', self.cellphone)
        print('employee address:', self.address)

e = employee('alak', 2, 65789, 'duke st')
e.eatInfo()
e.work()
e.empInfo()


n = int(input('Please enter the number of rows::  '))
for i in range(5):
    print(' ' * (n-i-1)+(str(i+1)+'') * (i+1))
    print(' ' * (n - i - 1) + ((i + 1) + ' ') * (i + 1))
