class Book:
    def __init__(self,pages):
        self.pages = pages

    def __add__(self, other):
        totalpages = self.pages + other.pages
        return  totalpages
b1 = Book(100)
b2 = Book(200)
print(b2+b1)

n = int(input('Enter the number of rows::'))
for i in range(n):
    print(' '*i, end=' ')
    for j in range(n-i):
        print(chr(64+n-j), end=' ')
    print()












