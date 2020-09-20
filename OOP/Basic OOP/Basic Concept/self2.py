class parent():
    def __init__(self,address,role,phone):
        #self.name = name
        self.address = address
        self.role= role
        self.phone=phone

    def chat(self):

        #print('Hello my name is:',self.name)
        print('Hello my address is:',self.address)
        print('Hello my role is:',self.role)
        print('Hello my phone is:',self.phone)

refvariable1=parent('alexandria',12,87654)
revar=parent('rakesh','duke',34,87654)
print(revar.chat())
print(refvariable1.chat())
