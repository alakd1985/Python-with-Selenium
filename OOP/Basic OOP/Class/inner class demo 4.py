class person:
    def __init__(self, name, dd, mm, yyyy):
        print('person class obj is created')
        self.name = name
        self.dob = self.Dob(dd, mm, yyyy)

    def info(self):
        print('The person name is:: ', self.name)
        self.dob.display()

    class Dob:
        def __init__(self, dd, mm, yyyy):
            self.yyyy = yyyy
            self.mm = mm
            self.dd = dd
            print('Date of Birth class is created')

        def display(self):
            print('Date of birth is {}/{}/{}'.format(self.dd, self.mm, self.yyyy))


# when the person class obj is created then person class constructor is called and simultaneously
# Dob class constructor is also called
p = person('Alak', 23, 4, 1985)
p.info()
