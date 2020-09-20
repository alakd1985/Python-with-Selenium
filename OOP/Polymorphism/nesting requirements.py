class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages


b = Book(100)
b1 = Book(200)
b2 = Book(300)
print(b1 + b)


# if we want to add three books following methods should be used. we can also use this method to
# in case of adding two values instead of more than 2 values.


class student:
    def __init__(self, id):
        self.id = id

    def __add__(self, other):
        return student(self.id + other.id)

    def __str__(self):
        return 'total number of people: {}'.format(self.id)

    def __mul__(self, other):
        return student(self.id * other.id)


s = student(10)
s1 = student(10)
s2 = student(20)
print(s + s1 * s2)
