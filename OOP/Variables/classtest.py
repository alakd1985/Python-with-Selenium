class test:
    @classmethod
    def m(cls):
        print(id(cls))
print(id(test))
test.m()
