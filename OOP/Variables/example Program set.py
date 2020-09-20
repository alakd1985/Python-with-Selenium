class Test:
    a = 10  # static variable

    def m(self):  # instance method
        self.a = 888  # instance variable declaration


t1 = Test()  # obj created of t1, since there is no explicit constructor default constructor will be executed
t1.m()  # we are calling instance method and inside the instance method there is a instance variable
print(Test.a)  # this one represents static variable as it is accessed by the class, so the answer is 10
print(t1.a)  # by using obj ref accessing any variable, first preference should be gone to the instance variable


# if the instance variable is not available then static variable will be accessed


class student:
    a = 10  # static variable

    def m(self):  # instance method
        student.a = 999  # static variable modifies the earlier static variable 10


t2 = student()  # obj created of t1, since there is no explicit constructor default constructor will be executed
t2.m()  # we are calling instance method and inside the instance method there is a instance variable
print(student.a)  # this one represents static variable as it is accessed by the class, so the answer is 10
print(t2.a)  # by using obj ref accessing any variable, first preference should be gone to the instance variable


# if the instance variable is not available then static variable will be accessed


class parent:
    a = 10  # static variable

    def __init__(self):  # constructor
        self.b = 20  #


t = parent()  # obj created of t, so the constructor will be called
t3 = parent()  # obj created of t3, so the constructor will be called
print('t', t.a, t.b)  # since there is no instance variable inside the obj, so static variable of a=10 will be called
print('t3', t3.a, t3.b)  # since there is no instance variable inside the obj, so static variable of a=10 will be called
t.a = 888  # since by obj reference we can not modify obj ref, therefore a new instance variable will be created
# inside the obj
t.b = 999  # we can modify instance variable by obj reference and therefore b= 20 will be replaced by 999
print('t', t.a, t.b)  # since a new reference variable is created,therefore a=888 will be executed replaced a=10
print('t3', t3.a, t3.b)  # since there is no instance variable, therefore static variable a=10 will be called and


# since there is no modification in instance variable b, so b =20 will be called


class food:
    a = 10  # static variable

    def __init__(self):  # constructor
        self.b = 20  #


u = food()  # obj created of u, so the constructor will be called
u1 = food()  # obj created of u1, so the constructor will be called
print('u', u.a,
      u.b)  # since there is no instance variable of a inside the obj, so static variable of a=10 will be called
print('u1', u1.a,
      u1.b)  # since there is no instance variable of a inside the obj, so static variable of a=10 will be called
food.a = 888  # static variable a =10 will be modified by new static variable a=888
food.b = 999  # A new static variable is declared
print('u', u.a,
      u.b)  # since a =10 is replaced by a =888, so a=888 will be executed. since instance variable is preferable to
# static variable, so b=20 will be executed than b=999
print('u1', u1.a, u1.b)  # same as the previous example
print('food', food.a,
      food.b)  # since we are accessing static variable by class, so static variable of a=888 and b = 999 will be called
