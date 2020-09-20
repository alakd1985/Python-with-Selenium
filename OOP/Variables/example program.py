# If we change the value of static variable by using either self
# or object reference variable:
# If we change the value of static variable by using either self or object reference variable, then the
# value of static variable won't be changed,just a new instance variable with that name will be
# added to that particular object.
class student:
    a = 10

    def m(self):
        self.a = 900


t = student()
t.m()
print(t.a)
print(student.a)


# Another example
class test:
    a = 10

    def m1(self):
        test.a = 800


p = test()
p.m1()
print(p.a)
print(test.a)
