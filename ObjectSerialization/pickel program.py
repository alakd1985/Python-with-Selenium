import pickle
class employee:
    def __init__(self, ename, esalary, eno, eaddress):
        self.eaddress = eaddress
        self.eno = eno
        self.esalary = esalary
        self.ename = ename

    def display(self):
        print('Employee Name:{},Employee Salary:{},Employee Number:{},Employee addresses:{}'
              .format(self.ename, self.esalary, self.eno, self.eaddress))


e = employee('John', 1000, 2, 'duke st')

with open('emp.ser','wb') as f:
    pickle.dump(e,f)

with open('emp.ser','rb') as f:
   newobj= pickle.load(f)
   print(newobj.display())
