import csv

with open('emp1.csv', 'w', newline='') as f:
    w = csv.writer(f)  # returns the writer obj to write data
    # print(type(w))
    w.writerow(['ename', 'eno', 'esalary', 'eaddess'])
    while True:
        ename = input('Please enter name of the employee::  ')
        eno = int(input('Please enter the employee number:: '))
        esalary = float(input('Please enter the salary:: '))
        eaddess = input('Please enter the address:: ')
        w.writerow([ename, eno, eaddess, esalary])
        option = input('Do you want to insert any record: yes or No')
        if option.lower() == 'no':
            break
print('writing data completed successfully')
