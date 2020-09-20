class student:
    @staticmethod
    def average(list1):
        result = sum(list1) / len(list1)
        print('The average is ::', result)

    @staticmethod
    def wish(name):
        for i in range(5):
            print('Good morning::', i, name)


print(student.wish('alak'))
list1 = [1, 2, 3, 4, 5]
student.average(list1)

# within the method we can not access the local variable
