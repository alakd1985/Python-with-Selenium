class student:
    def __init__(self, name, marks):
        self.marks = marks
        self.name = name

    def __gt__(self, other):
        return self.marks < other.marks


s1 = student('alak', 5)
s2 = student('tom', 6)
s3 = student('tomi', 10)
print(s2 > s3)
