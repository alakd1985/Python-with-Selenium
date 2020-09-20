class employee:
    def __init__(self, ename, esalary, eno, eaddress):
        self.eaddress = eaddress
        self.eno = eno
        self.esalary = esalary
        self.ename = ename

    def display(self):
        print('Employee Name:{},Employee Salary:{},Employee Number:{},Employee addresses:{}'
              .format(self.ename, self.esalary, self.eno, self.eaddress))
