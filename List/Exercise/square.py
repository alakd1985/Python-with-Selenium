# Generate and print a list of first and last 5 elements where the values are square of numbers between two numbers

def square():
    l = []
    for element in range(1, 11):
        l.append(element ** 2)
    print(l[:5])
    print(l[-5:])


print('The values are:', square())
