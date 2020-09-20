fname = input('Please enter the file name::  ')
f = open(fname, 'w')
while True:
    data = input('Enter data to write:  ')
    f.write(data + '\n')
    option = input('Do you want to add more data:: [Yes or No]   ')
    if option.lower() == 'no':
        break
f.close()
print('Data is printed successfully')