import csv

with open('emp1.csv', 'r') as f:
    r = csv.reader(f)
    data = list(r)
    print(list(r))
    # for row in data:
    #   print(row)
    for row in data:
        for column in row:
            print(column, '\t', end='')
        print()
